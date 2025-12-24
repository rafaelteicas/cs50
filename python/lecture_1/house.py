name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# The code above is redundant, you check if Harry, Hermione or Ron are from Gryffindor
# We can group then to simplify:
if name == "Harry" or name == "Hermione" or  name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# The keyword "match" has the same idea, is the same of "switch" from other languages
# The "match" function will test each "case" and execute when the conditional is true
match(name):
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# We can group to test to Gryffindor in the same line, like we did before:
match(name):
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# In comparison with other languages, in Python you don't need to use the word "break" to stop the flow and you don't have the keyword "default", but the "case _:" to set the default behavior