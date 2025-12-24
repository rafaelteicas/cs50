score = int(input("Score: "))

# In Python we have the keyword and to test more than one conditional:
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grande: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# In Python you can group the ranges:
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grande: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# We can organize the program above without use the ranges:
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grande: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# If we don't use elif we can have more than one conditional true, so it will print more than one result
# If we have a 95 to score all the conditionals are truthy
if score >= 90:
    print("Grade: A")
if score >= 80:
    print("Grade: B")
if score >= 70:
    print("Grande: C")
if score >= 60:
    print("Grade: D")
# So, it will print on console:
# Grade: A
# Grade: B
# Grande: C
# Grade: D

