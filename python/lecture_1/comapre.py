# The ifs statements will control the flow of the program.

# First, the user types the values of x and y, the input function will get the value and the int function will convert the value into a integer.
x = int(input("What's x? "))
y = int(input("What's y? "))

# We have three options in this case, that are expressed below.
# When a conditional is true, the following line is executed and the print function is executed.
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
# The code above is correct, it will return the correct answer, but is bad designed, because it pass by each if statement, even when one of than is true.

# We have other conditional statement in Python with the keyword elif, that is the conjunction of else if in english.
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
# The performance will be better than the first one, because the program will stop when the condition is true.
# But if the x is equal to y we have to pass by the three conditionals, anyway.
# To have a better performance in that case we have to be lucky to be in the first or second case.

# In Python we also have a third conditional keyword, the 'else':
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# In Python we have the 'or' keyword:
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
# In the case above we can simplify with only one question:
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
# So the program only have two options, or x is equal y or not.

# We can do the reverse, asking if x is not equal to y:
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")