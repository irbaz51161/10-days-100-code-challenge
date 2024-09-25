def main():
    choice = input("Enter choice (yes/no): ")
    while choice == "yes":
        x = int(input("Enter number: "))
        if x % 2 == 0:
            print(f"{x} is even.")
        else:
            print(f"{x} it's fasle.")
        choice = input("Enter choice (yes/no): ")

main()