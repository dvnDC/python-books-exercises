"""
“Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters will be removed
from the beginning and end of the string.
Otherwise, the characters specified in the second argument to the function will be removed from the string.”

Excerpt From
Automate the Boring Stuff with Python
Al Sweigart
This material may be protected by copyright.
"""

import re


def my_strip(string, chars=None):
    if chars is None:
        return re.sub(r'^\s+|\s+$', '', string)
    else:
        return re.sub(f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$', '', string)


print(my_strip("   Hello, World!   "))  # "Hello, World!"
print(my_strip("   Hello,     World!   "))  # "Hello,     World!"
print(my_strip("--Hello, World!--", "-"))  # "Hello, World!"
