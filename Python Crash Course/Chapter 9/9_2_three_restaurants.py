# 9-2. Three Restaurants: Start with your class from
# Exercise 9-1. Create three different instances from the
# class, and call describe_restaurant() for each instance.

class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        prompt = f"Restaurant name: {self.restaurant_name}"
        print(f"{prompt}\tCuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant1 = Restaurant("Happy Italy", "Italian")
restaurant2 = Restaurant("Wokamor", "Asian")
restaurant3 = Restaurant("Hudson\t", "American")

for restaurant in [restaurant1, restaurant2, restaurant3]:
    restaurant.describe_restaurant()