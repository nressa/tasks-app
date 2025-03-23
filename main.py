from controllers.TaskController import TaskController
from helpers.ValidateText import ValidateText


def menu():
    validator = ValidateText()

    while True:
        print("""
💡 Choose Feature:
[1] Create Task
[2] List Task
[3] Show Task
[4] Update Task
[5] Delete Task
[6] Exit
        """)

        task = input("Select Task: ")

        if task == "1":
            name = validator.required_string("Add Name: ", "name").title()
            TaskController.store({
                "name": name,
                "description": validator.required_string("Add Description: ", "description")
            })

            print("✅ Task Created: " + name)

        elif task == "2":
            print("🔍 List Tasks")
            keyword = input("Search: ")
            response = TaskController.index(keyword)

            for task in response:
                print(str(task["id"]) + ". " + task["name"])

        elif task == "3":
            print("🚀 Task Detail")
            task_id = input("ID: ")
            task = TaskController.show(task_id)
            print("🏷️ ID: " + str(task["id"]))
            print("📌 Title: " + task["name"])
            print("📊 Status: " + task["status"])
            print("📋 Description: " + task["description"])

        elif task == "4":
            print("📝 Task Update")
            task_id = input("ID: ")
            task = TaskController.update(
                    int(task_id),
                    {
                        "name": validator.required_string("New Name: ", "name"),
                        "description": validator.required_string("New Description: ", "description"),
                        "status": validator.required_string("New Status: ", "status")
                    }
                )

        elif task == "6":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, 3, 4, 6.")


# Run the menu
if __name__ == "__main__":
    menu()
