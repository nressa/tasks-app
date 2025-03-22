from controllers.EntertainmentTypeController import EntertainmentTypeController
from helpers.ValidateText import ValidateText


def store_entertainment_type():
    controller = EntertainmentTypeController

    data = {
        "name": ValidateText().required_string("Add Name: ", "name"),
        "description": ValidateText().required_string("Add Description: ", "description")
    }

    response = controller.store(data)

    if response is True:
        store_entertainment_type()
    else:
        exit()


store_entertainment_type()
