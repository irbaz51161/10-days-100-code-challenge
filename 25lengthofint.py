def main():
    n = (input("Enter number for method 1: "))
    method_1(n)
    n2 = int(input("Enter number for method 2: "))
    m2 = method_2(n2)
    print(f"The length of {n2} is {m2}.")

def method_1(num):
    if num.isdigit():
        print(f"The length of user input integer is: {len(num)}.")
    else:
        print(f"The user input is not integer but still the length is: {len(num)}.")

def method_2(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count

main()