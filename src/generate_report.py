import pandas as pd
import os

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


# File paths
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_student_data.csv"
)

REPORTS_PATH = os.path.join(
    BASE_DIR,
    "reports"
)

CHARTS_PATH = os.path.join(
    BASE_DIR,
    "charts"
)

PDF_PATH = os.path.join(
    REPORTS_PATH,
    "Student_Performance_Report.pdf"
)

INSIGHTS_PATH = os.path.join(
    REPORTS_PATH,
    "Business_Insights.txt"
)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Create PDF
document = SimpleDocTemplate(
    PDF_PATH,
    pagesize=A4
)

styles = getSampleStyleSheet()

story = []

# Title
story.append(
    Paragraph(
        "Student Performance Analysis Report",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))

# Dataset summary
story.append(
    Paragraph(
        "Dataset Summary",
        styles["Heading2"]
    )
)

story.append(Spacer(1, 10))

story.append(
    Paragraph(
        f"Total Students: {len(df)}",
        styles["Normal"]
    )
)

story.append(
    Paragraph(
        f"Average Marks: {df['Average_Marks'].mean():.2f}",
        styles["Normal"]
    )
)

story.append(
    Paragraph(
        f"Highest Marks: {df['Average_Marks'].max():.2f}",
        styles["Normal"]
    )
)

story.append(
    Paragraph(
        f"Lowest Marks: {df['Average_Marks'].min():.2f}",
        styles["Normal"]
    )
)

story.append(Spacer(1, 20))

# Business insights
story.append(
    Paragraph(
        "Business Insights",
        styles["Heading2"]
    )
)

story.append(Spacer(1, 10))

with open(
    INSIGHTS_PATH,
    "r"
) as file:

    insights = file.readlines()

for line in insights:

    if line.strip():

        story.append(
            Paragraph(
                line,
                styles["Normal"]
            )
        )

        story.append(
            Spacer(1, 5)
        )

# New page for charts
story.append(PageBreak())

# Charts
story.append(
    Paragraph(
        "Data Visualizations",
        styles["Heading2"]
    )
)

story.append(Spacer(1, 15))
charts = [
    "marks_histogram.png",
    "attendance_histogram.png",
    "gender_count.png",
    "study_hours_analysis.png",
    "pass_fail_pie.png",
    "marks_boxplot.png",
    "study_hours_vs_marks.png",
    "correlation_heatmap.png",
    "pairplot.png",
    "top_students.png"
]

# Add charts to PDF
for chart in charts:

    chart_path = os.path.join(
        CHARTS_PATH,
        chart
    )

    if os.path.exists(chart_path):

        story.append(
            Paragraph(
                chart.replace(
                    "_", " "
                ).replace(
                    ".png", ""
                ).title(),
                styles["Heading3"]
            )
        )

        story.append(
            Spacer(1, 5)
        )

        image = Image(
            chart_path,
            width=450,
            height=280
        )

        story.append(image)

        story.append(
            Spacer(1, 15)
        )

# Generate PDF
document.build(story)

print("\nPDF Report Generated Successfully!")
print("Saved at:", PDF_PATH)