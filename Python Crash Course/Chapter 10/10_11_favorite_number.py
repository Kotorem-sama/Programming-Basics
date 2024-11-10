# 10-11. Favorite Number: Write a program that prompts for
# the user’s favorite number. Use json.dumps() to store this
# number in a file. Write a separate program that reads in
# this value and prints the message “I know your favorite
# number! It’s _____.”

import json
from pathlib import Path

def save_favorite_number():
    favorite_number = input("What is your favorite number? ")

    path = Path(__file__).parent / 'Textfiles/Jsonfiles/favorite.json'
    path.write_text(json.dumps(favorite_number))

def load_favorite_number():
    path = Path(__file__).parent / 'Textfiles/Jsonfiles/favorite.json'
    favorite_number = json.loads(path.read_text())

    print(f"I know your favorite number! It's {favorite_number}.")

load_favorite_number()