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