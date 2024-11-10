# 10-4. Guest: Write a program that prompts the user for
# their name. When they respond, write their name to a
# file called guest.txt.

from pathlib import Path

path = Path(__file__).parent / 'Textfiles/guest.txt'

name = input("What is your name? ")
path.write_text(name)