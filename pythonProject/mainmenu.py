from appJar import gui
from pythonProject.JsonHandler import JsonHandler


class MainMenu:
    json = JsonHandler()

    def __init__(self, app: gui):
        app.startSubWindow("test")
        app.addLabel("l1", "HR Management")
        app.addButton("Add employee", self.add_employee("hello", "hello", "hello", "hello"))
        app.addButton("Read Employee file", print("no"))

        app.stopSubWindow()

    def add_employee(self, name: str, date_of_birth: str, salary: str, bonus: str):
        self.json.add_employee(name, date_of_birth, salary, bonus)


