import pandas as pd

df = pd.read_csv("train.csv")

print("First 5 rows:")
print(df.head())

print("\n Dataset Shape:")
print(df.shape)

print("\n Column Names:")
print(df.columns)

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Duplicate Rows:")
print(df.duplicated().sum())

print("\n Columns with Missing Values:")
print(df.isnull().sum()[df.isnull().sum()>0])

# Fill missing Age values with average age

df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Embarked values with most common value
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column because it has too many missing values
df = df.drop(columns=["Cabin"])


df = df.drop_duplicates()

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1


df.to_csv("cleaned_dataset.csv",index=False)
print("\n Cleaned dataset saved successfully")

