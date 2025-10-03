#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    """Return first five chars of the string argument."""
    s = str(s)
    return s[:5]

def last_seven(s):
    """Return last seven chars of the string argument."""
    s = str(s)
    return s[-7:]

def middle_number(n):
    """
    Accept an int (per lab) but we’ll stringify to slice.
    Return the 2nd and 3rd characters as a string.
    Examples: 1500 -> '50', 1.50 -> '.5' (matches sample).
    """
    s = str(n)
    # guard for short strings
    return s[1:3]

def first_three_last_three(a, b):
    """
    Return first three chars of a + last three chars of b.
    """
    a = str(a)
    b = str(b)
    return a[:3] + b[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
