import os
import matplotlib.pyplot as plt

# Function to add a task
def add_task(tasks, task_name, priority, due_date):
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'name': task_name,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

# Function to remove a task
def remove_task(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task['name']}' removed.")
    else:
        print("Task not found.")

# Function to mark a task as completed
def mark_task_completed(tasks, task_id):
    task = find_task_by_id(tasks, task_id)
    if task:
        task['completed'] = True
        save_tasks(tasks)
        print(f"Task '{task['name']}' marked as completed.")
    else:
        print("Task not found.")

# Function to list all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Task List:")
    for task in tasks:
        print(f"ID: {task['id']}, Name: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")

# Function to find a task by ID
def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['id']},{task['name']},{task['priority']},{task['due_date']},{int(task['completed'])}\n")

# Function to load tasks from a file
def load_tasks():
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                task_info = line.strip().split(',')
                task = {
                    'id': int(task_info[0]),
                    'name': task_info[1],
                    'priority': task_info[2],
                    'due_date': task_info[3],
                    'completed': bool(int(task_info[4]))
                }
                tasks.append(task)
    return tasks

# Function to visualize task priorities using a bar chart
def visualize_priorities(tasks):
    priorities = {'high': 0, 'medium': 0, 'low': 0}

    for task in tasks:
        priority = task['priority']
        if priority in priorities:
            priorities[priority] += 1

    labels = list(priorities.keys())
    counts = list(priorities.values())

    plt.bar(labels, counts)
    plt.xlabel('Priority')
    plt.ylabel('Count')
    plt.title('Task Priorities')
    plt.show()

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Visualize Task Priorities")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            task_name = input("Enter task name: ")
            priority = input("Enter priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, task_name, priority, due_date)
        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            remove_task(tasks, task_id)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(tasks, task_id)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            visualize_priorities(tasks)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if _name_ == "_main_":
    main()
