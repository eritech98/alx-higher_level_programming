#!/usr/bin/python3

def list_division(l1, l2, len):
    """Divides element by element 2 lists."""
    my_list = []
    for x in range(len):
        try:
            my_list.append(l1[x] / l2[x])
        except ZeroDivisionError:
            print("division by 0")
            my_list.append(0)
            continue
        except IndexError:
            print("out of range")
            my_list.append(0)
            continue
        except TypeError:
            print("wrong type")
            my_list.append(0)
            continue
        finally:
            continue
    return my_list
