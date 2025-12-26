"""
File Name : tkinter_widgets_complete_guide.py
Topic     : Tkinter Widgets – Complete Practical Guide
Level     : Beginner → Intermediate
Purpose   : Learn and demonstrate all commonly used Tkinter widgets
"""

import tkinter as tk
from tkinter import messagebox, ttk

# =================================================
# MAIN WINDOW
# =================================================
root = tk.Tk()
root.title("Tkinter Widgets Complete Guide")
root.geometry("700x800")

# =================================================
# 1. LABEL – DISPLAY STATIC TEXT
# =================================================
label_title = tk.Label(
    root,
    text="Tkinter Widgets Demonstration",
    font=("Arial", 18, "bold"),
    fg="blue"
)
label_title.pack(pady=10)

label_info = tk.Label(
    root,
    text="This window demonstrates common Tkinter widgets",
    font=("Arial", 12)
)
label_info.pack()

# =================================================
# 2. BUTTON – TRIGGER ACTIONS
# =================================================
def button_clicked():
    messagebox.showinfo("Button Clicked", "You clicked the button!")

btn = tk.Button(
    root,
    text="Click Me",
    command=button_clicked,
    bg="green",
    fg="white",
    font=("Arial", 12)
)
btn.pack(pady=10)

# =================================================
# 3. ENTRY – SINGLE LINE INPUT
# =================================================
def submit_name():
    name = entry_name.get()
    output_label.config(text=f"Hello, {name}!")
    entry_name.delete(0, tk.END)

tk.Label(root, text="Enter your name:").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)
entry_name.insert(0, "John Doe")

tk.Button(root, text="Submit Name", command=submit_name).pack()
output_label = tk.Label(root, text="")
output_label.pack(pady=5)

# =================================================
# 4. TEXT – MULTI LINE INPUT
# =================================================
tk.Label(root, text="Multi-line Text Input:").pack()
text_area = tk.Text(root, height=5, width=50)
text_area.pack(pady=5)
text_area.insert(tk.END, "This is a multi-line text widget.\n")

def read_text():
    content = text_area.get("1.0", tk.END)
    messagebox.showinfo("Text Content", content)

tk.Button(root, text="Read Text", command=read_text).pack(pady=5)

# =================================================
# 5. CHECKBUTTON & RADIOBUTTON
# =================================================
tk.Label(root, text="Checkbutton & Radiobutton Example").pack(pady=10)

check_var1 = tk.IntVar()
check_var2 = tk.IntVar()

tk.Checkbutton(root, text="Enable Notifications", variable=check_var1).pack(anchor="w")
tk.Checkbutton(root, text="Accept Terms", variable=check_var2).pack(anchor="w")

radio_var = tk.StringVar(value="A")

tk.Radiobutton(root, text="Option A", variable=radio_var, value="A").pack(anchor="w")
tk.Radiobutton(root, text="Option B", variable=radio_var, value="B").pack(anchor="w")
tk.Radiobutton(root, text="Option C", variable=radio_var, value="C").pack(anchor="w")

# =================================================
# 6. LISTBOX & COMBOBOX
# =================================================
tk.Label(root, text="Listbox Selection").pack(pady=5)
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=4)
for fruit in ["Apple", "Banana", "Cherry", "Date"]:
    listbox.insert(tk.END, fruit)
listbox.pack()

def show_listbox_selection():
    selected = [listbox.get(i) for i in listbox.curselection()]
    messagebox.showinfo("Listbox Selection", str(selected))

tk.Button(root, text="Get Listbox Selection", command=show_listbox_selection).pack(pady=5)

tk.Label(root, text="Combobox Selection").pack(pady=5)
combo = ttk.Combobox(root, values=["Red", "Green", "Blue"], state="readonly")
combo.set("Red")
combo.pack()

# =================================================
# 7. SCALE & SPINBOX – NUMERIC INPUT
# =================================================
tk.Label(root, text="Scale Widget").pack(pady=5)

def update_scale(val):
    scale_label.config(text=f"Scale Value: {val}")

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_scale)
scale.set(50)
scale.pack()
scale_label = tk.Label(root, text="Scale Value: 50")
scale_label.pack()

tk.Label(root, text="Spinbox Widget").pack(pady=5)
spinbox = tk.Spinbox(root, from_=0, to=10, width=5)
spinbox.pack()

# =================================================
# 8. FRAME – ORGANIZING WIDGETS
# =================================================
frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)
frame.pack(pady=10, fill="x")

tk.Label(frame, text="This is inside a Frame").pack()
tk.Button(frame, text="Frame Button").pack(pady=5)

# =================================================
# 9. MESSAGEBOX – ALERT DIALOGS
# =================================================
def show_info():
    messagebox.showinfo("Information", "This is an info message")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning")

def show_error():
    messagebox.showerror("Error", "This is an error message")

tk.Button(root, text="Show Info", command=show_info).pack(pady=2)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=2)
tk.Button(root, text="Show Error", command=show_error).pack(pady=2)

# =================================================
# START GUI LOOP
# =================================================
root.mainloop()
