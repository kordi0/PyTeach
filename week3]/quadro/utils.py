def get_parameter(name):
    while True:
        p = input("Enter the parameter of the equation: %s = " % name)
        if p.replace('.', '').isdigit() and float(p) != 0:
            p = float(p)
            return p
        else:
            print("Please enter the number of non-zero!")

class QadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_descr(self):
        d = self.b ** 2 - 4 * self.a * self.c
        return d

    def res(self, d):
        self.d = d
        if d < 0:
            return("No results!")
        else:
            x1 = (-self.b + self.d **(1/2.0)) / 2 * self.a
            x2 = (-self.b - self.d **(1/2.0)) / 2 * self.a
            return("Results: x1 = %s, x2 = %s" % (x1, x2))
