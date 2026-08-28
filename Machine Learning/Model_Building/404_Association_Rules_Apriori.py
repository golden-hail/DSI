################################################################
# Association Rule Learning (using Apriori)
################################################################

"""
Hello aspiring Data Scientists,

You keep knocking it out of the park - so here is another task!

We're looking to potentially re-jig the alcohol department within our store. Our customers are often complaining that they can't find the products they want, and are also wanting recommendations about which other products they should try.  

On top of this, our marketing team at ABC want to start running some bundled promotions to see if they can spark this department into life.

We've heard you'd been studying Association Rule Learning and wondered if this might help us solve some of these problems.

We can provide you with a file of 3,500 alcohol transactions. I don't know what you'll find...but if you could use your magic to help us on the above ideas then this could have a huge impact! Please let us know once you have some results and we can discuss!  

Thanks again,
ABC Grocery Marketing Team
"""

################################################################
# Import required packages
################################################################

from apyori import apriori
import pandas as pd

################################################################
# Import data
################################################################

# import

alcohol_transactions = pd.read_csv('data/sample_data_apriori.csv')

# drop ID column

alcohol_transactions.drop("transaction_id", axis = 1, inplace = True)

# modify data for apriori algorithm

transactions_list = []

for index, row in alcohol_transactions.iterrows():
    transaction = list(row.dropna())
    transactions_list.append(transaction)

################################################################
# Apply the Apriori algorithm
################################################################

apriori_rules = apriori(transactions_list,
                        min_support = 0.003,
                        min_confidence = 0.2,
                        min_lift = 3,
                        min_length = 2,
                        max_length = 2)

# Convert generator object to a usable list
apriori_rules = list(apriori_rules)

apriori_rules[0]

################################################################
# Convert output to DataFrame
################################################################

apriori_rules[0][2][0][0]
# >> frozenset({'American Rose'})

product1 = [list(rule[2][0][0])[0] for rule in apriori_rules]
product2 = [list(rule[2][0][1])[0] for rule in apriori_rules]
support = [rule[1] for rule in apriori_rules]
confidence = [rule[2][0][2] for rule in apriori_rules]
lift = [rule[2][0][3] for rule in apriori_rules]

apriori_rules_df = pd.DataFrame({"product1" : product1,
                                "product2" : product2,
                                "support" : support,
                                "confidence": confidence,
                                "lift" : lift})

################################################################
# Sort rules by descending lift
################################################################

# Creates a sorted DataFrame with relationships between products (their support, confidence, & lift)
apriori_rules_df.sort_values(by = "lift", ascending = False, inplace = True)

################################################################
# Search rules
################################################################

apriori_rules_df[apriori_rules_df['product1'].str.contains("New Zealand")]


