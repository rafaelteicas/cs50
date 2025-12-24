students = ["Hermione", "Harry", "Ron"]

print(students[0]) # You can use this syntax to access an item on list with his index, in this case will access the first "Hermione".

# You can print each student accessing each index.
print(students[0])
print(students[1])
print(students[2])

# Using a for loop to print each str in list, iterating the list.
for student in students:
    print(student)

# You can iterate the number of items in the list using the function "len" that will return the length of items at list, in this case is 3, and use it at "range" function:
for i in range(len(students)):
    print(i + 1, students[i]) # prints the location and student, using + 1 because it starts from zero.

# The for loop is creating a variable and assign each value in the range, you can use different kinds of data, like str and int.
# So it just follows the order of data that you pass as argument:
for i in [3, 5, 1, 9, 29381, -2]:
    print(i) # it will print by the position, so it will first print 3, then 5, then 1.

# Dictionaries (dict in Python) are something associated with something else, called key and value.

# Here the index are associated with they values, the first is student is Hermione who is from Gryffindor and so on until Draco that is from Slytherin. 
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# But they can be associated with dict, this is the syntax:
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# They locations are allowed to use the words as the index:
print(students["Hermione"]) # Should return Hermione's house, so it will print "Gryffindor".
print(students["Draco"]) # It will print Slytherin.

# The indexes also can be iterated in for loops:
for student in students:
    print(student) # It will print all the students, so it will print the keys.
    print(students[student]) # It will access the value associated with that key.

# But what if we have more data about the student, like them patronum, like the databases does.
# We will need to associate the house and the patronum with each student, so we will need use other data structure:
students = [
    {
        "name": "Hermione",
        "house": "Gryffindor",
        "patronus": "Otter"
    },
    {
        "name": "Harry",
        "house": "Gryffindor",
        "patronus": "Stag"
    },
    {
        "name": "Ron",
        "house": "Gryffindor",
        "patronus": "Jack Russell Terrier"
    },
    {
        "name": "Draco",
        "house": "Slytherin",
        "patronus": None # Him patronous was never seen in books or movies, there is other keyword called None, that means there'snt a value.
    }
]
# You see there is a list because there is a square bracket in the beginning and other at end.
# You see there is a dictionary in each item because there is a curly bracket at beginning and other at end.

# It will iterate each item by they indexes. 0, 1, 2...
for student in students:
    print(student["name"], student["home"],  student["patronus"]) # You can access the value in dictionary by the key.