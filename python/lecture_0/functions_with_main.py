# In Python we don't need a main function, but we can have:
def main():
    name = input("What's your name? ")
    # Without params
    hello()
    # Without format
    hello(name)
    # Format the string
    hello(name.strip().title())

# In that case we don't have to declare the function before
# The main function will be executed after
def hello(to="world"):
    print(f"Hello, {to}")

# Now we call the main function:
main()