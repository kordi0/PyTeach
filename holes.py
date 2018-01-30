import sys
n = input("Enter your Number: ")
def count_holes(value):
    l = 0
    if type(value) == float:
        return 'error'
    else:
        for i in str(value):
            if i == '6' or i == '4' or i == '9' or i == '0':
                l += 1
            elif i == '8':
                l += 2
    return(l)
print(count_holes(n))
