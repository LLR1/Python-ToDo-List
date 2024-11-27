import tkinter as tk
from tkinter import messagebox

# Task list
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({"task": task, "completed": False})  # Store task with completion status
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a task!")

# Function to delete the selected task
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        del tasks[selected_task]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Error", "Please select a task to delete!")

# Function to mark a task as completed
def mark_as_completed():
    try:
        selected_task = task_listbox.curselection()[0]
        tasks[selected_task]["completed"] = True  # Mark task as completed
        update_task_list()
    except IndexError:
        messagebox.showwarning("Error", "Please select a task to mark as completed!")

# Function to update the task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_text = task["task"]
        if task["completed"]:
            task_text = f"[Completed] {task_text}"  # Add a label for completed tasks
        task_listbox.insert(tk.END, task_text)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Input field for tasks
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# "Add" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# "Delete" button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# "Mark as Completed" button
mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
mark_completed_button.pack(pady=5)

# Task list (Listbox)
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Run the application
root.mainloop()

