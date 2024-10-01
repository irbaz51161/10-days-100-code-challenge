def main():
    num = int(input("Enter the number: "))
    result = armstrong(num)
    check(result, num)

def armstrong(n):
    str_n = str(n)
    calculation_1 = 0
    for i in str_n:
        calculation_1 += int(i) ** len(str_n)
    return calculation_1

def check(r, n):
    if r == n:
        print(f"Yes! {n} is an ARMSTRONG!")
    else:
        print(f"No! {n} not an ARMSTRONG!")

main()