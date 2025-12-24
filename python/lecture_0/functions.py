# Functions in Python are declared by the keyword "def"
# We going to create a function to print the hello getting the input:
def hello(to = "world"):
    print(f"Hello, {to.strip().title()}")

name = input("What's your name? ")

hello(name)

# We pass the default value "world" to the function:
hello()