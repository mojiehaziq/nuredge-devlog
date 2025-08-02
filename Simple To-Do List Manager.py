# Mini Project 7: Simple To-Do List Manager

todo_list = []

def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
    elif choice == '2':
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
