"""
“Comma Code
Say you have a list value like this:
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items
separated by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.”

Excerpt From
Automate the Boring Stuff with Python
Al Sweigart
This material may be protected by copyright.
"""


def comma_code(lst):
    if len(lst) == 0:
        return ""
    elif len(lst) == 1:
        return lst[0]
    else:
        return ", ".join(lst[:-1]) + " and " + lst[-1]


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))  # 'apples, bananas, tofu, and cats'
print(comma_code([]))  # ""
