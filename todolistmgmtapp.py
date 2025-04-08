import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except:
        return {"tasks": []}
def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file)
    except:
        print("Error saving task.")

def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")


def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks available.")
    else:
        print("Your To-Do List:")
        for idx, task in  enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx + 1}. {task['description']} | {status}")
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks ["tasks"][task_number - 1]["complete"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        

def main():
    tasks = load_tasks()

    
    while True:
        print ("\n To-Do List Management App")
        print ("1. View Task")
        print ("2. Add Task") 
        print ("3. Complete Task")
        print ("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()
# This is a simple To-Do List Management App that allows users to view, add, and complete tasks.

