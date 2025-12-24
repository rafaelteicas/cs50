# In Python the integers are referred as "int"
x = 1
y = 2
z = x + y
print(z)

# You can use input and ask to user's value for x and y:
x = input("What's x? ")
y = input("What's y? ")

# But you can't do this: z = x + y because you will be concatenating the strings, like: z = "1" + "2" => "12".
# You first need to convert both to int.
z = int(x) + int(y)
print(z)

# You can convert directly on input passing the input function to int, that is a function too: int(input("What's x? "))
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# Numbers with decimal points like 3.14, are "float" type
x = float(input("What's x? ")) # if input is "2" x = 2.0
y = float(input("What's y? ")) # if input x is "3.4" and y is "4.2"
print(x + y) # the result will be 7.6

# You can use the "round" function to round to next integer
x = float(input("What's x? ")) # if input x is "3.4"
y = float(input("What's y? ")) # if input y is "4.2"
print(round(x + y)) # the result will be 8
print(f"{z:,}") # if z = 1000000 the output will be "1,000,000" using comma as thousands separator
print(f"{z:_}") # if z = 1000000 the output will be "1_000_000" using underscore as thousands separator

# You can round the number of digits of the float with "round" function, like: z = round(z, 2).
# If z before round is 0.6666666, the result will be 0.67
z = 0.666666666666
print(round(z, 2))

# Or we can use the f-string to set the number of digits:
print(f"{z:.4f}") # 0.6667