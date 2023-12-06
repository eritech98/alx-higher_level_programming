#!/usr/bin/python3

"""
A script that reads stdin line by line and computes metrics.
"""

if __name__ == "__main__":
    n = 0
    size = 0
    status = []
    try:
        while True:
            stdin = input()
            lis = stdin.split()
            n += 1
            size += int(lis[-1])
            status.append(lis[-2])
            status = [i for i in status if i]
            if n % 10 == 0:
                print(f"File size: {size}")
                for i in sorted(set(status)):
                    print(f"{i}: {status.count(i)}")
    except KeyboardInterrupt:
        print(f"File size: {size}")
        for i in sorted(set(status)):
            print(f"{i}: {status.count(i)}")
