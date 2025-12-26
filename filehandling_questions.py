"""
File Name : file_handling_solutions_complete.py
Topic     : File Handling – Basic to Advanced Solutions
Level     : Beginner → Advanced
Purpose   : Demonstrate real-world file handling with error handling, logging,
            random access, reverse reading, and buffering concepts.
"""

# =================================================
# SOLUTION TO BASIC QUESTION 1
# Create and write to a file
# =================================================

with open("my_first_file.txt", "w") as file:
    file.write("Hello, Python file handling!")

print("File 'my_first_file.txt' created and written.")

print("--------------------------------")

# =================================================
# SOLUTION TO INTERMEDIATE QUESTION 6
# Copy file content with error handling
# =================================================

try:
    # Create a dummy source file
    with open("source.txt", "w") as f:
        f.write("This is the source content.")

    # Read from source file
    with open("source.txt", "r") as source_file:
        content = source_file.read()

    # Write to destination file
    with open("destination.txt", "w") as dest_file:
        dest_file.write(content)

    print("Content copied from 'source.txt' to 'destination.txt'.")

except FileNotFoundError:
    print("Error: The source file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("--------------------------------")

# =================================================
# SOLUTION TO ADVANCED QUESTION 11
# Log File Processing
# =================================================

import re
from collections import Counter

log_file_content = """INFO: User logged in
ERROR: Database connection failed.
WARNING: Low disk space.
ERROR: API request timeout.
INFO: Data processed.
ERROR: Database connection failed.
DEBUG: Temp file cleaned.
ERROR: Invalid input format.
"""

# Create a dummy log file
with open("app.log", "w") as f:
    f.write(log_file_content)

error_lines = []
error_messages = []
total_errors = 0

try:
    with open("app.log", "r") as infile:
        for line in infile:
            if "ERROR" in line:
                error_lines.append(line.strip())
                total_errors += 1

                # Extract error message after "ERROR:"
                match = re.search(r"ERROR:\s*(.*)", line)
                if match:
                    error_messages.append(match.group(1).strip())

    # Write extracted error lines to a new file
    with open("errors.log", "w") as outfile:
        for line in error_lines:
            outfile.write(line + "\n")

    print(f"Extracted {total_errors} error lines to 'errors.log'.")

    # Count most frequent error messages
    error_counts = Counter(error_messages)
    print("\nTop 3 most frequent error messages:")
    for msg, count in error_counts.most_common(3):
        print(f"- '{msg}': {count} times")

except FileNotFoundError:
    print("Error: 'app.log' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print("--------------------------------")

# =================================================
# SOLUTION TO ADVANCED QUESTION 14
# Reverse Reading a File using seek() and tell()
# =================================================

def read_lines_reverse(filename):
    """
    Reads a file line-by-line in reverse order using binary mode
    and precise file pointer movement.
    """
    with open(filename, "rb") as f:
        f.seek(0, 2)  # Move to end of file
        current_pos = f.tell()
        line_buffer = bytearray()

        while current_pos > 0:
            current_pos -= 1
            f.seek(current_pos)
            char = f.read(1)

            if char == b'\n':
                if line_buffer:
                    yield line_buffer[::-1].decode().strip()
                    line_buffer = bytearray()
            else:
                line_buffer.extend(char)

        # Yield the first line (if no newline at start)
        if line_buffer:
            yield line_buffer[::-1].decode().strip()


# Create sample file
with open("test_reverse.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\nLast Line")

print("Reading 'test_reverse.txt' in reverse:")
for line in read_lines_reverse("test_reverse.txt"):
    print(line)

print("--------------------------------")

# =================================================
# SOLUTION TO ADVANCED QUESTION 15
# Buffering vs Unbuffered File Writing
# =================================================

import time

def buffered_vs_unbuffered_write(filename_buffered, filename_unbuffered):
    """
    Demonstrates difference between buffered and unbuffered file writing.
    """

    print("Writing to buffered and unbuffered files...")

    # Buffered write (default behavior)
    with open(filename_buffered, "w") as f_buffered:
        f_buffered.write("Buffered data line 1\n")
        print("Buffered: Data written to memory buffer.")
        time.sleep(1)  # Simulate delay / crash risk
        f_buffered.write("Buffered data line 2\n")
        f_buffered.flush()  # Force write to disk
        print("Buffered: Data explicitly flushed to disk.")

    # Unbuffered write (binary mode required)
    with open(filename_unbuffered, "wb", buffering=0) as f_unbuffered:
        f_unbuffered.write(b"Unbuffered data line 1\n")
        print("Unbuffered: Data immediately written to disk.")
        time.sleep(1)
        f_unbuffered.write(b"Unbuffered data line 2\n")
        print("Unbuffered: Data immediately written to disk.")

# Example usage
buffered_vs_unbuffered_write("buffered_log.txt", "unbuffered_log.txt")
