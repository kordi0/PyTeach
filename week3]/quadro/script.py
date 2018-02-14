from utils import get_parameter, QadraticEquation
def main():
    a = get_parameter('a')
    b = get_parameter('b')
    c = get_parameter('c')

    qe = QadraticEquation(a, b, c)
    d = qe.get_descr()
    print(qe.res(d))

if __name__ == "__main__":
    main()
