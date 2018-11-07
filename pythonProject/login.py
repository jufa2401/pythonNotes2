from appJar import gui


class MyApplication:

    # Build the GUI
    def prepare(self, app):
        # Form GUI
        app.setTitle("Login Form")
        app.setFont(size=12, family="Times")
        app.setStopFunction(self.before_exit)

        # Add labels & entries
        # in the correct row & column
        app.addLabel("userLab", "Username:", 0, 0)
        app.addEntry("username", 0, 1)
        app.addLabel("passLab", "Password:", 1, 0)
        app.addSecretEntry("password", 1, 1)
        app.addButtons(["Submit", "Cancel"], self.submit, 3, 0, 2)  # Row 3, Column 0, Span 2

        return app

    # Build and Start your application
    def start(self):
        # Creates a UI
        app = gui()

        # Run the prebuild method that adds items to the UI
        app = self.prepare(app)

        # Make the app class-accesible
        self.app = app

        # Start appJar
        app.go()

    # Callback execute before quitting your app
    def before_exit(self):
        return self.app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")

    # Define method that is executed when the user clicks on the submit buttons
    # of the form
    def submit(self, btn):
        if btn == "Cancel":
            self.app.stop()
        else:
            username = self.app.getEntry("username")
            password = self.app.getEntry("password")
            if username == 'justin' and password == 'abc':
                self.app.infoBox("Logged in", "You are now logged in!")
                self.show_menu()
            else:
                self.app.errorBox("Error", "Your credentials are invalid!")

    def show_menu(self):
        self.app.startPagedWindow("one")
        self.app.addLabel("l1", "SubWindow One")
        # self.app.stopSubWindow()
        self.app.showSubWindow("one")


# Run the application
# `python main.py`
if __name__ == '__main__':
    # Create an instance of your application
    app = MyApplication()
    # Start your app !
    app.start()
