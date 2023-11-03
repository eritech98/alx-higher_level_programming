#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
