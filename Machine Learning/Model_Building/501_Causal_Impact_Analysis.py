################################################################
# Causal Impact Analysis
################################################################

'''
Hello aspiring Data Scientists,

As you know from previous projects, in July, we sent out mailers in a marketing campaign for our "delivery club". This was a new initiative that cost customers $100 per year for membership, and offered free grocery deliveries rather than the normal cost of $10 per delivery.

We really want to understand if customers who joined the club have increased their spending with us in the months following. Our hypothesis was that if customers are not paying for deliveries, they'll be tempted to shop with us more frequently, and hopefully even purchase more each time.

For now, we'd just really like to understand the uplift in sales for customers that joined the club, over and above what they would have spent had the club not come into existence - is this something you could help us with?

As always, we appreciate your hard work,
ABC Grocery Marketing Team
'''

################################################################
# Import required packages
################################################################

import warnings
from scipy.sparse import SparseEfficiencyWarning

# Clear out the annoying Pandas and Statsmodels deprecation warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=SparseEfficiencyWarning)

from causalimpact import CausalImpact
import pandas as pd

################################################################
# Import & create data
################################################################

# Import data tables

transactions = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'transactions')
campaign_data = pd.read_excel('data/grocery_database.xlsx', sheet_name = 'campaign_data')

# Aggregate transactions data to customer, date level

customer_daily_sales = transactions.groupby(['customer_id', 'transaction_date'])['sales_cost'].sum().reset_index()

# Merge on customer_id

customer_daily_sales = pd.merge(customer_daily_sales, campaign_data, how = 'inner', on = 'customer_id')


# Pivot the data to aggregate daily sales by signup group

causal_impact_df = customer_daily_sales.pivot_table(index = 'transaction_date',
                                                    columns = 'signup_flag',
                                                    values = 'sales_cost',
                                                    aggfunc = 'mean').round(2)

# provide a frequency for our DateTimeIndex (avoids a warning message)

causal_impact_df.index.freq = "D"

# for causal impact we need the impacted group in the first column

causal_impact_df = causal_impact_df[[1,0]]

# rename columns to something more meaningful

causal_impact_df.columns = ["member", "non_member"]

################################################################
# Apply Causal Impact
################################################################

pre_period = ["2020-04-01","2020-06-30"]
post_period = ["2020-07-01","2020-09-30"]

ci = CausalImpact(causal_impact_df, pre_period, post_period)

################################################################
# Plot the impact
################################################################

fig = ci.plot()

# # Looks like customers who signed up ended up spending more in store!

# # make more titles and stuff first
# # Save the plot to a file
# # Save it to your desired file path and format (PNG, PDF, SVG, etc.)

import matplotlib.pyplot as plt

# 1. Generate the plot without immediately showing it, and set the figure size
# ci.plot(show=False, figsize=(12, 10))

# 2. Get the current active figure and its subpanels (axes)
fig = plt.gcf()
axes = fig.get_axes()  # This returns a list of the 3 panels [original, pointwise, cumulative]

# 3. Add an Overall Main Title to the entire figure
fig.suptitle("Marketing Campaign Causal Impact Analysis", fontsize=18, fontweight='bold', y=0.98)

# 4. Format individual subpanels (0 = Top, 1 = Middle, 2 = Bottom)
# Panel 0: Original Data & Counterfactual
axes[0].set_title("Observed vs. Counterfactual Prediction", fontsize=12, color='darkblue', loc='left')
axes[0].set_ylabel("Sales Revenue ($)", fontsize=11)
axes[0].grid(True, linestyle='--', alpha=0.5)

# Panel 1: Pointwise Effect
axes[1].set_title("Pointwise Causal Effect (Daily Difference)", fontsize=12, color='darkblue', loc='left')
axes[1].set_ylabel("Delta", fontsize=11)

# Panel 2: Cumulative Effect
axes[2].set_title("Cumulative Effect Over Time", fontsize=12, color='darkblue', loc='left')
axes[2].set_ylabel("Total Added Value", fontsize=11)
axes[2].set_xlabel("Timeline", fontsize=12) # x-axis label is best applied to the bottom panel

# 5. Fix overlapping text elements layout automatically
plt.tight_layout()

# 6. Save or display your heavily formatted chart
fig.savefig('custom_causal_impact.png', dpi=300, bbox_inches='tight')
plt.show()

################################################################
# Extract the summary statistics & report
################################################################

print(ci.summary())
print(ci.summary(output = "report"))


