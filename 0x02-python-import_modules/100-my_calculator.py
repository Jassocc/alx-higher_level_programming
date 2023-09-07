#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("Usage:", arg[0], "<a> <operator> <b>")
        exit(1)
    oper = arg[2]
    func = {"+": add, "-": sub, "*": mul, "/": div}
    if oper not in func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(arg[1])
    b = int(arg[3])
    print("{:d} {:s} {:d} = {:d}".format(a, oper, b, func[oper](a, b)))
