import sys
x = input("a: ")
y = input("b: ")

def chek(a, b):
    if type(a) !=int or type(b) != int:
        return("str")
    else:
        if int(a) > int(b):
            return(">")
        elif int(a) < int(b):
            return("<")
        else:
            return("=")
print(chek(x, y))
