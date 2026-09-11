print("=" * 50)
print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

print("\n1. Data Cleaning Started...")
import src.data_cleaning

print("\n2. Data Analysis Started...")
import src.analysis

print("\n3. Charts Generation Started...")
import src.visualization

print("\n4. Business Insights Started...")
import src.insights

print("\n5. PDF Report Generation Started...")
import src.generate_report

print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 50)
print("\nGenerated Outputs:")
print("1. Cleaned Dataset")
print("2. Statistical Summary")
print("3. Business Insights")
print("4. Charts")
print("5. PDF Report")