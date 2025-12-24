def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            # break # You can use break to get out of loop.
            return n # But you can return directly the "n" to get out of loop.
        # return n # You have to return if you just get out with break.

def meow(n):
    for _ in range(n):
        print("meow")

main()