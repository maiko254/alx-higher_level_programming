#!/usr/bin/python3
""" Print newline after certain characters """


def text_indentation(text):
    """ Print 2 newlines after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    break_characters = ['.', '?', ':']

    current_line = ""

    for char in text:
        current_line += char

        if char in break_characters:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
