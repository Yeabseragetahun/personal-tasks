import os

FILENAME = "tasks.txt"

def load_tasks():
    """Loads tasks from a text file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Saves the current tasks back to the text file."""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def show_menu():
    """Displays the interactive menu option."""
    print("\n--- Personal Task Tracker ---")
    print("1. View Current Tasks")
    print("2. Add a New Task")
    print("3. Clear All Tasks")
    print("4. Exit")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            print("\nYour Active Tasks:")
            if not tasks:
                print("[No tasks added yet!]")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        elif choice == "2":
            new_task = input("\nEnter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"Added task: '{new_task}' successfully!")
            else:
                print("Task cannot be blank.")
                
        elif choice == "3":
            confirm = input("Are you sure you want to clear everything? (y/n): ").lower()
            if confirm == 'y':
                tasks = []
                save_tasks(tasks)
                print("All tasks cleared!")
                
        elif choice == "4":
            print("\nGoodbye! Have a productive day.")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
