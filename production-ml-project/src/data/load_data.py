import pandas as pd
from pathlib import Path
import subprocess

DATA_PATH = Path("data/raw/telecom_customer.csv")

df = pd.read_csv(DATA_PATH)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

profile = pd.DataFrame(
    {
        "dtype": df.dtypes,
        "missing_count": df.isnull().sum(),
        "missing_pct": df.isnull().mean() * 100,
        "unique_values": df.nunique(),
    }
)

print("\nData quality profile:")
print(profile.sort_values("missing_pct", ascending=False).head(20))

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].value_counts(dropna=False).head(10))

print("\nTarget distribution:")
print(df["churn"].value_counts())
print(df["churn"].value_counts(normalize=True) * 100)

X = df.drop(columns=["churn", "Customer_ID"])
y = df["churn"]

print("Features:", X.shape)
print("Target:", y.shape)

unique_counts = X.nunique().sort_values()

print("\nFeatures with the fewest unique values:")
print(unique_counts.head(20))

numeric_columns = X.select_dtypes(include="number").columns

correlations = X[numeric_columns].corrwith(y).abs().sort_values(ascending=False)

print("\nNumerical features most correlated with churn:")
print(correlations.head(20))

print("\nSelected numerical feature statistics:")

print(
    df[["eqpdays", "hnd_price", "totmrc_Mean", "mou_Mean", "avg3mou", "avg6mou"]]
    .describe()
    .T
)
