"""
This code uses the csv reader/writer code we learned earlier to demo several
options for enhancing your team's project

"""

import pandas

from appJar import gui
from pythonProject import pandaFunctions
from pythonProject import sendEmail


# The press(btn) function determines code to be executed when a button is pressed
class main_template:

    def __init__(self):
        app = gui("Main Menu", "800x800")
        self.app = app

    def press(self, btn):
        if btn == "Exit":
            self.app.stop()
        elif btn == "Add Employee":  # writes to a csv file
            entrylist = self.app.stringBox("Data for entry",
                                           "Enter name, DOB, salary, bonus and email to write separated by commas")
            listed = entrylist.split(',')  # creates a list from user entry
            pandaFunctions.addEmployee(listed)

        elif btn == "Change salary of employee":
            self.app.startSubWindow("Change salary")
            self.app.setSize(400, 400)
            self.app.setLocation("CENTER")
            self.app.addLabelEntry("Employee name:")
            self.app.addLabelEntry("Salary:")
            self.app.addButtons(["Submit", "Close"], self.enter_salary)
            self.app.showSubWindow("Change salary")
        elif btn == "Change bonus of employee":
            self.app.startSubWindow("Change bonus")
            self.app.setSize(400, 400)
            self.app.setLocation("CENTER")
            self.app.addLabelEntry("Employee name:")
            self.app.addLabelEntry("Bonus:")
            self.app.addButtons(["Submit", "Close"], self.enter_bonus)
            self.app.showSubWindow("Change bonus")

        elif btn == "Update salary of all employees by percentage":
            salary = self.app.stringBox("Percentage", "Enter percentage to update salaries")
            starter = open(salary, 'r', newline='')

        elif btn == "Update bonuses of all employees by percentage":
            # similar to code for "Add Employee option" uses self.app.Stringbox for user entry
            bonus = self.app.stringBox("Percentage", "Enter percentage to update bonuses")
            # entrylist = self.app.stringBox("Data for entry", "Enter data to write separated by commas")
            # listed = entrylist.split(',')
            # code to find a user name based on user entered first name
        elif btn == "Find Auth Level":
            # shows a popup to ask user for a first name
            findname = self.app.stringBox("First Name", "Enter the First Name")
            # reads the csv file and assigns it to the dataframe named namesfr
            namesfr = pandas.read_csv("users.csv")
            # finds the auth_level based on the user entered first name
            answername = namesfr[namesfr.name == findname].auth_level
            # conversion of the search result to a list
            answernamel = answername.tolist()
            # displays to search result in a popup
            self.app.infoBox("Your auth level is: ", answernamel)
        # the following code mimics the one in the previous elif to
        # find a password
        elif btn == "Find Password":
            findname = self.app.stringBox("Name", "Enter the Name")
            namesfr = pandas.read_csv("users.csv")
            answerword = namesfr[namesfr.name == findname].password
            self.app.infoBox("Your Password is", answerword)
        # this is code to display a column of data
        elif btn == "Display names":
            # reads the csv file and assigns it to the namesfr dataframe
            namesfr = pandas.read_csv("users.csv")
            # assigns data from the first column to the names object
            names = namesfr.name
            # converts names to a list
            namesl = names.tolist()
            # establishes a subwindow called "one"
            self.app.startSubWindow("one")
            self.app.showSubWindow("one")
            self.app.setSize(400, 400)
            self.app.setLocation("CENTER")
            # adds a Close button to the subwindow which calls the close() function
            # when pressed
            self.app.addButton("Close", self.close)
            # the following code adds a label to the subwindow for each
            # item in the first column of the dataframe as assigned to
            # namesl
            count = 1
            for first in namesl:
                self.app.addLabel("label" + str(count), first)
                count = count + 1
        elif btn == "Sort names ascending":
            pandaFunctions.sortUsersAsc()
            self.displayNames()

        elif btn == "Sort names descending":
            pandaFunctions.sortUsersDesc()
            self.displayNames()

    def displayNames(self):
        namesfr = pandas.read_csv("userssorted.csv")
        # assigns data from the first column to the names object
        names = namesfr.name
        # converts names to a list
        namesl = names.tolist()
        # establishes a subwindow called "one"
        self.app.startSubWindow("one")
        self.app.showSubWindow("one")
        self.app.setSize(400, 400)
        self.app.setLocation("CENTER")
        # adds a Close button to the subwindow which calls the close() function
        # when pressed
        self.app.addButton("Close", self.close)
        # the following code adds a label to the subwindow for each
        # item in the first column of the dataframe as assigned to
        # namesl
        count = 1
        for first in namesl:
            self.app.addLabel("label" + str(count), first)
            count = count + 1

    def enter_salary(self, btn2):
        if btn2 == "Close":
            self.app.removeLabelEntry("Employee name:")
            self.app.removeLabelEntry("Salary:")
            self.app.removeSubWindow
            self.app.stopSubWindow()
            self.app.destroySubWindow("Change salary")
        else:
            employee = self.app.getEntry("Employee name:")
            salary = self.app.getEntry("Salary:")
            pandaFunctions.changeEmployeeSalary(employee, int(salary))

            message = ["Dear", employee, "your salary was just changed to", salary]
            namesfr = pandas.read_csv("employees.csv")
            email = namesfr[namesfr.name == employee].email
            sendEmail.sendEmail("You got a salary change!", str(message), email)

    def enter_bonus(self, btn2):
        if btn2 == "Close":
            self.app.removeLabelEntry("Employee name:")
            self.app.removeLabelEntry("Bonus:")
            self.app.removeSubWindow
            self.app.stopSubWindow()
            self.app.destroySubWindow("Change bonus")
        else:
            employee = self.app.getEntry("Employee name:")
            bonus = self.app.getEntry("Bonus:")
            pandaFunctions.changeEmployeeBonus(employee, int(bonus))

            message = ["Dear", employee, "your bonus was just changed to", bonus]
            namesfr = pandas.read_csv("employees.csv")
            email = namesfr[namesfr.name == employee].email
            sendEmail.sendEmail("You got a bonus change!", str(message), email)

    def close(self):
        self.app.stopSubWindow()
        self.app.destroySubWindow("one")

    def start(self):
        self.app.addLabel("title", "Krazy Koder")
        self.app.setLabelBg("title", "orange")
        # self.app.addImage("decor", "reeee.gif")
        self.app.setFont(18)
        self.app.setStopFunction(self.before_exit)
        self.prepare()
        self.app.go()

    # Callback execute before quitting your app
    def before_exit(self):
        return self.app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

    def prepare(self):
        self.app.addButton("Add Employee", self.press)
        self.app.addButton("Change salary of employee", self.press)
        self.app.addButton("Change bonus of employee", self.press)
        self.app.addButton("Update salary of all employees by percantage", self.press)
        self.app.addButton("Update bonuses of all employees by percentage", self.press)
        # these are the buttons that call the press function
        # note how the button names match each elif statement above
        self.app.addButton("Find Auth Level", self.press)
        self.app.addButton("Find Password", self.press)
        self.app.addButton("Display names", self.press)
        self.app.addButton("Sort names ascending", self.press)
        self.app.addButton("Sort names descending", self.press)

        self.app.addButton("Exit", self.press)
