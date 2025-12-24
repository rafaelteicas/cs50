def convert(input):
    if ":)" in input:
        input = input.replace(":)", "🙂")
    if ":(" in input:
        input = input.replace(":(", "🙁")
    return input

def main():
    value = input()
    print(convert(value))

main()
