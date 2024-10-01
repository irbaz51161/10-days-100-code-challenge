def main():
    for i in range(ord('a'), ord('z')+1):
        print(f"({chr(i)} {chr(i).upper()})",end="")
    print("\n")

main()