#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 18:39:47 2018

@author: mariaroldan
"""

import pandas
from appJar import gui

"""
The code below defines the press function which includes
the code to be executed when a given button is pressed
"""


def press(btn):
    if btn == "Exit":  # code to stop the entire application
        app.stop()
    # code to find a user name based on user entered first name
    elif btn == "Find Auth Level":
        # shows a popup to ask user for a first name
        findname = app.stringBox("First Name", "Enter the First Name")
        # reads the csv file and assigns it to the dataframe named namesfr
        namesfr = pandas.read_csv("users.csv")
        # finds the auth_level based on the user entered first name
        answername = namesfr[namesfr.name == findname].auth_level
        # conversion of the search result to a list
        answernamel = answername.tolist()
        # displays to search result in a popup
        app.infoBox("Your auth level is: ", answernamel)
    # the following code mimics the one in the previous elif to
    # find a password
    elif btn == "Find Password":
        findname = app.stringBox("Name", "Enter the Name")
        namesfr = pandas.read_csv("users.csv")
        answerword = namesfr[namesfr.name == findname].password
        answerwordl = answerword.tolist()
        app.infoBox("Your Password is", answerwordl)
    # this is code to display a column of data
    elif btn == "Display names":
        # reads the csv file and assigns it to the namesfr dataframe
        namesfr = pandas.read_csv("users.csv")
        # assigns data from the first column to the names object
        names = namesfr.name
        # converts names to a list
        namesl = names.tolist()
        # establishes a subwindow called "one"
        app.startSubWindow("one")
        app.showSubWindow("one")
        app.setSize(400, 400)
        app.setLocation("CENTER")
        # adds a Close button to the subwindow which calls the close() function
        # when pressed
        app.addButton("Close", close)
        # the following code adds a label to the subwindow for each
        # item in the first column of the dataframe as assigned to
        # namesl
        count = 1
        for first in namesl:
            app.addLabel("label" + str(count), first)
            count = count + 1
    elif btn == "Sort names ascending":
        names = pandas.read_csv("users.csv")
        desc_names = names.sort_values("name", ascending=False)
        desc_names.to_csv("userssorted.csv", index=False)
        print("Written to file!")
        print("Displaying....")
        displayNames()

    elif btn == "Sort names descending":
        names = pandas.read_csv("users.csv")
        asc_names = names.sort_values("name", ascending=True)
        asc_names.to_csv("userssorted.csv", index=False)
        print("Written to file!")
        print("Displaying....")
        displayNames()


def displayNames():
    namesfr = pandas.read_csv("userssorted.csv")
    # assigns data from the first column to the names object
    names = namesfr.name
    # converts names to a list
    namesl = names.tolist()
    # establishes a subwindow called "one"
    app.startSubWindow("one")
    app.showSubWindow("one")
    app.setSize(400, 400)
    app.setLocation("CENTER")
    # adds a Close button to the subwindow which calls the close() function
    # when pressed
    app.addButton("Close", close)
    # the following code adds a label to the subwindow for each
    # item in the first column of the dataframe as assigned to
    # namesl
    count = 1
    for first in namesl:
        app.addLabel("label" + str(count), first)
        count = count + 1


def close():
    # stops and destroys to window so that you can re-create
    # it from scratch with new data as needed
    app.stopSubWindow()
    app.destroySubWindow("one")


"""
This section creates the Main Window, starting with a
Splash Screen then displaying the main window with
a graphic and buttons for each action.  When a button
is pressed, the press function (above) is called
"""
app = gui("Main Menu", "800x800")
# shows a splashpage for a few seconds
app.showSplash("Hello!", fill='red', stripe='black', fg='white', font=44)
app.addLabel("title", "Welcome to the csv Main Menu")
app.setLabelBg("title", "orange")
app.addImage("decor", "k.gif")
app.setFont(18)
# these are the buttons that call the press function
# note how the button names match each elif statement above
app.addButton("Find Auth Level", press)
app.addButton("Find Password", press)
app.addButton("Display names", press)
app.addButton("Sort names ascending", press)
app.addButton("Sort names descending", press)
app.addButton("Exit", press)
app.go()
