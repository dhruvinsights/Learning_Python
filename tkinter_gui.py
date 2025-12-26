"""
Tkinter Basics Demo
-------------------
This file demonstrates:
1. Your first Tkinter program (Hello World)
2. A simple interactive greeting app using Label, Entry, Button, and grid layout
"""

import tkinter as tk
from tkinter import messagebox


# ======================================================
# EXAMPLE 1: HELLO WORLD (BASIC TKINTER)
# ======================================================
def hello_world_window():
    """
    Creates a simple window that displays 'Hello, Tkinter!'
    """

    # 1. Create the main application window
    root = tk.Tk()

    # 2. Set the window title
    root.title("Hello World!")

    # 3. Create a Label widget
    label = tk.Label(
        root,
        text="Hello, Tkinter!",
        font=("Arial", 16),
        fg="blue"
    )

    # 4. Pack the label into the window
    label.pack(padx=20, pady=20)

    # 5. Start the Tkinter event loop
    root.mainloop()


# ======================================================
# EXAMPLE 2: SIMPLE GREETING APP (INTERACTIVE)
# ======================================================
def greeting_app():
    """
    Creates an interactive greeting app using:
    Label, Entry, Button, grid layout, and messagebox
    """

    def show_greeting():
        """
        Called when button is clicked.
        Shows greeting if name is entered.
        """
        user_name = entry.get()
        if user_name:
            messagebox.showinfo("Greeting", f"Hello, {user_name}!")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

    # Create main window
    root = tk.Tk()
    root.title("Simple Greeting App")
    root.geometry("300x150")

    # Create Label
    label = tk.Label(root, text="Enter your name:")
    label.grid(row=0, column=0, padx=10, pady=10)

    # Create Entry widget
    entry = tk.Entry(root, width=25)
    entry.grid(row=0, column=1, padx=10, pady=10)

    # Create Button
    button = tk.Button(root, text="Say Hello", command=show_greeting)
    button.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()


# ======================================================
# MAIN MENU TO RUN EXAMPLES
# ======================================================
def main_menu():
    """
    Main menu to launch Tkinter examples
    """

    root = tk.Tk()
    root.title("Tkinter Basics")
    root.geometry("300x200")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Tkinter Basics Examples",
        font=("Arial", 14, "bold")
    ).pack(pady=20)

    tk.Button(
        root,
        text="Hello World Example",
        width=25,
        command=hello_world_window
    ).pack(pady=5)

    tk.Button(
        root,
        text="Greeting App Example",
        width=25,
        command=greeting_app
    ).pack(pady=5)

    tk.Button(
        root,
        text="Exit",
        width=25,
        command=root.destroy
    ).pack(pady=15)

    root.mainloop()


# ======================================================
# PROGRAM STARTS HERE
# ======================================================
if __name__ == "__main__":
    main_menu()
