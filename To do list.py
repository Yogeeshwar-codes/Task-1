import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_num - 1)
        print(f"Deleted task: {deleted['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
