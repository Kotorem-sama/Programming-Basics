# 9-4. Number Served: Start with your program from
# Exercise 9-1 (page 162). Add an attribute called
# number_served with a default value of 0. Create an instance
# called restaurant from this class. Print the number of
# customers the restaurant has served, and then change this
# value and print it again.

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

restaurant = Restaurant("Hudson", "American")
print(restaurant.number_served)

restaurant.number_served += 23
print(restaurant.number_served)
print()

# 1) Add a method called set_number_served() that lets you set
# the number of customers that have been served. Call this
# method with a new number and print the value again.

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

restaurant = Restaurant("Hudson", "American")
print(restaurant.number_served)

restaurant.set_number_served(92)
print(restaurant.number_served)
print()

# 2) Add a method called increment_number_served() that lets
# you increment the number of customers who’ve been served.
# Call this method with any number you like that could
# represent how many customers were served in, say, a day of
# business.

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

restaurant = Restaurant("Hudson", "American")
for hour in range(0, 12):
    restaurant.increment_number_served(23)
print(restaurant.number_served)