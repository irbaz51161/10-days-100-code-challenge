def main():
    option = input("Do you want to check? (yes/no): ")
    while option == "yes":
        a = input("Enter an alphabet: ")
        check(a)
        option = input("Do you want to check? (yes/no): ")

def check(alpha):
    if len(alpha) == 1:
        if alpha == alpha.lower():
            print(f"{alpha} is in lower case.")
        else:
            print(f"{alpha} is in upper case.")

main()