import sys
integer = sys.getsizeof(int())
float = sys.getsizeof(float())
list = sys.getsizeof(list())
bool = sys.getsizeof(bool())

print(f"size of integer is {integer} bytes.")
print(f"size of float is {float} bytes.")
print(f"size of list is {list} bytes.")
print(f"size of bool is {bool} bytes.")