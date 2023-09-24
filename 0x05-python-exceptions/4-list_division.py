#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listing = []
    for a in range(list_length):
        division = 0
        try:
            division = my_list_1[a] / my_list_2[a]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            listing.append(division)
    return listing
