rangee = int(input("Enter the range: "))
list_prime = []
for i in range(2, rangee + 1):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        list_prime.append(i)

print(f"Prime number series = {list_prime}")