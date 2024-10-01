def palindrome(u):
    if u_input == u_input[::-1]:
        print("Yes, the user input is Palindrome!")
    else:
        print("No, it's not a Palindrome!")

u_input = input("Enter input: ")
palindrome(u_input)