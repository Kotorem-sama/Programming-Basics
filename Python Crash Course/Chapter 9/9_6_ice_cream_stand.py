# 9-6. Ice Cream Stand: An ice cream stand is a specific
# kind of restaurant. Write a class called IceCreamStand that
# inherits from the Restaurant class you wrote in Exercise
# 9-1 (page 162) or Exercise 9-4 (page 166). Either version
# of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice
# cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        prompt = f"Restaurant name: {self.restaurant_name}"
        print(f"{prompt}\tCuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self, amount):
        self.number_served = amount

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, name):
        super().__init__(name, "Ice Cream")
        self.flavors = []

    def show_flavors(self):
        flavors = ", ".join(self.flavors)
        print(f"The flavors you can choose from are: {flavors}.")

stand = IceCreamStand("Alex Ice Cream Stand")
stand.flavors = ["Vanilla", "Pistacio", "Strawberry"]

stand.describe_restaurant()
stand.show_flavors()