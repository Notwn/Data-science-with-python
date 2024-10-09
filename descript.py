import pandas as pd

# Load the dataset
auto_dataset = "auto_dataset.csv"
df = pd.read_csv(auto_dataset)

#Counting the number of cars in each category
drive_wheels_counts= df["drive-wheels"].value_counts()
print(drive_wheels_counts)
