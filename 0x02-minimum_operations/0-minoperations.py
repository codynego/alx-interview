#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    write a method that calculates the fewest number of
    operations needed to result in exactly n
    H characters in the file
    Returns:
        returns an int
    """
    operation_count = 0
    characters = "H"
    clipboard = ""

    for i in range(n):
        if len(characters) > n or n <= 1:
            return (0)

        if len(characters) == n:
            break
        else:
            if n % len(characters) == 0:
                clipboard = characters
                characters += clipboard
                operation_count += 2

            else:
                characters += clipboard
                operation_count += 1

    return (operation_count)
