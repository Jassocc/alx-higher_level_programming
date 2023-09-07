#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    inp = sys.argv[1:]
    num_ar = len(inp)
    print("{:d} {:s}{:s}".format(num_ar, 'arguments' if num_ar != 1
                                 else 'argument', "." if num_ar == 0 else ":"))
    for a, ar in enumerate(inp):
        print("{:d}: {:s}".format(a + 1, ar))
