# Define method that is executed when the user clicks on the submit buttons
# of the form
def submit(btn):
    if btn == "Cancel":
        app.stop()
    else:
        username = app.getEntry("username")
        password = app.getEntry("password")
        if username == 'justin' and password == 'abc':
            app.infoBox("Logged in", "You are now logged in!")
            app.showSubWindow("test")
            app.hide("Login Form")

        else:
            self.app.errorBox("Error", "Your credentials are invalid!")