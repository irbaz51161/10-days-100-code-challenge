def main():
    rangee = int(input("Enter till you want to sum all the natural numbers: "))
    count = 0
    func(rangee, count)

def func(r, c):
    for i in range(1,r+1):
        c += i
    print(f"The total sum of natural numbers from 1 to {r} is \"{c}\".")

main()