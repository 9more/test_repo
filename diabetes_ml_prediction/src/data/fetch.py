from ucimlrepo import fetch_ucirepo
import pandas as pd

diabetes = fetch_ucirepo(id=296)

X = diabetes.data.features
y = diabetes.data.targets

df = pd.concat([X, y], axis=1)

ids = diabetes.data.ids

df = pd.concat([ids, diabetes.data.features, diabetes.data.targets], axis=1)

print(df.shape)
print(df.columns.tolist())


print(df["readmitted"].value_counts())
print(df["readmitted"].value_counts(normalize=True) * 100)
print(df.dtypes.value_counts())
print(df.dtypes)

missing = df.isna().sum()

missing = missing[missing > 0].sort_values(ascending=False)

print(missing)

missing_pct = (df.isna().mean() * 100).sort_values(ascending=False)

print(missing_pct[missing_pct > 0])
print((df == "?").sum().sort_values(ascending=False).head(20))
df["target"] = (df["readmitted"] == "<30").astype(int)
print(df["target"].value_counts())
print(df["target"].value_counts(normalize=True))
print(diabetes.data.ids)
print(diabetes.data.headers)
print(diabetes.metadata)
print("Unique patients:", df["patient_nbr"].nunique())
print("Total encounters:", len(df))

print(df["patient_nbr"].value_counts().head(10))
print(df[["encounter_id", "patient_nbr", "readmitted"]].head())
