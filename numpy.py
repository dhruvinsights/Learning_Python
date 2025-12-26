"""
File Name : numpy_complete_basics_guide.py
Topic     : NumPy Basics – From Performance to Real-World Analysis
Level     : Beginner → Intermediate
Purpose   : Understand why NumPy is fast, how to create arrays,
            perform operations, and analyze data efficiently.
"""

import numpy as np
import time

# =================================================
# 1. WHY NUMPY? – PERFORMANCE COMPARISON
# =================================================

# Python List
python_list = list(range(1_000_000))

# NumPy Array
numpy_array = np.arange(1_000_000)

# Squaring using Python list
start_time = time.time()
squared_list = [x**2 for x in python_list]
end_time = time.time()
print(f"Python list squaring took: {end_time - start_time:.4f} seconds")

# Squaring using NumPy (vectorized operation)
start_time = time.time()
squared_array = numpy_array ** 2
end_time = time.time()
print(f"NumPy array squaring took: {end_time - start_time:.4f} seconds")

print("--------------------------------")

# =================================================
# 2. CREATING NUMPY ARRAYS
# =================================================

# From Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("np.array from list:", arr1)

# Array of zeros (2x3)
arr_zeros = np.zeros((2, 3))
print("np.zeros:\n", arr_zeros)

# Array of ones (1x5)
arr_ones = np.ones((1, 5))
print("np.ones:", arr_ones)

# Array with range
arr_range = np.arange(0, 10, 2)
print("np.arange:", arr_range)

# Evenly spaced values
arr_linspace = np.linspace(0, 1, 5)
print("np.linspace:", arr_linspace)

print("--------------------------------")

# =================================================
# 3. ARRAY OPERATIONS & BROADCASTING
# =================================================

arr_a = np.array([1, 2, 3])
arr_b = np.array([10, 20, 30])

# Element-wise operations
print("Addition:", arr_a + arr_b)
print("Multiplication:", arr_a * arr_b)

# Broadcasting with scalar
print("Scalar addition:", arr_a + 5)

# Broadcasting with 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_vector = np.array([10, 0, -10])
print("Matrix + Row Vector:\n", matrix + row_vector)

print("--------------------------------")

# =================================================
# 4. STATISTICAL FUNCTIONS
# =================================================

data = np.array([10, 12, 15, 12, 18, 20, 15, 12, 10, 15])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Sum:", np.sum(data))

print("--------------------------------")

# =================================================
# 5. ARRAY INDEXING & SLICING
# =================================================

arr = np.array([10, 20, 30, 40, 50, 60])
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 1D indexing and slicing
print("arr[2]:", arr[2])
print("arr[1:5]:", arr[1:5])

# 2D indexing
print("matrix[0,1]:", matrix[0, 1])
print("First row:", matrix[0, :])
print("First column:", matrix[:, 0])
print("Sub-matrix:\n", matrix[0:2, 1:3])

print("--------------------------------")

# =================================================
# 6. RESHAPING ARRAYS
# =================================================

flat_arr = np.array([1, 2, 3, 4, 5, 6,
                     7, 8, 9, 10, 11, 12])

print("Original array:", flat_arr)
print("Original shape:", flat_arr.shape)

# Reshape to 3x4
reshaped_arr = flat_arr.reshape((3, 4))
print("Reshaped 3x4:\n", reshaped_arr)

# Reshape using -1 (automatic inference)
reshaped_inferred = flat_arr.reshape((2, -1))
print("Reshaped with inferred dimension:\n", reshaped_inferred)

print("--------------------------------")

# =================================================
# 7. NUMPY IN ACTION – STUDENT GRADES ANALYSIS
# =================================================

# Simulated Math grades
math_grades = np.array([85, 78, 92, 88, 95, 82, 90, 85, 88, 92])

print("All Math Grades:", math_grades)
print("Number of students:", len(math_grades))
print("Average Math Score:", np.mean(math_grades))
print("Highest Score:", np.max(math_grades))
print("Lowest Score:", np.min(math_grades))
print("Standard Deviation:", np.std(math_grades))

# Boolean indexing
high_achievers = math_grades[math_grades > 90]
print("Scores above 90:", high_achievers)
print("Number of high achievers:", len(high_achievers))
