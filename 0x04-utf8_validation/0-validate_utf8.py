#!/usr/bin/python3

"""
utf-8 validation
"""


def validUTF8(data):
    """
    check if a data is a valid utf-8 encoding
    """
    if max(data) > 255:
        return False
    return True
