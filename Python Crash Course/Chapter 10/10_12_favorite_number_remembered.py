# 10-12. Favorite Number Remembered: Combine the two programs
# you wrote in Exercise 10-11 into one file. If the number is
# already stored, report the favorite number to the user. If
# not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.

import json
from pathlib import Path

path = Path(__file__).parent / 'Textfiles/Jsonfiles/second_favorite.json'
try:
    favorite_number = json.loads(path.read_text())
    print(f"I know your favorite number! It's {favorite_number}.")
except:
    favorite_number = input("What is your favorite number? ")
    path.write_text(json.dumps(favorite_number))