import pandas as pd

RAW = "Sleep_health_and_lifestyle_dataset.csv"
OUT = "sleep_clean.csv"

df = pd.read_csv(RAW)

bp = df["Blood Pressure"].str.split("/", expand=True).astype(int)
df["Systolic"] = bp[0]
df["Diastolic"] = bp[1]

df["Sleep Disorder"] = df["Sleep Disorder"].fillna("None")
df["BMI Category"] = df["BMI Category"].replace({"Normal Weight": "Normal"})

df = df.drop(columns=["Person ID", "Blood Pressure"])
df.to_csv(OUT, index=False)

print(df.head())
print("\nShape:", df.shape)
print("\nNumeric summary:")
print(df.describe())
print("\nSleep Disorder counts:", df["Sleep Disorder"].value_counts().to_dict())
print("Occupation counts:", df["Occupation"].value_counts().to_dict())
