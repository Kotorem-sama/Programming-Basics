# 9-7. Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User
# class you wrote in Exercise 9-3 (page 162) or Exercise 9-5
# (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban
# user", and so on. Write a method called show_privileges()
# that lists the administrator’s set of privileges. Create an
# instance of Admin, and call your method.

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
        self.privileges = []
    
    def show_privileges(self):
        privileges = ", ".join(self.privileges)
        print(f"The admin has the privileges to: {privileges}")

admin = Admin("Keith", "Moua", 26, "Male", "Cincinnati")
admin.describe_user()

admin.privileges = ["add posts", "delete posts", "ban users", "warn users"]
admin.show_privileges()