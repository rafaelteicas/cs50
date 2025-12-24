# In Python you can use '#' to write comments
"""
And multi-line comments with triple quotes
"""

# You can use comments to create a to-do list, or explain your code, or do pseudo-code planning, like this:
# Greet the user
print("Hello, world!")

# Ask for their name
name = input("What is your name? ") # name is a variable that stores user input

print(f"Without format the string {name}")

name = name.strip() # remove the space before and after string like: "     rafael     " => "rafael"
name = name.title() # capitalize the first letter of each word "rafael castro" => "Rafael Castro"
# you can write name = name.strip().title() or even directly on declaration name = input("What is your name? ").strip().title()

# Print a personalized greeting
print(f"Hello, {name}!") # f-strings for formatting
print("Hello,", end=" ")  # end="" changes the end character from newline to space, the default is end='\n' that adds a new line
print(name + "!")  # Concatenation with +

# Different ways to format the output
print("Hello, " + name + "!")
print("Hello, ", name, "!", sep="") # sep="" removes spaces, you can customize it

# Demonstrating escape characters
print("He said, \"Hello!\"")  # Using backslash to escape double quotes
print('It\'s a beautiful day!')  # Using backslash to escape single quote
print('He said, "Hello!"')  # Using single quotes for string and double inside the string.