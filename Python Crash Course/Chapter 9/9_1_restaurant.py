# 9-1. Restaurant: Make a class called Restaurant. The
# __init__() method for Restaurant should store two
# attributes: a restaurant_name and a cuisine_type. Make
# a method called describe_restaurant() that prints these two
# pieces of information, and a method called open_restaurant()
# that prints a message indicating that the restaurant is
# open.

class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        prompt = f"Restaurant name: {self.restaurant_name}"
        print(f"{prompt}\tCuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

# Make an instance called restaurant from your class. Print
# the two attributes individually, and then call both methods.

restaurant = Restaurant("Mcdonalds", "Fastfood")
restaurant.describe_restaurant()
restaurant.open_restaurant()