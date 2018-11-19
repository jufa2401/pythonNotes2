"""
This code uses the csv reader/writer code we learned earlier to demo several
options for enhancing your team's project

"""

import csv

from appJar import gui


# The press(btn) function determines code to be executed when a button is pressed
class mainTemplate:

    def __init__(self):
        app = gui("Main Menu", "800x800")
        self.app = app

    def press(self, btn):
        if btn == "Exit":
            self.app.stop()
        elif btn == "Add Employee":  # writes to a csv file
            # self.app.stringBox is used to obtain user input (more options at:
            # http://appjar.info/pythonDialogs/)
            filename = self.self.app.stringBox("Filename to edit", "Enter a filename to edit")
            entrylist = self.self.app.stringBox("Data for entry",
                                      "Enter name, DOB, salary and bonus to write separated by commas")
            listed = entrylist.split(',')  # creates a list from user entry
            f = open(filename, 'a', newline='')
            csv.writer(f).writerow(listed)
            f.close()
        elif btn == "Increase salary of employee":
            self.app.startSubWindow("two")
            self.app.setSize(400, 400)
            self.app.setLocation("CENTER")
            self.app.addLabelEntry("Employee name")
            self.app.addLabelEntry("Salary:")
            self.app.addButtons(["Submit", "Close"], self.enter)
            self.app.showSubWindow("two")
        elif btn == "Increase bonus of employee":
            filename = self.app.stringBox("Bonus", "Enter a bonus amount")
            starter = open(filename, 'r', newline='')
            reader = csv.reader(starter)
            # creates a subwindow called "one" to display output
            self.app.startSubWindow("one")
            self.app.showSubWindow("one")
            self.app.setSize(400, 400)
            self.app.setLocation("CENTER")
            # iterates through csv file and displays in the Subwindow
            count = 1
            for row in reader:
                self.app.addLabel("label" + str(count), row)
                count = count + 1
            # adds a Close button to the subwindow which calls the close() function
            # when pressed
            self.app.addButton("Close", self.close)
            starter.close()
        elif btn == "Update salary of all employees by percentage":
            salary = self.app.stringBox("Percentage", "Enter percentage to update salaries")
            starter = open(salary, 'r', newline='')
            reader = csv.reader(starter)
            for row in reader:
                self.app.infoBox("Output", row)
        elif btn == "Update bonuses of all employees by percentage":
            # similar to code for "Add Employee option" uses self.app.Stringbox for user entry
            bonus = self.app.stringBox("Percentage", "Enter percentage to update bonuses")
            # entrylist = self.app.stringBox("Data for entry", "Enter data to write separated by commas")
            # listed = entrylist.split(',')
            f = open(bonus, 'a', newline='')
            csv.writer(f).writerow(bonus)
            f.close()
        else:
            print('Pick a valid option')

    def enter(self, btn2):
        if btn2 == "Close":
            self.self.app.removeLabelEntry("Employee name")
            self.self.app.removeLabelEntry("Salary:")
            self.self.app.removeSubWindow
            self.self.app.stopSubWindow()
            self.self.app.destroySubWindow("two")
        else:
            fn = self.self.app.getEntry("Employee name")
            dt = self.self.app.getEntry("Salary:")
            dtt = dt.split(',')
            f = open(fn, 'a', newline='')
            csv.writer(f).writerow(dtt)
            f.close()

    def close(self):
        self.self.app.stopSubWindow()
        self.self.app.destroySubWindow("one")

    def start(self):
        self.app.addLabel("title", "Krazy Koder")
        self.app.setLabelBg("title", "orange")
        self.app.addImage("decor", "reeee.gif")
        self.app.setFont(18)
        self.app.setStopFunction(self.before_exit)
        self.prepare()
        self.app.go()

    # Callback execute before quitting your app
    def before_exit(self):
        return self.app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

    def prepare(self):
        self.app.addButton("Add Employee", self.press)
        self.app.addButton("Increase salary of employee", self.press)
        self.app.addButton("Increase bonus of employee", self.press)
        self.app.addButton("Update salary of all employees by percantage", self.press)
        self.app.addButton("Update bonuses of all employees by percentage", self.press)
        self.app.addButton("Exit", self.press)
