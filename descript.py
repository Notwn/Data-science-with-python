import pandas as pd

# Load the dataset
auto_dataset = "auto_dataset.csv"
df = pd.read_csv(auto_dataset)
descc= df.describe()
print(descc)