from controllers.TaskController import TaskController
from helpers.ValidateText import ValidateText
from helpers.ValidateStatus import ValidateStatus
from helpers.ValidateId import ValidateId


def menu():
    validator = ValidateText()
    validator_status = ValidateStatus()
    validate_id = ValidateId()

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

        task = input("👉 Select Task: ")

        match task:
            case 1 | "1":
                name = validator.required_string("Add Name: ", "name").title()
                TaskController.store({
                    "name": name,
                    "description": validator.required_string("Add Description: ", "description")
                })

                print("✅ Task Created: " + name)

            case 2 | "2":
                print("🔍 List Tasks")
                keyword = input("Search: ")
                response = TaskController.index(keyword)

                for task in response:
                    print(f"🏷️ Task: {task['id']}. {task['name']}")

            case 3 | "3":
                print("🚀 Task Detail")
                task = TaskController.show(int(input("ID: ")))

                if task:
                    print(f"🏷️ ID: {task['id']}")
                    print(f"📌 Title: {task['name']}")
                    print(f"📊 Status: {task['status']}")
                    print(f"📋 Description: {task['description']}")

                else:
                    print("🐞 Task not fond")

            case 4 | "4":

                while True:

                    print("📝 Task Update")
                    task_id = validate_id.exit("tasks", input("ID: "))
                    name = validator.required_string("New Name: ", "name")
                    description = validator.required_string("New Description: ", "description")
                    status = validator_status.in_list(validator.required_string("New Status: ", "status"))

                    if name is False or description is False or status is False:
                        print("⚠️ Task update failed or task not found.")
                        break

                    else:
                        TaskController\
                            .update(
                                int(task_id),
                                {
                                    "name": name,
                                    "description": description,
                                    "status": status
                                }
                            )

                        print(f"✅ Task Updated: {task['id']}")

            case 5 | "5":
                task = TaskController.destroy(int(input("ID: ")))
                print(task)

            case 6 | "6":
                print("👋 Exiting...")
                break

            case _:
                print("❌ Invalid option. Please choose 1, 2, 3, 4, 5, 6.")


# Run the menu
if __name__ == "__main__":
    menu()
