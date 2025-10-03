#!/usr/bin/env python3
# Author ID: [seneca_id]

def is_digits(sobj):
    """
    Return True iff EVERY character in sobj is a digit 0-9.
    No signs, no spaces, no decimal point.
    """
    for ch in sobj:
        if ch not in '0123456789':
            return False
    return len(sobj) > 0  # empty string should not be an integer

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
