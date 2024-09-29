import math
def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    print(f"Your quadratic epuation looks like: {a}x^2 + {b}x + {c}")
    quad(a, b, c)
    

def quad(x, y, z):
    sqrtt = math.sqrt(y ** 2 - 4 * x * z)
    if sqrtt >= 0 and x != 0:
        alpha = (-y+sqrtt)/2*x
        beta = (-y-sqrtt)/2*x
        print(f"Roots are: {alpha} and {beta}")
    else:
        print("Invalid input!")


main()
