# 🎓 Student Performance Analysis

<p align="center">
  <b>Exploratory Data Analysis, SQL Analytics & Power BI Dashboard</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Pandas-EDA-150458?logo=pandas">
  <img src="https://img.shields.io/badge/NumPy-Data%20Analysis-013243?logo=numpy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange">
  <img src="https://img.shields.io/badge/Seaborn-Visualization-76B5C5">
  <img src="https://img.shields.io/badge/SQL-Analysis-blue?logo=mysql">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi">
</p>

## 📌 Project Overview

The **Student Performance Analysis** project focuses on analyzing
student academic performance using Python, SQL, Data Visualization,
and Power BI.

The project explores academic, attendance, demographic, study-related,
and parental factors to identify meaningful patterns and generate
useful insights from student data.

### 🔍 Areas Covered

- Academic Performance
- Attendance Analysis
- Study Hours Analysis
- Gender-wise Analysis
- Pass/Fail Analysis
- Student Ranking
- Correlation Analysis
- Interactive Power BI Dashboards

  ## 🎯 Project Objectives

- Analyze student academic performance
- Identify factors affecting student performance
- Study the relationship between study hours and marks
- Analyze attendance patterns
- Compare performance across genders
- Identify top-performing students
- Calculate pass and fail percentages
- Generate statistical and business insights
- Build interactive dashboards using Power BI

  ## 📊 Dataset Information

| Property | Details |
|----------|---------|
| Total Records | 395 |
| Data Type | Student Academic Dataset |
| Target Analysis | Student Performance |
| Data Format | CSV |
| Processing | Python / Pandas |
| Analysis | SQL + EDA |
| Visualization | Matplotlib + Seaborn |
| Dashboard | Power BI |

## 🛠️ Technologies & Tools

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Data Analysis & Automation |
| 🐼 Pandas | Data Cleaning & EDA |
| 🔢 NumPy | Numerical Analysis |
| 📊 Matplotlib | Data Visualization |
| 📈 Seaborn | Statistical Visualization |
| 🗄️ SQL | Analytical Queries |
| 📊 Power BI | Interactive Dashboards |
| 📄 ReportLab | PDF Report Generation |
| 💻 VS Code | Development |
| 🔧 GitHub | Version Control & Project Hosting |

## 🔄 Project Workflow

```text
Raw Dataset
     ↓
Data Loading
     ↓
Data Exploration
     ↓
Data Cleaning
     ↓
EDA & Statistical Analysis
     ↓
SQL Analysis
     ↓
Data Visualization
     ↓
Business Insights
     ↓
Automatic Report Generation
     ↓
Power BI Dashboard
```

## 🗄️ SQL Analysis

The project uses SQL to perform analytical queries on student
performance data.

### SQL Tasks

- Count total students
- Calculate average marks
- Find top 10 performing students
- Analyze gender-wise performance
- Calculate average attendance
- Find students scoring above 90%
- Analyze performance by parental education
- Rank students based on total marks
- Find average study hours
- Identify pass and fail percentages

## 🐼 Exploratory Data Analysis (EDA)

Python and Pandas are used to clean, explore and analyze the dataset.

### EDA Tasks

- Load dataset
- Explore dataset structure
- Handle missing values
- Remove duplicate records
- Analyze marks distribution
- Perform attendance analysis
- Analyze study hours
- Compare performance by gender
- Perform correlation analysis
- Generate business insights

## 📈 Data Visualization

The project includes multiple visualizations to understand
student performance patterns.

### Visualizations

| Visualization | Purpose |
|---------------|---------|
| 📊 Marks Histogram | Analyze marks distribution |
| 📊 Attendance Histogram | Analyze attendance distribution |
| 👥 Gender Count Plot | Compare student count by gender |
| 📚 Study Hours Bar Chart | Analyze study-hour categories |
| 🥧 Pass/Fail Pie Chart | Show pass and fail percentage |
| 📦 Marks Box Plot | Identify marks spread and outliers |
| 🔵 Scatter Plot | Study Hours vs Marks |
| 🔥 Correlation Heatmap | Identify relationships between variables |
| 🔗 Pair Plot | Explore relationships between multiple variables |
| 🏆 Top Students Bar Chart | Display highest-performing students |

## 📊 Sample Visualizations

### Marks Histogram

<img src="charts\marks_histogram.png" width="700">

### Study Hours vs Marks

<img src="charts\study_hours_vs_marks.png" width="700">

### Correlation Analysis

<img src="charts\correlation_heatmap.png" width="700">

### Attendance Histogram

<img src="charts\attendance_histogram.png" width="700">

### Gender Count Plot  

<img src="charts\gender_count.png" width="700">

### Pass/Fail Pie Chart 

<img src="charts\pass_fail_pie.png" width="700">

### Marks Box Plot  

<img src="charts\marks_boxplot.png" width="700">

### Scatter Plot (Study Hours vs Marks)  

<img src="charts\study_hours_vs_marks.png" width="700">

### Pair Plot  

<img src="charts\pairplot.png" width="700">

### Top Students Bar Chart    

<img src="charts\top_students.png" width="700">

## 💡 Business Insights

The analysis helps identify important patterns in student academic
performance.

Key areas of insight include:

- Relationship between study hours and marks
- Attendance and academic performance patterns
- Gender-wise performance differences
- Performance of students with different failure histories
- High-performing and low-performing student groups
- Pass and fail distribution

## 🤖 Automatic Report Generation

The project automatically generates analytical outputs from the dataset.

### Automatically Generated Outputs

- ✅ Cleaned Dataset
- ✅ Statistical Summary
- ✅ Business Insights Report
- ✅ Data Visualization Charts
- ✅ PDF Analytical Report
- ✅ Charts Embedded Inside PDF

## 📊 Power BI Dashboard

An interactive Power BI dashboard was created to analyze student
performance from multiple perspectives.

### Dashboard Pages

1. 🎓 Student Overview
2. 📚 Academic Performance
3. 📅 Attendance Dashboard
4. 👥 Gender Analysis
5. ⏱️ Study Hours Dashboard
6. 🏆 Student Ranking

### 📌 Key Performance Indicators

The dashboard includes the following KPIs:

- 👨‍🎓 Total Students
- 📊 Average Marks
- 🏆 Highest Marks
- 📅 Average Attendance
- ✅ Pass Percentage
- ⏱️ Average Study Hours

## 🖥️ Power BI Dashboard Preview

<img src="powerbi\Student_Overview.PNG" width="900">

## 📂 Project Structure

```text
Student-Performance-Analysis/
│
├── 📁 data/
│   ├── raw/
│   └── processed/
│
├── 📁 src/
│   ├── analysis.py
│   ├── data_cleaning.py
│   ├── generate_report.py
│   ├── insights.py
│   └── visualization.py
│
├── 📁 charts/
│
├── 📁 reports/
│   ├── Statistical_Summary.csv
│   ├── Business_Insights.txt
│   └── Student_Performance_Report.pdf
│
├── 📁 sql/
│   └── student_analysis.sql
│
├── 📁 powerbi/
│
├── main.py
├── requirements.txt
├── README.md
└──.gitignore

## 👩‍💻 Author

**Isha Namdev Jadhav**
