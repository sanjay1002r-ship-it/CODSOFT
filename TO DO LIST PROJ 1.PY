storage = []

while True:
    print("\n=======================")
    print("TO DO LIST")
    print("=======================")
    print("1. ADD NEW TASK")
    print("2. VIEW TASK")
    print("3. DELETE TASK")
    print("4. COMPLETE TASK")
    print("5. EXIT")

    choice = int(input("ENTER THE CHOICE NUMBER: "))

    if choice == 1:
        task = input("Enter the task: ")
        storage.append(task)
        print("Task added successfully.")

    elif choice == 2:
        if len(storage) == 0:
            print("No tasks are available.")
        else:
            print("\nYOUR TASKS")
            for i in range(len(storage)):
                print(f"{i + 1}. {storage[i]}")

    elif choice == 3:
        if len(storage) == 0:
            print("No tasks are available.")
        else:
            print("\nYOUR TASKS")
            for i in range(len(storage)):
                print(f"{i + 1}. {storage[i]}")

            delete_task = int(input("Enter the task number to delete: "))
            if 1 <= delete_task <= len(storage):
                removed = storage.pop(delete_task - 1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")

    elif choice == 4:
        if len(storage) == 0:
            print("No tasks are available.")
        else:
            print("\nYOUR TASKS")
            for i in range(len(storage)):
                print(f"{i + 1}. {storage[i]}")

            completed_task = int(input("Enter the task number: "))
            if 1 <= completed_task <= len(storage):
                storage[completed_task - 1] = storage[completed_task - 1] + " [completed]"
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    elif choice == 5:
        print("EXIT")
        print("Thanks for choosing to-do list.")
        break

    else:
        print("Invalid number.")
