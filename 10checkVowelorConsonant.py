def main():
    choice = input("Enter choice (yes/no): ")
    while choice == "yes":
        y = input("Enter alphabet: ").lower()
        match y:
            case "a" | "e" | "i" | "o" | "u":
                print(f"{y} is even.")
            case _:
                print(f"{y} is odd.")
        choice = input("Enter choice (yes/no): ")

main()