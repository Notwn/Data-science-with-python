import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
auto_dataset = "auto_dataset.csv"
df = pd.read_csv(auto_dataset)

#Counting the number of cars in each category
drive_wheels_counts= df["drive-wheels"].value_counts()
print(drive_wheels_counts)
# Convert the 'price' column to numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')

sns.boxplot(x="drive-wheels", y="price", data=df ,hue= "drive-wheels", hue_order=["fwd","rwd","4wd" ], palette=["blue","orange","green"])
plt.show()