"""
File Name : file_pointer_tell_seek_complete_guide.py
Topic     : File Pointer Handling in Python (tell & seek)
Level     : Intermediate
Purpose   : Understand file pointer position, movement, and random access
"""

# =================================================
# SECTION 2: tell() METHOD – CHECK CURRENT POSITION
# =================================================
# tell() returns the current position of the file pointer
# Position is counted in BYTES from the beginning

# ---------- Example 1: Basic tell() usage ----------

with open("sample.txt", "w") as file:
    file.write("Hello World")

with open("sample.txt", "r") as file:
    print("Initial position:", file.tell())  # 0
    
    file.read(5)  # Read "Hello"
    print("After reading 5 chars:", file.tell())  # 5
    
    file.read(6)  # Read " World"
    print("After reading 6 more:", file.tell())  # 11

print("--------------------------------")

# ---------- Example 2: tell() with readline() ----------

with open("sample.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3")

with open("sample.txt", "r") as file:
    print("Start:", file.tell())  # 0
    
    file.readline()
    print("After line 1:", file.tell())  # includes '\n'
    
    file.readline()
    print("After line 2:", file.tell())

print("--------------------------------")

# =================================================
# SECTION 3: seek() METHOD – MOVE FILE POINTER
# =================================================
# seek(offset, whence)
# whence:
# 0 → beginning of file
# 1 → current position (binary mode)
# 2 → end of file (binary mode)

# ---------- Example 1: seek() from beginning ----------

with open("sample.txt", "w") as file:
    file.write("0123456789")

with open("sample.txt", "r") as file:
    file.seek(5)
    print("Position:", file.tell())
    print("Read:", file.read(3))
    
    file.seek(0)
    print("Position:", file.tell())
    print("Read:", file.read(3))

print("--------------------------------")

# ---------- Example 2: seek() from current position (binary mode) ----------

with open("sample.txt", "w") as file:
    file.write("ABCDEFGHIJ")

with open("sample.txt", "rb") as file:
    file.read(3)  # ABC
    print("Current position:", file.tell())
    
    file.seek(2, 1)  # Move forward 2 bytes
    print("After seek(2,1):", file.tell())
    print("Read:", file.read(2).decode())

print("--------------------------------")

# ---------- Example 3: seek() from end (binary mode) ----------

with open("sample.txt", "w") as file:
    file.write("0123456789")

with open("sample.txt", "rb") as file:
    file.seek(-5, 2)
    print("Position:", file.tell())
    print("Read:", file.read().decode())

print("--------------------------------")

# =================================================
# SECTION 4: PRACTICAL EXAMPLES
# =================================================

# ---------- Example 1: Read file from specific position ----------

with open("data.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"Line {i}\n")

with open("data.txt", "r") as file:
    file.seek(14)  # Skip first two lines
    print(file.read())

print("--------------------------------")

# ---------- Example 2: Read last N bytes of a file ----------

def read_last_n_bytes(filename, n):
    with open(filename, "rb") as file:
        file.seek(-n, 2)
        return file.read().decode()

with open("log.txt", "w") as file:
    file.write("This is a log file with some content")

print("Last 10 bytes:", read_last_n_bytes("log.txt", 10))

print("--------------------------------")

# ---------- Example 3: Rewind and re-read ----------

with open("data.txt", "r") as file:
    print("First read:")
    print(file.read())
    
    file.seek(0)
    print("Second read:")
    print(file.read())

print("--------------------------------")

# ---------- Example 4: Skip header in CSV ----------

with open("students.csv", "w") as file:
    file.write("Name,Age,Grade\n")
    file.write("Alice,20,A\n")
    file.write("Bob,21,B\n")

with open("students.csv", "r") as file:
    header = file.readline()  # Skip header
    for line in file:
        print(line.strip())

print("--------------------------------")

# ---------- Example 5: Random access to fixed-width records ----------

with open("records.txt", "w") as file:
    file.write("Record1\n")
    file.write("Record2\n")
    file.write("Record3\n")
    file.write("Record4\n")

record_size = 8
record_number = 3

with open("records.txt", "r") as file:
    position = (record_number - 1) * record_size
    file.seek(position)
    print(f"Record {record_number}:", file.read(record_size).strip())

print("--------------------------------")

# =================================================
# TEXT MODE vs BINARY MODE
# =================================================

with open("test.txt", "w") as file:
    file.write("Hello World")

# Text mode (limited seek)
with open("test.txt", "r") as file:
    file.seek(5)
    print(file.read())

# Binary mode (full seek)
with open("test.txt", "rb") as file:
    file.seek(5)
    print(file.read().decode())
    file.seek(2, 1)
    print(file.read().decode())

print("--------------------------------")

# =================================================
# SECTION 8: COMPLETE FILE POINTER VISUALIZER
# =================================================

def view_file_with_positions(filename):
    """Display file content with byte positions"""
    with open(filename, "r") as file:
        position = 0
        while True:
            char = file.read(1)
            if not char:
                break
            print(f"Pos {position}: '{char}' (ASCII: {ord(char)})")
            position = file.tell()

with open("demo.txt", "w") as file:
    file.write("ABC\n123")

view_file_with_positions("demo.txt")
