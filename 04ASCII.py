def main():
    char = input("Enter an alphabetic: ")
    if len(char) == 1:
        print(f"The ASCII value of {char} is {ord(char)}.")


main()