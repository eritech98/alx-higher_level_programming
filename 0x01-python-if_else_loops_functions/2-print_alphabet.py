#!/usr/bin/python3
for letter_e in range(97, 123):
    if letter_e == 101 or letter_e == 113:
        continue
print("{}".format(chr(letter_e)), end="")
