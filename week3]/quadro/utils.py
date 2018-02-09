def get_parameter(name):
    while True:
        p = input("Enter the parameter of the equation: %s = " % name)
        if p.replace('.', '').isdigit() and float(p) != 0:
            p = float(p)
            return p
        else:
            print("Please enter the number of non-zero!")

def get_descr(a, b, c):
    d = b ** 2 - 4 * a * c
    return d
           
