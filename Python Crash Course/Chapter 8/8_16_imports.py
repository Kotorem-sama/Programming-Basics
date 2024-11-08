# 8-16. Imports: Using a program you wrote that has one
# function in it, store that function in a separate file.
# Import the function into your main program file, and call
# the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import imports
import imports as i
from imports import show_messages as sm
from imports import show_messages
from imports import *

# Import #1
sent_messages = []
short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
imports.send_messages(short_messages, sent_messages)
print(f"To-be sent list: {short_messages}\nSent list: {sent_messages}")
print()

# Import #2
sent_messages = []
short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
i.send_messages(short_messages, sent_messages)
print(f"To-be sent list: {short_messages}\nSent list: {sent_messages}")
print()

# Import #3
short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
sm(short_messages)
print()

# Import #4
short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
show_messages(short_messages)
print()

# Import #5
sent_messages = []
short_messages = [ "Run!", "Hide!", "Duck!", "Jump!" ]
send_messages(short_messages, sent_messages)
print(f"To-be sent list: {short_messages}\nSent list: {sent_messages}")
print()