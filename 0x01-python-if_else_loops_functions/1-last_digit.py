#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod_e = number % 10
if number < 0:
    mod_e = number % -10
print("Last digit of", end=" ")
if mod_e > 5:
    print(f"{number} is {mod_e} and is greater than 5")
elif mod_e == 0:
    print(f"{number} is {mod_e} and is 0")
else:
    print(f"{number} is {mod_e} and is less than 6 and not 0")
