import sys
x = input("a: ")
y = input("b: ")

def chek(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return("str")
    else:
        if int(a) > int(b):
            return(">")
        elif int(a) < int(b):
            return("<")
        else:
            return("=")
print(chek(x, y))
