# In this file we will see how to use loops in Python.
# A loop is a programming structure that repeats a sequence of instructions until a specific condition is met.

# For example, if we want to print "meow" 3 times on console, we could do it like this:
print("meow")
print("meow")
print("meow")

# In Python we have "while" as conditional loop, it will test the conditional and execute the line of code every time the conditional isn't truthy.
i = 3
# Every time "i" is different to 0 it will print "meow" on console.
while i != 0:
    print("meow")
    # If we execute until here it will print "meow" infinitely, because the "i" always is different to 0.
    # So we have to update the "i" value to stop the loop:
    i = i - 1
    # When it executes first time, the "i" value is 3, so the "while" continual it'll be truthy.
    # On the last line it will decrease the "i" value by 1, so the second time the "i" will be 2, and will repeat until "i" equal 0. So the program will stop.

# Is the same thing above but "i" value starts from 1 and it will be increased each execution of loop.
i = 0
while i < 3:
    print("meow")
    # First time it will be 1, so it will be i = 1 + 1. Second time it will be i = 2 + 1...
    # When the i is updated to 3 the "while" conditional isn't executed. 
    i = i + 1

# For is other loop keyword, you can simplify the variable initialization, in this case i starts with the value 0, and will assume each value in the list.
for i in [0, 1, 2]:
    print("meow")

# Instead of write manually each value you can use a function called "range", and will starts from zero until the number passed in param:
for i in range(3):
    print("meow")

print("meow\n" * 3, end = "")

# Create a infinite loop and use the keywords "continue" and "break" to control the flow of loop.
while True:
    n = int(input("What's n? "))
    # if n < 0:
    #     continue
    # else:
    #     break
    if n > 0:
        break

for _ in range(n):
    print("meow")