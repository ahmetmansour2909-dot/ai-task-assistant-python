from agent import analyze_task, generate_suggestions, generate_summary
from storage import load_tasks, add_task, delete_task, update_task


def show_menu():
    print("\n=== AI Task Assistant ===")
    print("1. Add new task")
    print("2. Show all tasks")
    print("3. Delete a task")
    print("4. Edit a task")
    print("5. AI Suggestions")
    print("6. AI Task Summary")
    print("7. Exit")


def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        print(
            f"{i}. {task['text']} | "
            f"Priority: {task['priority']} | "
            f"Category: {task['category']}"
        )


def add_new_task():
    text = input("Enter task description: ")
    task = analyze_task(text)
    add_task(task)
    print("[AI] Task added successfully.")


def delete_existing_task():
    show_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if delete_task(index):
        print("[AI] Task deleted successfully.")
    else:
        print("[Error] Invalid task number.")


def edit_existing_task():
    show_tasks()
    index = int(input("Enter task number to edit: ")) - 1
    new_text = input("Enter new task description: ")
    if update_task(index, new_text):
        print("[AI] Task updated successfully.")
    else:
        print("[Error] Invalid task number.")


def show_ai_suggestions():
    tasks = load_tasks()
    print("\n[AI Suggestion]")
    print(generate_suggestions(tasks))


def show_summary():
    tasks = load_tasks()
    summary = generate_summary(tasks)

    print("\n=== Task Summary ===")
    print(f"Total tasks : {summary['total']}")
    print(f"High        : {summary['high']}")
    print(f"Medium      : {summary['medium']}")
    print(f"Low         : {summary['low']}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_existing_task()
        elif choice == "4":
            edit_existing_task()
        elif choice == "5":
            show_ai_suggestions()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
