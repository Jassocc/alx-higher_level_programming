#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    re = add(a, b)
    res = sub(a, b)
    resu = mul(a, b)
    result = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, re))
    print("{:d} - {:d} = {:d}".format(a, b, res))
    print("{:d} * {:d} = {:d}".format(a, b, resu))
    print("{:d} / {:d} = {:d}".format(a, b, result))
