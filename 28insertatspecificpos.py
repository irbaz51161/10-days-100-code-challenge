def main():
    inp = input("Enter input: ")
    inp2 = input("Enter what you want to insert in the middle of the string: ")
    position = int(input("At what position you want to enter the input 2: "))
    result = edit(inp, inp2, position)
    print(f"User input was :{inp} and now {result}")


def edit(i1, i2, pos):
    return i1[:pos] + i2 + i1[pos:]
    

main()