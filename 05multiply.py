def main():
    a = float(input("Enter a float number 1: "))
    b = float(input("Enter a float number 2: "))
    c = float(input("Enter a float number 3: "))
    d = int(input("Enter integer 4: "))
    e = int(input("Enter integer 5: "))
    mult = a * b * c
    div = d / e
    print(f"{a} * {b} * {c} = {mult}")
    print(f"{d} / {e} = {div:.2f}")      #will still print float evem tho it was taken as integer in an input

main()