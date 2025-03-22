from controllers.EntertainmentTypeController import EntertainmentTypeController
from helpers.ValidateText import ValidateText


def menu():
    validator = ValidateText()

    while True:
        print("""
            Choose Feature:
            1. Create Task
            2. List Task
        """)

        task = input("Select Task: ")

        if task == "1":
            name = ValidateText().required_string("Add Name: ", "name").title()
            response = EntertainmentTypeController.store({
                "name": name,
                "description": ValidateText().required_string("Add Description: ", "description")
            })

            print("✅ Task Created: " + name)

        elif task == "2":
            print("🔍 List Tasks")
            keyword = input("Search: ")
            response = EntertainmentTypeController.index(keyword)

            for task in response:
                print(str(task["id"]) + ". " + task["name"])

        elif task == "exit":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, or 'exit'.")


# Run the menu
if __name__ == "__main__":
    menu()