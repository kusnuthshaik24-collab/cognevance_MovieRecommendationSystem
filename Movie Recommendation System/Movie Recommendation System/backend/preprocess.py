import pandas as pd

df = pd.read_csv("dataset.csv")

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df.to_csv("cleaned_dataset.csv", index=False)

print("Data cleaned successfully")