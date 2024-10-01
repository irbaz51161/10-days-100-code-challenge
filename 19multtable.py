def main():
    num = int(input("Enter for which table you want to print: "))
    till = int(input("Till when you want to print the table: "))
    mult(num, till)

def mult(n, t):
    ans = 1
    for i in range(1, t+1):
        ans = n * i
        print(f"{n} * {i} = {ans}")

main()