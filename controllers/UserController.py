class UserController:

    def __init__(self, name):
        self.name = name

    @classmethod
    def store(cls, data):
        return data

