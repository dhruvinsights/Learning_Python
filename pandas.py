"""
Pandas Basics to Intermediate Demo
----------------------------------
This file demonstrates:
1. Loading CSV data into Pandas
2. Viewing and understanding data
3. Selecting and filtering data
4. Sorting, grouping, and column operations
5. Handling missing values
6. Real-world student performance analysis
"""

import pandas as pd
import numpy as np
import io  # Used to simulate CSV file input


# ======================================================
# SECTION 1: LOADING AND VIEWING DATA
# ======================================================

# Simulated students.csv file using a multi-line string
csv_data = """Name,City,Math,Science,English,Age,Gender
Alice,New York,85,90,78,16,Female
Bob,Los Angeles,78,82,75,17,Male
Charlie,New York,92,88,95,16,Male
Diana,Chicago,88,91,89,17,Female
Eve,Los Angeles,95,94,92,16,Female
Frank,New York,82,79,80,17,Male
Grace,Chicago,90,85,88,16,Female
Heidi,Los Angeles,85,88,85,17,Female
Ivan,New York,88,90,87,16,Male
Judy,Chicago,92,93,91,17,Female
"""

# Load CSV data into DataFrame
df = pd.read_csv(io.StringIO(csv_data))

print("\n--- First 5 rows (df.head()) ---")
print(df.head())

print("\n--- Last 3 rows (df.tail(3)) ---")
print(df.tail(3))

print("\n--- DataFrame Info (df.info()) ---")
df.info()

print("\n--- Descriptive Statistics (df.describe()) ---")
print(df.describe())


# ======================================================
# SECTION 2: SELECTING AND FILTERING DATA
# ======================================================

# Select a single column
math_scores = df['Math']
print("\n--- Math Scores ---")
print(math_scores.head())

# Select multiple columns
grades_subset = df[['Name', 'Math', 'Science']]
print("\n--- Name, Math, Science Columns ---")
print(grades_subset.head())

# Select rows using iloc (index-based)
first_three_students = df.iloc[0:3]
print("\n--- First Three Students ---")
print(first_three_students)

# Select a row using loc (label-based)
print("\n--- Data of First Student (loc[0]) ---")
print(df.loc[0])

# Filter rows: Students from New York
ny_students = df[df['City'] == 'New York']
print("\n--- Students from New York ---")
print(ny_students)

# Filter with multiple conditions
ny_female_students = df[(df['City'] == 'New York') & (df['Gender'] == 'Female')]
print("\n--- Female Students from New York ---")
print(ny_female_students)


# ======================================================
# SECTION 3: SORTING, GROUPING, AND COLUMN OPERATIONS
# ======================================================

# Sort by Math score (descending)
top_math_students = df.sort_values(by='Math', ascending=False)
print("\n--- Top Math Students ---")
print(top_math_students.head())

# Group by City and calculate average scores
avg_scores_by_city = df.groupby('City')[['Math', 'Science', 'English']].mean()
print("\n--- Average Scores by City ---")
print(avg_scores_by_city)

# Add a new column: Total Score
df['Total Score'] = df['Math'] + df['Science'] + df['English']
print("\n--- DataFrame with Total Score ---")
print(df.head())

# Remove a column (Age)
df_no_age = df.drop(columns=['Age'])
print("\n--- DataFrame without Age column ---")
print(df_no_age.head())


# ======================================================
# SECTION 4: HANDLING MISSING DATA
# ======================================================

# Create a copy and introduce missing values
df_missing = df.copy()
df_missing.loc[1, 'Science'] = np.nan
df_missing.loc[4, 'English'] = np.nan
df_missing.loc[7, 'City'] = np.nan

print("\n--- DataFrame with Missing Values ---")
print(df_missing)

# Count missing values per column
print("\n--- Missing Values Count ---")
print(df_missing.isnull().sum())

# Drop rows with missing values
df_cleaned = df_missing.dropna()
print("\n--- After Dropping Rows with Missing Values ---")
print(df_cleaned)

# Fill missing values
df_filled = df_missing.copy()
df_filled['Science'] = df_filled['Science'].fillna(df_filled['Science'].mean())
df_filled['English'] = df_filled['English'].fillna(df_filled['English'].mean())
df_filled['City'] = df_filled['City'].fillna("Unknown")

print("\n--- After Filling Missing Values ---")
print(df_filled)


# ======================================================
# SECTION 5: REAL-WORLD STUDENT PERFORMANCE ANALYSIS
# ======================================================

# Add Average Score column
df['Average Score'] = (df['Math'] + df['Science'] + df['English']) / 3
print("\n--- DataFrame with Average Score ---")
print(df.head())

# Average performance by city
city_performance = df.groupby('City')['Average Score'].mean().sort_values(ascending=False)
print("\n--- Average Performance by City ---")
print(city_performance)

# Top 3 overall performers
top_performers = df.sort_values(by='Average Score', ascending=False).head(3)
print("\n--- Top 3 Overall Performers ---")
print(top_performers[['Name', 'City', 'Average Score']])

# Export data (commented for demo)
# df.to_csv("students_analyzed.csv", index=False)

print("\n--- Data ready for export (students_analyzed.csv) ---")
print(df.head())
