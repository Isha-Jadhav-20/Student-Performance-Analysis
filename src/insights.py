import pandas as pd
import os

# File paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_student_data.csv"
)

REPORT_PATH = os.path.join(
    BASE_DIR,
    "reports",
    "Business_Insights.txt"
)

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")

# Basic calculations
total_students = len(df)

average_marks = df["Average_Marks"].mean()

highest_marks = df["Average_Marks"].max()

lowest_marks = df["Average_Marks"].min()

pass_percentage = (
    (df["Result"] == "Pass").sum()
    / total_students
) * 100

fail_percentage = (
    (df["Result"] == "Fail").sum()
    / total_students
) * 100

average_absences = df["absences"].mean()

average_study_time = df["studytime"].mean()

# Gender-wise performance
gender_performance = df.groupby(
    "sex"
)["Average_Marks"].mean()

# Study hours analysis
study_analysis = df.groupby(
    "Study_Hours_Category"
)["Average_Marks"].mean()

# Top 10 students
top_students = df.sort_values(
    "Total_Marks",
    ascending=False
).head(10)

# Create reports folder
os.makedirs(
    os.path.dirname(REPORT_PATH),
    exist_ok=True
)

# Write insights to text file
with open(REPORT_PATH, "w") as file:

    file.write("STUDENT PERFORMANCE - BUSINESS INSIGHTS\n")
    file.write("=" * 50 + "\n\n")

    file.write(
        f"Total Students: {total_students}\n"
    )

    file.write(
        f"Average Marks: {average_marks:.2f}\n"
    )

    file.write(
        f"Highest Marks: {highest_marks:.2f}\n"
    )

    file.write(
        f"Lowest Marks: {lowest_marks:.2f}\n"
    )

    file.write(
        f"Pass Percentage: {pass_percentage:.2f}%\n"
    )

    file.write(
        f"Fail Percentage: {fail_percentage:.2f}%\n"
    )

    file.write(
        f"Average Absences: {average_absences:.2f}\n"
    )

    file.write(
        f"Average Study Time: {average_study_time:.2f}\n"
    )

    file.write("\nGender-wise Average Marks:\n")
    file.write(
        gender_performance.round(2).to_string()
    )

    file.write("\n\nAverage Marks by Study Hours:\n")
    file.write(
        study_analysis.round(2).to_string()
    )

    file.write("\n\nTop 10 Students:\n")
    file.write(
        top_students[
            [
                "Student_ID",
                "Total_Marks",
                "Average_Marks",
                "Result"
            ]
        ].to_string(index=False)
    )

print("\nBusiness Insights Generated Successfully!")
print("Saved at:", REPORT_PATH)