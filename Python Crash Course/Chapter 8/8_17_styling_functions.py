# 8-17. Styling Functions: Choose any three programs you wrote
# for this chapter, and make sure they follow the styling
# guidelines described in this section.

def make_shirt(size="L", text="I love Python"):
    print_statement = f"This shirt's size is '{size}' and will"
    print(f"{print_statement} be printed with the text '{text}'.")

make_shirt()
make_shirt("M")
make_shirt("XXL", "I dislike Python >:(")