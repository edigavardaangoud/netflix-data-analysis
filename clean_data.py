import pandas as pd

df = pd.read_csv("netflix_full_catalog.csv")

print("shape:", df.shape)
print("\nColumn info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate rows", df.duplicated().sum())
print("\nDuplicate titles (same title, posibly listed twice):", df.duplicated(subset=["title", "type"]).sum())

print("\nSample of rows with missing genres:")
print(df[df["genres"].isnull()].head())

print("\nRating range:", df["rating"].min(), "to", df["rating"].max())
print("popularity range:", df["popularity"].min(), "to", df["popularity"].max())

#1 Remove duplicate titles, keeping the first occurrence
df = df.drop_duplicates(subset=["title", "type"],keep= "first")
print("\nShape after removing dupilcates:", df.shape)


#2 Fill missing genres with aclear label instead of leaving blank
df["genres"] = df["genres"].fillna("Unknown")

#3 Drop rows with missing release dates (too few to matter, and are important for time-based analysis)
df = df.dropna(subset=["release_date"])
print("Shape after dropping missing release date:", df.shape)

#4 convert release_date from text to an actual date type, andextract the year
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["release_year"] = df["release_date"].dt.year

print("\nFinal check - missing values:")
print(df.isnull().sum())

#save the cleaned version
df.to_csv("netflix_cleaned.csv", index=False)
print("\nsaved cleaned dataset to netflix_cleaned.csv")
