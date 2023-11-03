#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x_ = 1
    n_ = len(sys.argv)
    if len(sys.argv) == 1:
        print("{:d} arguments.".format(0))
    else:
        if n_ == 2:
            print("{:d} argument:".format(n_ - 1))
        else:
            print("{:d} arguments:".format(n_ - 1))
        while x_ < n_:
            print("{:d}: {}".format(x_, sys.argv[x_]))
            x_ += 1
