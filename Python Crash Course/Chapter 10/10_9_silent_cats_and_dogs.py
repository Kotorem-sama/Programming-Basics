# 10-9. Silent Cats and Dogs: Modify your except block in
# Exercise 10-8 to fail silently if either file is missing.

from pathlib import Path

filenames = [ 'cats.txt', 'dogs.txt' ]

for filename in filenames:
    try:
        path = Path(__file__).parent / f'Textfiles/{filename}'
        content = ", ".join(path.read_text().splitlines())
        print(f"Names for {path.stem}: {content}.")
    except FileNotFoundError:
        pass