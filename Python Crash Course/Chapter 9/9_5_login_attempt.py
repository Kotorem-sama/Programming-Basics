# 9-5. Login Attempts: Add an attribute called login_attempts
# to your User class from Exercise 9-3 (page 162). Write a
# method called increment_login_attempts() that increments
# the value of login_attempts by 1. Write another method
# called reset_login_attempts() that resets the value of
# login_attempts to 0.

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

# Make an instance of the User class and call
# increment_login_attempts() several times. Print the value
# of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts
# again to make sure it was reset to 0.

user = User("Danny", "Wilson", 23, "Male", "Twello")
for attempts in range(0, 12):
    user.increment_login_attempts()
    user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)