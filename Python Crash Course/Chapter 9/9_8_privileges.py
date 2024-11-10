# 9-8. Privileges: Write a separate Privileges class. The
# class should have one attribute, privileges, that stores
# a list of strings as described in Exercise 9-7. Move the
# show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new
# instance of Admin and use your method to show its
# privileges.

class User:
    def __init__(self, first, last, age, gender, city):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.city = city
        self.login_attempts = 0
    
    def describe_user(self):
        prompt = f"{self.first_name} {self.last_name}"
        prompt += f" ({self.gender}) is {self.age} years old"
        print(f"{prompt} and lives in {self.city}.")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome to our program!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

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

admin = Admin("Keith", "Moua", 26, "Male", "Cincinnati")
admin.describe_user()

admin.privileges.privileges = ["add posts", "delete posts", "ban users", "warn users"]
admin.privileges.show_privileges()