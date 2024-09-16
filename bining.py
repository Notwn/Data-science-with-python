import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
auto_dataset = "auto_dataset.csv"
df = pd.read_csv(auto_dataset)

# Convert the 'price' column to numeric, forcing errors to NaN
df["price"] = pd.to_numeric(df["price"], errors='coerce')

# Remove rows with missing 'price' values (optional, depending on your handling strategy)
df = df.dropna(subset=["price"])

# Define the bins and labels
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["low", "medium", "high"]


df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)

#printing the output to verify
print(df[["price", "price-binned"]].head(20))


# Plot a histogram of the binned prices
plt.figure(figsize=(8, 6))
df["price-binned"].value_counts().sort_index().plot(kind='bar', color='aqua', edgecolor='black')
plt.title("Price Distribution (Binned)")
plt.xlabel("Price Category")
plt.ylabel("Number of Vehicles")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

