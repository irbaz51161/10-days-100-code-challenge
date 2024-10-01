def main():
    num = int(input("Enter number: "))
    print(f"The series of Fibonacci is: {fibonacci_func(num)}")

def  fibonacci_func(n):
    fib_seq = [0,1]
    for i in range(2, n):
        next_value = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(next_value)
    return fib_seq


main()