#LCM FORMULA = (A * B) / HCF(A, B)

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    hcf_value = HCF(num1, num2)
    lcm_value = LCM(num1, num2, hcf_value)  
    print(f"LCM({num1}, {num2}) = {lcm_value}")

def HCF(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def LCM(n1_1, n2_2, h):
    ans = (n1_1 * n2_2) // h
    return ans


main()