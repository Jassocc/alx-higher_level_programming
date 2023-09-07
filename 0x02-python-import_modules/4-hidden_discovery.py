#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    sorted_name = (dir(hidden_4))
    for name in sorted_name:
        if not name.startswith("__"):
            print("{:s}".format(name))
