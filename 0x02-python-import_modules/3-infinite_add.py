#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    total = 0
    for ar in arg:
        total = total + int(ar)
    print(total)
