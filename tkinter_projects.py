import tkinter as tk
from tkinter import messagebox

# ======================================================
# PROJECT 1: SIMPLE CALCULATOR
# ======================================================
def open_calculator():
    root = tk.Toplevel()
    root.title("Simple Calculator")
    root.resizable(False, False)

    display_var = tk.StringVar()
    display = tk.Entry(root, textvariable=display_var,
                       font=("Arial", 22), bd=10,
                       justify="right", width=15)
    display.grid(row=0, column=0, columnspan=4)

    current = ""
    first = None
    operator = None

    def click(char):
        nonlocal current, first, operator

        if char == "C":
            current = ""
            first = None
            operator = None
            display_var.set("")

        elif char in "+-*/":
            if current:
                first = float(current)
                operator = char
                current = ""
                display_var.set(f"{first} {operator}")

        elif char == "=":
            if first is not None and operator and current:
                try:
                    second = float(current)
                    if operator == "+": result = first + second
                    elif operator == "-": result = first - second
                    elif operator == "*": result = first * second
                    elif operator == "/":
                        if second == 0:
                            raise ZeroDivisionError
                        result = first / second

                    display_var.set(result)
                    current = str(result)
                    first = operator = None

                except:
                    display_var.set("Error")
                    current = ""
                    first = operator = None
        else:
            current += char
            display_var.set(current)

    buttons = [
        ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
        ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
        ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
        ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
        ("C",5,0)
    ]

    for text,row,col in buttons:
        btn = tk.Button(root, text=text, font=("Arial",18),
                        width=5, height=2,
                        command=lambda t=text: click(t))
        if text == "C":
            btn.grid(row=row, column=col, columnspan=4, sticky="nsew")
        else:
            btn.grid(row=row, column=col)


# ======================================================
# PROJECT 2: TO-DO LIST APPLICATION
# ======================================================
def open_todo():
    root = tk.Toplevel()
    root.title("To-Do List")
    root.geometry("400x450")

    def add_task():
        task = entry.get()
        if task:
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task")

    def delete_task():
        try:
            listbox.delete(listbox.curselection())
        except:
            messagebox.showwarning("Warning", "Select a task")

    def mark_complete():
        try:
            index = listbox.curselection()[0]
            task = listbox.get(index)
            if not task.startswith("✓ "):
                listbox.delete(index)
                listbox.insert(index, "✓ " + task)
                listbox.itemconfig(index, fg="green")
        except:
            messagebox.showwarning("Warning", "Select a task")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox = tk.Listbox(frame, width=40, height=15)
    listbox.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    tk.Button(root, text="Add Task", command=add_task).pack(pady=2)
    tk.Button(root, text="Complete Task", command=mark_complete).pack(pady=2)
    tk.Button(root, text="Delete Task", command=delete_task).pack(pady=2)


# ======================================================
# PROJECT 3: TEMPERATURE CONVERTER
# ======================================================
def open_temperature_converter():
    root = tk.Toplevel()
    root.title("Temperature Converter")
    root.geometry("350x220")

    def convert():
        try:
            temp = float(entry.get())
            if choice.get() == "C":
                result = (temp * 9/5) + 32
                result_label.config(text=f"{temp}°C = {result:.2f}°F")
            else:
                result = (temp - 32) * 5/9
                result_label.config(text=f"{temp}°F = {result:.2f}°C")
        except:
            messagebox.showerror("Error", "Enter a valid number")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    tk.Label(frame, text="Enter Temperature").grid(row=0, column=0)
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1)

    choice = tk.StringVar(value="C")
    tk.Radiobutton(frame, text="Celsius → Fahrenheit",
                   variable=choice, value="C").grid(row=1, column=0, columnspan=2)
    tk.Radiobutton(frame, text="Fahrenheit → Celsius",
                   variable=choice, value="F").grid(row=2, column=0, columnspan=2)

    tk.Button(frame, text="Convert", command=convert).grid(row=3, column=0, columnspan=2, pady=10)
    result_label = tk.Label(frame, text="", fg="blue", font=("Arial",12,"bold"))
    result_label.grid(row=4, column=0, columnspan=2)


# ======================================================
# MAIN MENU WINDOW
# ======================================================
root = tk.Tk()
root.title("Tkinter Mini Projects")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Tkinter Mini Projects",
         font=("Arial",16,"bold")).pack(pady=20)

tk.Button(root, text="Simple Calculator",
          width=20, command=open_calculator).pack(pady=5)

tk.Button(root, text="To-Do List App",
          width=20, command=open_todo).pack(pady=5)

tk.Button(root, text="Temperature Converter",
          width=20, command=open_temperature_converter).pack(pady=5)

tk.Button(root, text="Exit",
          width=20, command=root.destroy).pack(pady=15)

root.mainloop()
