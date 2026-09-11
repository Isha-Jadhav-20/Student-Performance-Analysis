import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

CHARTS_PATH = os.path.join(
    BASE_DIR,
    "charts"
)

# Create Charts Folder

os.makedirs(
    CHARTS_PATH,
    exist_ok=True
)

# Load Dataset

df = pd.read_csv(
    CLEANED_DATA_PATH
)

print("Dataset loaded successfully!")

# Marks Histogram

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Average_Marks",
    bins=10,
    kde=True
)

plt.title("Average Marks Distribution")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "marks_histogram.png"
    )
)

plt.close()

# Absences Histogram

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="absences",
    bins=15,
    kde=True
)

plt.title("Absences Distribution")
plt.xlabel("Number of Absences")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "attendance_histogram.png"
    )
)

plt.close()

# Gender Count Plot

plt.figure(figsize=(6, 5))

sns.countplot(
    data=df,
    x="sex"
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Student Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "gender_count.png"
    )
)

plt.close()

# Study Hours Analysis

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Study_Hours_Category",
    y="Average_Marks",
    estimator="mean"
)

plt.title("Average Marks by Study Hours")
plt.xlabel("Study Hours Category")
plt.ylabel("Average Marks")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "study_hours_analysis.png"
    )
)

plt.close()

# Pass / Fail Pie Chart

result_counts = df[
    "Result"
].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    result_counts.values,
    labels=result_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Pass vs Fail Percentage")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "pass_fail_pie.png"
    )
)

plt.close()

# Marks Box Plot

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Average_Marks"
)

plt.title("Average Marks Box Plot")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "marks_boxplot.png"
    )
)

plt.close()

# Study Time vs Marks

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="studytime",
    y="Average_Marks",
    hue="sex"
)

plt.title("Study Time vs Average Marks")
plt.xlabel("Study Time")
plt.ylabel("Average Marks")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "study_hours_vs_marks.png"
    )
)

plt.close()

# Correlation Heatmap

numerical_columns = df.select_dtypes(
    include="number"
)

plt.figure(figsize=(16, 10))

sns.heatmap(
    numerical_columns.corr(),
    annot=False,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "correlation_heatmap.png"
    )
)

plt.close()

# Pair Plot

pairplot_data = df[
    [
        "age",
        "studytime",
        "absences",
        "G1",
        "G2",
        "G3",
        "Average_Marks"
    ]
]

pair_plot = sns.pairplot(
    pairplot_data
)

pair_plot.savefig(
    os.path.join(
        CHARTS_PATH,
        "pairplot.png"
    )
)

plt.close()

# Top 10 Students

top_students = df.sort_values(
    by="Total_Marks",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=top_students,
    x="Student_ID",
    y="Total_Marks"
)

plt.title("Top 10 Performing Students")
plt.xlabel("Student ID")
plt.ylabel("Total Marks")

plt.tight_layout()

plt.savefig(
    os.path.join(
        CHARTS_PATH,
        "top_students.png"
    )
)

plt.close()

# Final Message

print("\nAll Charts Generated Successfully!")

print("\nCharts saved in:")
print(CHARTS_PATH)