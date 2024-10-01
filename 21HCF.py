def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"HCF: {num1}, {num2} = {HCF(num1, num2)}")

def HCF(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

main()