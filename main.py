import pandas as pd

columns = ["sentiment", "id", "date", "query", "username", "tweet"]

negative_df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None,
    names=columns,
    nrows=100
)

positive_df = pd.read_csv(
    "training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None,
    names=columns,
    skiprows=800000,
    nrows=100
)

df = pd.concat([negative_df, positive_df], ignore_index=True)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df["sentiment"] = df["sentiment"].map({
    0: "Negative",
    4: "Positive"
})

print("Dataset shape:", df.shape)
print(df["sentiment"].value_counts())
print(df.head())