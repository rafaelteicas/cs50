x = int(input("What's x? "))

# "%" is called modular operator, the result is the rest of division
# If x = 2, x % 2 = 0, so it's even. If x = 3, x % 3 = 1.5, so it's odd
if x % 2 == 0:
    print("It's even")
else:
    print("It's odd")

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# Python has the boolean value, that can be True or False
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# You can condense the conditional in only one line
# def is_even(n):
#     return True if n % 2 == 0 else False

# But the expression already is a boolean value, you can just return the result of expression:
def is_even(n):
    return n % 2 == 0

main()