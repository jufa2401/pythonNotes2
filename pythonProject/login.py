from appJar import gui
from pythonProject import main_template

# from mainmenu import MainMenu
class Login:

    # Build the GUI
    def prepare(self, app):
        # Form GUI
        app.setTitle("Login Form")
        app.setFont(size=12, family="Verdana")
        # Add labels & entries
        # in the correct row & column
        app.addLabel("userLab", "Username:", 0, 0)
        app.addEntry("username", 0, 1)
        app.setFocus("username")

        app.addLabel("passLab", "Password:", 1, 0)
        app.addSecretEntry("password", 1, 1)

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
                    # app.showSubWindow("test")
                    app.hide("Login Form")
                    app.stop()
                    menu = main_template.main_template()
                    menu.start()

                else:
                    self.app.errorBox("Error", "Your credentials are invalid!")

        app.addButtons(["Submit", "Cancel"], submit, 3, 0, 2)  # Row 3, Column 0, Span 2

        # mainmenu.MainMenu(app)

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


# Run the application
# `python main.py`
if __name__ == '__main__':
    # Create an instance of your application
    app = Login()
    # Start your app !
    app.start()
