#########################################
# Matplotlib - Histograms
#########################################

# bars that represent different frequencies for a range of values 
    # *** powerful way to vizualize the spread / distribution of data
    
import matplotlib.pyplot as plt
import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")

body_data.describe()

male = body_data[body_data["Gender"]== "Male"]
female = body_data[body_data["Gender"]== "Female"]

## Histogram, input bin Default: 10
    # aplha input maskes overlap seeable
plt.style.use("seaborn-v0_8")
plt.hist(male["Weight"], bins = 20, edgecolor = "black", alpha = 0.6, color = "royalblue", label = "Male")
plt.hist(female["Weight"], bins = 20, edgecolor = "black", alpha = 0.6, color = "magenta", label = "Female")
plt.title('Distribution of Body Weight by Gender')
plt.xlabel("Weight (lbs)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()





