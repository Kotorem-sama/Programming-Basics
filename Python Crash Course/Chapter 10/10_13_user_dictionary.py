# 10-13. User Dictionary: The remember_me.py example only
# stores one piece of information, the username. Expand this
# example by asking for two more pieces of information about
# the user, then store all the information you collect in a
# dictionary. Write this dictionary to a file using
# json.dumps(), and read it back in using json.loads(). Print
# a summary showing exactly what your program remembers about
# the user.

from pathlib import Path
import json


def get_stored_information(path):
    """Get stored information if available."""
    if path.exists():
        contents = path.read_text()
        information:dict = json.loads(contents)
        return information
    else:
        return None

def get_new_information(path):
    """Prompt for a new username, e-mail and country."""
    username = input("What is your username? ")
    email = input("What is your e-mail? ")
    country = input("What country are you from? ")
    information = { 'username':username, 'e-mail':email, 'country':country }

    contents = json.dumps(information)
    path.write_text(contents)
    return information

def greet_user():
    """Greet the user by name."""
    path = Path(__file__).parent / 'Textfiles/Jsonfiles/username.json'
    information = get_stored_information(path)
    if information:
        username = information['username']
        email = information['e-mail']
        country = information['country']
        print(f"Welcome back, {username}({email}) from {country}!")
    else:
        information = get_new_information(path)
        print(f"This is what we'll remember when you come back:")
        for key, value in information.items():
            print(f"{key.upper()}: {value}")

greet_user()