#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    e = 1
    while e < len(sys.argv):
        sum += int(sys.argv[e])
        e += 1
    print(sum)
