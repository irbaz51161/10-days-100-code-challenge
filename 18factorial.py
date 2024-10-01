def main():
    option = input("Enter your choice (yes/no): ")
    while option == "yes":
        num = int(input("Enter number for which you want to find factorial: "))
        mult = 1
        factorial(num, mult)
        option = input("Enter your choice again (yes/no): ")

def factorial(n, m):
    for i in range(1, n+1):
        m *= i
    print(f"Factorial: {n}! = {m}")

main()