def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    greater(num1, num2, num3)
    

def greater(a, b, c):
    if a > b and a > c:
        print(f"{a} is greater then {b} and {c}.")
    elif b > a and b > c:
        print(f"{b} is greater then {a} and {c}.")
    else:
        print(f"{c} is greater then {a} and {b}")


main()