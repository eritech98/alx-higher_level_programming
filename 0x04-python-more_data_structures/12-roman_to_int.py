#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""
    num = 0
    if type(roman_string) is not str or roman_string is None:
        return 0

    for i in roman_string:
        if roman_string.startswith('M'):
            num += 1000
            roman_string = roman_string[1:]
        elif roman_string.startswith('CM'):
            num += 900
            roman_string = roman_string[2:]
        elif roman_string.startswith('D'):
            num += 500
            roman_string = roman_string[1:]
        elif roman_string.startswith('CD'):
            num += 400
            roman_string = roman_string[2:]
        elif roman_string.startswith('C'):
            num += 100
            roman_string = roman_string[1:]
        elif roman_string.startswith('XC'):
            num += 90
            roman_string = roman_string[2:]
        elif roman_string.startswith('L'):
            num += 50
            roman_string = roman_string[1:]
        elif roman_string.startswith('XL'):
            num += 40
            roman_string = roman_string[2:]
        elif roman_string.startswith('X'):
            num += 10
            roman_string = roman_string[1:]
        elif roman_string.startswith('IX'):
            num += 9
            roman_string = roman_string[2:]
        elif roman_string.startswith('V'):
            num += 5
            roman_string = roman_string[1:]
        elif roman_string.startswith('IV'):
            num += 4
            roman_string = roman_string[2:]
        elif roman_string.startswith('I'):
            num += 1
            roman_string = roman_string[1:]

    return num
