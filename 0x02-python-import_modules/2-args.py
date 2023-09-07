#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    inp = sys.argv[1:]
    num_arg = len(inp)
    print("{:d} {:s}{:s}".format(num_arg, 'arguments' if num_arg != 1 else 'argument', "." if num_arg == 0 else ":"))
    for a, ar in enumerate(inp):
        print("{:d}: {:s}".format(a + 1, ar))
