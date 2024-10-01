def main():
    user_input = input("Enter something: ")
    if user_input.isdigit():
        print("It's an integer!")
    else:
        print("It's not an integer!")

main()