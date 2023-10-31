#!/usr/bin/python3
def fizzbuzz():
    """Prints the numbers from 1 to 100, \
            prints Fizz for mutiples of 3, \
            prints Buzz for mutliples of 5 and \
            FizzBuzz for mutiples of both 3 and 5."""
    for i in range(1, 101):
        mod3_e = i % 3
        mod5_e = i % 5
        if mod3_e == 0 and mod5_e == 0:
            print("FizzBuzz", end=" ")
        elif mod3_e == 0:
            print("Fizz", end=" ")
        elif mod5_e == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")i
