from controllers.EntertainmentTypeController import EntertainmentTypeController


def store_entertainment_type():
    controller = EntertainmentTypeController
    data = {"name": input("Add Name: "), "description": input("Add Description: ")}

    response = controller.store(data)

    if response is True:
        store_entertainment_type()
    else:
        exit()


store_entertainment_type()
