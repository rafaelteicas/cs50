# x = int(input("What's x? ")) # The int function receives the input function's return value and convert into a integer.
# print(f"x is {x}") # Everything goes fine if the user types a value that can be converted wih the int function
# but if the user pass other type of data? A value that cannot be converted to integer, like a string?
# If he input is "cat" it will throw:
# ValueError: invalid literal for int() with base 10: 'cat'
# In this case we have to handle this error, assuming the user isn't paying attention or he is a malicious user.
# The Python we have the try statement who have a keyword called "try" and "except":

# try do something
try:
    x = int(input("What's x? ")) # try convert the input into a integer and pass to x variable
    # print(f"x is {x}") 
# except something goes wrong
except ValueError:
    print("x is not an integer") # except it throws a ValueError, so it will execute this line and print
# But in this case we have to preview that can be a ValueError, we can catch errors in general, but isn't a good practice, because it can hide other bugs or things that you need to fix.
# print(f"x is {x}") # If you try to print the x outside of try block it will throws a NameError, because the int function is throwing.
# To solve this problem we can use the else keyword:
else:
    print(f"x is {x}")
# OBS: in other languages we can have the scope problem but in Python we can declare the variable inside the block and use outside.

# We can use loops to ask the x value until the user types correctly:
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not a number")
    else:
        break # Break out of loop.
print(f"x is {x}") # This line is only executed when everything is fine.

# We can do this way:
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not a number")

def get_int(prompt):
    while True:
        try:
        return int(input(prompt)) # we can also return directly here.
    except ValueError:
        pass # the keyword "pass" ignores when the try throws an error.
    else:
        # break
        # return x # returns value and break out the loop.
    # return x # we need to return the value back inside a function.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

main()