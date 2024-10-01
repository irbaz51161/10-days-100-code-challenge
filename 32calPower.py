def main():
    option = input("Enter the option: (Yes / No) ").capitalize()
    while option == "Yes":
        base = int(input("Base: "))
        power = int(input("Power: "))
        print(f"{base} base to the power {power} is {pow(base, power)}.")
        option = input("Enter the option again: (Yes / No) ").capitalize()

main()