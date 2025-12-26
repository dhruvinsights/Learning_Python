"""
File Name : file_handling_practical_examples.py
Topic     : Practical File Handling Examples in Python
Level     : Beginner → Intermediate
Focus     : Real-world file processing using best practices
"""

# =================================================
# NOTE:
# Make sure a file named "story.txt" exists in the
# same folder as this Python file before running.
# Example content of story.txt:
#
# Once upon a time
# There was a programmer
# Who loved Python
# =================================================


# =================================================
# Example 1: Count Words in a File
# =================================================
# Logic:
# - Read entire file
# - Split content into words
# - Count number of words using len()

with open("story.txt", "r") as file:
    content = file.read()          # Read full file
    words = content.split()        # Split by whitespace
    print(f"Total words: {len(words)}")

print("--------------------------------")

# Expected Output:
# Total words: 10


# =================================================
# Example 2: Find the Longest Line in a File
# =================================================
# Logic:
# - Read all lines into a list
# - Use max() with key=len to find longest line
# - Strip newline for accurate length

with open("story.txt", "r") as file:
    lines = file.readlines()                       # Read all lines
    longest = max(lines, key=len)                  # Find longest line
    print(f"Longest line: {longest.strip()}")
    print(f"Length: {len(longest.strip())}")

print("--------------------------------")

# Expected Output:
# Longest line: There was a programmer
# Length: 22


# =================================================
# Example 3: Read and Number Lines
# =================================================
# Logic:
# - enumerate() gives line number
# - start=1 to begin numbering from 1
# - strip() removes extra newline characters

with open("story.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"{i}. {line.strip()}")

# Expected Output:
# 1. Once upon a time
# 2. There was a programmer
# 3. Who loved Python
