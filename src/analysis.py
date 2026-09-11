import pandas as pd
import os

# File Paths

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CLEANED_DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_student_data.csv"
)

REPORTS_PATH = os.path.join(
    BASE_DIR,
    "reports"
)

# Load Cleaned Dataset

df = pd.read_csv(CLEANED_DATA_PATH)

print("Cleaned dataset loaded successfully!")

print("\nDataset Shape:")
print(df.shape)

# Display First 5 Rows

print("\nFirst 5 Rows:")
print(df.head())

# Dataset Information

print("\nDataset Information:")
df.info()

# Column Names

print("\nColumn Names:")
print(df.columns.tolist())

# Statistical Summary

print("\nStatistical Summary:")

statistical_summary = df.describe()

print(statistical_summary)

# Create Reports Folder

os.makedirs(
    REPORTS_PATH,
    exist_ok=True
)

# Save Statistical Summary

SUMMARY_PATH = os.path.join(
    REPORTS_PATH,
    "Statistical_Summary.csv"
)

statistical_summary.to_csv(
    SUMMARY_PATH
)

print("\nStatistical Summary Saved Successfully!")

print("\nSaved at:")
print(SUMMARY_PATH)

# 9) Basic Analysis

print("\n----- BASIC ANALYSIS -----")

print("\nTotal Students:")
print(len(df))


print("\nAverage Marks:")
print(
    round(
        df["Average_Marks"].mean(),
        2
    )
)


print("\nHighest Marks:")
print(
    df["Average_Marks"].max()
)


print("\nLowest Marks:")
print(
    df["Average_Marks"].min()
)


print("\nAverage Absences:")
print(
    round(
        df["absences"].mean(),
        2
    )
)

print("\nAverage Study Time:")
print(
    round(
        df["studytime"].mean(),
        2
    )
)

# Gender-wise Analysis

print("\n----- GENDER-WISE PERFORMANCE -----")

gender_performance = df.groupby(
    "sex"
)["Average_Marks"].agg(
    ["count", "mean", "max", "min"]
)

print(gender_performance)

# 11. Result Analysis

print("\n----- PASS/FAIL ANALYSIS -----")

result_analysis = df["Result"].value_counts()

print(result_analysis)

# Study Hours Analysis

print("\n----- STUDY HOURS ANALYSIS -----")

study_hours_analysis = df.groupby(
    "Study_Hours_Category"
)["Average_Marks"].mean()

print(study_hours_analysis)

# Parental Education Analysis

print("\n----- PARENTAL EDUCATION ANALYSIS -----")

parental_education_analysis = df.groupby(
    "Parental_Education"
)["Average_Marks"].agg(
    ["count", "mean"]
)

print(parental_education_analysis)
print("\nEDA Completed Successfully!")