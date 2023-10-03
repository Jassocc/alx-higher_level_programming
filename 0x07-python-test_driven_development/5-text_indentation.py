#!/usr/bin/python3
"""
module 5 text_indentation
prints a text with 2 new lines after chars
function:
    def text_indentation(text):
"""


def text_indentation(text):
    """
    prints a text with new lines after
    specified chars: . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars_split = ['.', '?', ':']
    li = []
    line = ''
    for char in text:
        line += char
        if char in chars_split:
            li.append(line.strip())
            line = ''
    if line:
        li.append(line.strip())
    if not text.endswith(tuple(chars_split)):
        print("\n\n".join(li), end="")
    else:
        print("\n\n".join(li))
