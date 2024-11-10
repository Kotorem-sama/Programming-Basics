# 10-3. Simpler Code: The program file_reader.py in this
# section uses a temporary variable, lines, to show how
# splitlines() works. You can skip the temporary variable
# and loop directly over the list that splitlines() returns:
# for line in contents.splitlines():
# Remove the temporary variable from each of the programs in
# this section, to make them more concise.


# 10.1

from pathlib import Path

path = Path(__file__).parent / 'Textfiles/learning_python.txt'
content = path.read_text()
print(content + "\n")
print(content + "\n")

for line in content.splitlines():
    print(line)
print()


# 10.2

from pathlib import Path

path = Path(__file__).parent / 'Textfiles/learning_python.txt'
content = path.read_text().replace("Python", "C")

for line in content.splitlines():
    print(line)