import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
auto_dataset = "auto_dataset.csv"
df = pd.read_csv(auto_dataset)

#finding the average price of cars and how they differ between different types of body-styles and drive-wheels
df_test = df[["price", "body-style","drive-wheels"]]

df_grp = df_test.groupby(["body-style","drive-wheels","price"], as_index=False).mean()

df_pivot= df_grp.pivot(index= "drive-wheels", columns= "body-style")
print(df_pivot)
