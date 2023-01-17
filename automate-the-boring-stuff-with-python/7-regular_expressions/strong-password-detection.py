"""
“Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and
 lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.”

Excerpt From
Automate the Boring Stuff with Python
Al Sweigart
This material may be protected by copyright.
"""

import re


def is_strong_password(password):
    strong_password_regex = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
    if re.fullmatch(strong_password_regex, password):
        return True
    return False


print(is_strong_password("Ab1"))  # False
print(is_strong_password("Ab1#Ab1#Ab1#"))  # True
print(is_strong_password("RazDwaTrzy123"))  # False
print(is_strong_password("RazDwaTrzy123!"))  # True
