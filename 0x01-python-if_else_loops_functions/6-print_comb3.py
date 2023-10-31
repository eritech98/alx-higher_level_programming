#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if a != b and a < b:
            print("{}{}".format(a, b), end="")
            if a != 8:
                print(", ", end="")
print()
