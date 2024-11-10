# Since Python will think user.py is in the same directory as
# where I'm importing this file from, you need to add a dot
# to the import to indicate the location more accurately.
# Instead of Python thinking user.py is in the 'Chapter 9'
# folder, it will know it can locate user.py in 'Modules'.
from .user import *

class Admin(User):
    def __init__(self, first, last, age, gender, city):
        super().__init__(first, last, age, gender, city)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, *privileges):
        self.privileges = list(privileges)
    
    def show_privileges(self):
        privileges = ", ".join(self.privileges)
        print(f"The user has the privileges to: {privileges}")