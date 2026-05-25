import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Name": ["Tharun", "Ravi", "Anu", "Kiran", "Sneha"],
    "Maths": [85, 45, 95, 76, 88],
    "Science": [90, 50, 92, 80, 84],
    "English": [78, 40, 98, 70, 91]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate Total
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Calculate Average
df["Average"] = df["Total"] / 3

# Grade Function
def calculate_grade(avg):

    if avg >= 90:
        return "A"

    elif avg >= 75:
        return "B"

    elif avg >= 50:
        return "C"

    else:
        return "Fail"

# Apply grades
df["Grade"] = df["Average"].apply(calculate_grade)

# Rank students
df["Rank"] = df["Average"].rank(ascending=False)

# Display Report
print("\n===== STUDENT PERFORMANCE REPORT =====\n")
print(df)

# Find Topper
topper = df.loc[df["Average"].idxmax()]

print("\n===== TOPPER DETAILS =====")
print("Name :", topper["Name"])
print("Average :", round(topper["Average"], 2))
print("Grade :", topper["Grade"])

# Failed Students
failed_students = df[df["Grade"] == "Fail"]

print("\n===== FAILED STUDENTS =====")

if len(failed_students) > 0:
    print(failed_students[["Name", "Average"]])
else:
    print("No Failed Students")

# Save report to CSV
df.to_csv("student_report.csv", index=False)

print("\nReport saved as student_report.csv")

# Visualization
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")

plt.savefig("performance_chart.png")
print("Chart saved")