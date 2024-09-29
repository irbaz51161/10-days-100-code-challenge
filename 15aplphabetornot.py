def main():
    alphabet = input("Enter an alphabet: ")
    checker(alphabet)

def checker(a):
    if len(a) == 1:
        if a.isalpha():
            print(f"{a} is an alphabet.")
        else:
            print(f"{a} is not an alphabet.")

main()


# OR WE CAN ALSO CHECK BY USING ASCII RANGE