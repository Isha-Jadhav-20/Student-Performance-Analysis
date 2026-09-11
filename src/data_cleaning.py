import pandas as pd
import numpy as np
import os

# File Paths

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "student_data.csv"
)

PROCESSED_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_student_data.csv"
)

# Load Dataset

df = pd.read_csv(RAW_DATA_PATH,sep="\t")

print("Dataset loaded successfully!")
print("Original Dataset Shape:", df.shape)

# Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows with missing values
df.dropna(inplace=True)

# Remove Duplicate Rows

print("\nDuplicate Rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)

# Create Student ID

df.insert(
    0,
    "Student_ID",
    range(1, len(df) + 1)
)

# Create Total Marks

df["Total_Marks"] = (
    df["G1"] +
    df["G2"] +
    df["G3"]
)

# Create Average Marks

df["Average_Marks"] = (
    df["Total_Marks"] / 3
).round(2)

# Create Percentage

df["Percentage"] = (
    df["Total_Marks"] / 60 * 100
).round(2)

# Create Pass / Fail Column

df["Result"] = np.where(
    df["G3"] >= 10,
    "Pass",
    "Fail"
)

# Parental Education Score

df["Parental_Education_Score"] = (
    df["Medu"] + df["Fedu"]
)

# Parental Education Category

def education_category(score):

    if score <= 2:
        return "Low"

    elif score <= 5:
        return "Medium"

    elif score <= 8:
        return "High"

    else:
        return "Very High"

df["Parental_Education"] = df[
    "Parental_Education_Score"
].apply(education_category)

# 12) Study Hours Category

studytime_mapping = {
    1: "<2 Hours",
    2: "2-5 Hours",
    3: "5-10 Hours",
    4: ">10 Hours"
}

df["Study_Hours_Category"] = df[
    "studytime"
].map(studytime_mapping)

# Student Ranking

df["Student_Rank"] = df[
    "Total_Marks"
].rank(
    ascending=False,
    method="dense"
).astype(int)

# Create Processed Folder

os.makedirs(
    os.path.dirname(PROCESSED_DATA_PATH),
    exist_ok=True
)

# 15. Save Cleaned Dataset

df.to_csv(
    PROCESSED_DATA_PATH,
    index=False
)

# Final Output

print("\nData Cleaning Completed Successfully!")
print("Final Dataset Shape:", df.shape)

print("\nCleaned Dataset Saved At:")
print(PROCESSED_DATA_PATH)

print("\nNew Columns Added:")
print([
    "Student_ID",
    "Total_Marks",
    "Average_Marks",
    "Percentage",
    "Result",
    "Parental_Education_Score",
    "Parental_Education",
    "Study_Hours_Category",
    "Student_Rank"
])