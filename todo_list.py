# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

def show_menu():
    """Displays the main menu."""
    print("\n==== To-Do List Menu ====")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

def add_task():
    """Adds a new task to the to-do list."""
    task = input("Enter the task you want to add: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks():
    """Displays all tasks."""
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n==== To-Do List ====")
        for index, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{index}. [{status}] {task['task']}")

def mark_task_done():
    """Marks a task as done."""
    if not tasks:
        print("\nNo tasks to mark as done.")
        return

    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task {task_num} marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    """Deletes a task from the list."""
    if not tasks:
        print("\nNo tasks to delete.")
        return

    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function to run the to-do list app."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
