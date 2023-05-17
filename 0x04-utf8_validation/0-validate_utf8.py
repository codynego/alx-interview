#!/usr/bin/python3

"""
utf-8 validation
"""


def validUTF8(data):
    """
    check if a data is a valid utf-8 encoding
    """
    for i in data:
        if len(bin(i)[2:]) > 8 or type(i) != int:
            return False
    return True
