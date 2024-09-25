def main():
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    temp = a
    a = b
    b = temp
    print(f"Now value 1 is {a} and value 2 is {b}.")

main()