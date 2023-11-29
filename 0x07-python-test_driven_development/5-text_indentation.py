#!/usr/bin/python3

"""
Text indentation module.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text - the string to be printed.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    for k, i in enumerate(text):
        if i == " " and (text[k - 1] == "." or
                         text[k - 1] == "?" or text[k - 1] == ":"):
            string.replace(i, "")
            continue
        string += i
        if i == "." or i == "?" or i == ":":
            string += "\n\n"
            continue

    print(string, end="")
