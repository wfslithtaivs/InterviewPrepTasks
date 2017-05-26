"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards(0)
    '0'

    >>> dec2bin_backwards(1)
    '1'

    >>> dec2bin_backwards(2)
    '10'

    >>> dec2bin_backwards(4)
    '100'

    >>> dec2bin_backwards(15)
    '1111'

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""

def dec2bin_forwards(num):
    """Convert a decimal number to binary representation."""
    if num == 0: return "0"

    res = []

    while num != 0:
        res.append(str(num % 2))
        num /= 2

    return ''.join(res[::-1])

def dec2bin_backwards(num):
    """Convert a decimal number to binary representation."""
    if num == 0: return "0"

    res = ""

    while num != 0:
        res = str(num % 2) + res
        num /= 2

    return res


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
