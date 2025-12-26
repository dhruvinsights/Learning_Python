"""
File Name : matplotlib_complete_visualization_guide.py
Topic     : Data Visualization using Matplotlib (with NumPy & Pandas)
Level     : Beginner → Intermediate
Purpose   : Visualize trends, comparisons, distributions, and relationships
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# =================================================
# 1. LINE CHART – TRENDS OVER TIME
# =================================================
# Used to show progression or trend over time or sequence

exam_numbers = np.array([1, 2, 3, 4, 5])
math_scores = np.array([75, 80, 85, 90, 92])

plt.figure(figsize=(8, 5))
plt.plot(exam_numbers, math_scores, marker='o', linestyle='-')
plt.title('Student Math Scores Over Exams')
plt.xlabel('Exam Number')
plt.ylabel('Score (%)')
plt.grid(True)
plt.show()

# =================================================
# 2. BAR CHART – COMPARING CATEGORIES
# =================================================
# Used to compare discrete categories

subjects = ['Math', 'Science', 'History', 'Art']
avg_grades = [88, 82, 75, 90]

plt.figure(figsize=(8, 5))
plt.bar(subjects, avg_grades)
plt.title('Average Student Grades by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Grade (%)')
plt.show()

# =================================================
# 3. PIE CHART – DISTRIBUTION OF A WHOLE
# =================================================
# Shows proportion of each category

city_counts = {
    'New York': 30,
    'Los Angeles': 25,
    'Chicago': 15,
    'Houston': 10,
    'Miami': 20
}

cities = list(city_counts.keys())
counts = list(city_counts.values())

plt.figure(figsize=(7, 7))
plt.pie(counts, labels=cities, autopct='%1.1f%%', startangle=90)
plt.title('Student Distribution by City')
plt.axis('equal')
plt.show()

# =================================================
# 4. SCATTER PLOT – RELATIONSHIP BETWEEN VARIABLES
# =================================================
# Used to detect correlation or pattern

ages = np.array([16, 17, 18, 16, 17, 19, 18, 16, 17, 19])
math_scores = np.array([85, 78, 92, 88, 95, 82, 90, 85, 88, 92])

plt.figure(figsize=(8, 5))
plt.scatter(ages, math_scores)
plt.title('Student Age vs Math Grades')
plt.xlabel('Age')
plt.ylabel('Math Grade (%)')
plt.grid(True)
plt.show()

# =================================================
# 5. SUBPLOTS & SAVING FIGURES
# =================================================
# Multiple plots in one figure for comparison

plt.figure(figsize=(12, 5))

# Subplot 1: Line chart
plt.subplot(1, 2, 1)
plt.plot(exam_numbers, math_scores)
plt.title('Math Scores Trend')
plt.xlabel('Exam')
plt.ylabel('Score')

# Subplot 2: Bar chart
plt.subplot(1, 2, 2)
plt.bar(subjects, avg_grades)
plt.title('Average Grades by Subject')
plt.xlabel('Subject')
plt.ylabel('Grade')

plt.tight_layout()
plt.savefig('student_analysis.png')
plt.show()

# =================================================
# 6. COMPLETE EXAMPLE – STUDENT DATA DASHBOARD
# =================================================
# Simulated data as if loaded from students.csv

data = {
    'Student_ID': range(1, 11),
    'Age': [16, 17, 18, 16, 17, 19, 18, 16, 17, 19],
    'Math_Grade': [85, 78, 92, 88, 95, 82, 90, 85, 88, 92],
    'Science_Grade': [80, 85, 88, 79, 90, 85, 87, 80, 83, 89],
    'History_Grade': [70, 75, 80, 72, 85, 78, 82, 70, 75, 88],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami',
             'New York', 'Los Angeles', 'Chicago', 'Miami', 'Houston']
}

df = pd.DataFrame(data)

plt.figure(figsize=(15, 10))

# Subplot 1: Line chart
plt.subplot(2, 2, 1)
plt.plot(df['Student_ID'], df['Math_Grade'], marker='o')
plt.title('Math Grade Progression')
plt.xlabel('Student ID')
plt.ylabel('Math Grade')
plt.grid(True)

# Subplot 2: Bar chart (average grades)
plt.subplot(2, 2, 2)
avg_subject_grades = df[['Math_Grade', 'Science_Grade', 'History_Grade']].mean()
avg_subject_grades.plot(kind='bar')
plt.title('Average Grades by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Grade')
plt.xticks(rotation=0)

# Subplot 3: Pie chart (city distribution)
plt.subplot(2, 2, 3)
city_counts = df['City'].value_counts()
plt.pie(city_counts, labels=city_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Student Distribution by City')
plt.axis('equal')

# Subplot 4: Scatter plot (age vs math)
plt.subplot(2, 2, 4)
plt.scatter(df['Age'], df['Math_Grade'])
plt.title('Age vs Math Grade')
plt.xlabel('Age')
plt.ylabel('Math Grade')
plt.grid(True)

plt.suptitle('Comprehensive Student Data Analysis', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('student_dashboard.png', dpi=300)
plt.show()
