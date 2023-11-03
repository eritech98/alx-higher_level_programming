#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for e in dir(hidden_4):
        if e[0] == "_":
            continue
        print(e)
