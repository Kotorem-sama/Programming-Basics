# 9-3. Users: Make a class called User. Create two attributes
# called first_name and last_name, and then create several
# other attributes that are typically stored in a user
# profile. Make a method called describe_user() that prints
# a summary of the user’s information. Make another method
# called greet_user() that prints a personalized greeting to
# the user.

class User:
    def __init__(self, first, last, age, gender, city):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.city = city
    
    def describe_user(self):
        prompt = f"{self.first_name} {self.last_name}"
        prompt += f" ({self.gender}) is {self.age} years old"
        print(f"{prompt} and lives in {self.city}.")

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome to our program!")

# Create several instances representing different users, and
# call both methods for each user.

user1 = User("Danny", "Wilson", 23, "Male", "Twello")
user2 = User("Charles", "Page", 59, "Male", "Amerongen")
user3 = User("Daniela", "Beyer", 63, "Female", "Amsterdam")

for user in [user1, user2, user3]:
    user.describe_user()
    user.greet_user()