# 10-5. Guest Book: Write a while loop that prompts users
# for their name. Collect all the names that are entered,
# and then write these names to a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.

from pathlib import Path

users = []
path = Path(__file__).parent / 'Textfiles/guest_book.txt'

while True:
    message = "(Enter q to stop) "
    name = input(f"What is user{len(users)+1}'s name?\n{message}")

    if name == 'q':
        break
    else:
        users.append(name)
        print()
    
path.write_text("\n".join(users))