def main():
    result = square(int(input("What's the value? ")))
    print(result)
def square(n):
    # We could do with: return n ** 2 or return n * n
    return pow(n, 2)
main()