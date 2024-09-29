def main():
    num = float(input("Enter number: "))
    if num >= 0:
        print(f"{num} is a positive integer.")
    elif num < 0:
        print(f"{num} is a negative integer.")
    else:
        print(f"{num} is either positive or negative.")

main()