# 8-4. Large Shirts: Modify the make_shirt() function so that
# shirts are large by default with a message that reads I
# love Python. Make a large shirt and a medium shirt with
# the default message, and a shirt of any size with a
# different message.

def make_shirt(size="L", text="I love Python"):
    print(f"This shirt's size is '{size}' and will be printed with the text '{text}'.")

make_shirt()
make_shirt("M")
make_shirt("XXL", "I dislike Python >:(")