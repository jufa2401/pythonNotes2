from appJar import gui #imports the gui library from appJar

"""
This is the function that determines code executed when each button is pressed

QUIZ ITEM:  Each teammember should replace the Button name (e.g. Button 1) and 
text to be displayed using the print statement.  Note that the Button name should
match the Button names in the gui definition starting on line 37.

Add code for your functions after each print statement

"""
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Button 1":
        app.infoBox("b1","describe/code your first function")
    elif btn == "Button 2":
        app.infoBox("b1","describe/code your second function")
    elif btn == "Button 3":
        app.infoBox("b1","describe/code your third function")      
    elif btn == "Button 4":
        app.infoBox("b1","describe/code your fourth function")    
    elif btn == "Button 5":
        app.infoBox("b1","describe/code your fifth function")   
    else:
        print('Pick a valid option')

"""
The code below defines the gui, adding buttons, labels, images, color, etc.

QUIZ ITEM: Make changes to the title (line 37), image (line 39), and button
names (lines 42-46)

"""

app=gui("Main Menu","500x500")

#Replace "Blank Team" with your team name in line 41

app.addLabel("title", "Welcome to Blank Team's Main Menu")
app.setLabelBg("title", "orange")

#Find your team gif image, save to your project code folder, and replace k.gif
#with the image file name in line 47

app.addImage("decor","k.gif")
app.setFont(18)

#change the names Button 1-5 with names aligning with your team functions
#make sure they match the Button names in the press function above

app.addButton("Button 1", press)
app.addButton("Button 2", press)
app.addButton("Button 3", press)
app.addButton("Button 4", press)
app.addButton("Button 5", press)
app.addButton("Exit",press)
app.go() #displays the gui


