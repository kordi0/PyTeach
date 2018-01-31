import sys
k = input("Please input your tuple: ")
def double_tuple(value):
    return tuple([value[i:i+2] for i, item in enumerate(value) if i % 2 == 0])
print(double_tuple(k))
