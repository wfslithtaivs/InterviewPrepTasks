"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of thh two::

    >>> rain([10, 2, 3, 4, 9])
    18

Bunch of tallest buildings are of the same length:

    >>> rain([4, 2, 3, 3, 3])
    1

    >>> rain([4, 2, 3, 3, 3, 4])
    5

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""

def len_between_indexes(a, start, finish):
    """" Calculates amount of rain between given buildings"""
    amount = 0

    roof_top = min(a[start], a[finish])

    for i in range(start + 1, finish):
        amount += roof_top - a[i]

    return amount

def rain(buildings):
    """How much rain is trapped in Codelandia?"""

    rain_amount = 0
    rain_stack = []

    # return 0 if no buildings to hold any rain
    if len(buildings) < 3:
        return rain_amount

    a = [0] + buildings + [0] # sentinell value (dummy data to avoid border cases)

    # iterate over list of buildings
    for i in range(1, len(a) - 1):

         # if we have a local maximum (redundant check, optimization only)
        if a[i] > a[i-1] and a[i] >= a[i+1]:

            # remove from stack everything less than current element
            while len(rain_stack) > 1 and a[rain_stack[-1]] <= a[i]:
                rain_stack.pop()

            # collapse current element with the bottom element of stack
            if len(rain_stack) == 1 and a[rain_stack[-1]] <= a[i]:
                rain_amount += len_between_indexes(a, rain_stack[-1], i)
                rain_stack.pop()
                
            # append stack with the current element
            rain_stack.append(i)

    # calculate rain amount between stacked borders             
    while len(rain_stack) > 1:
        rain_amount += len_between_indexes(a, rain_stack[0], rain_stack[1])
        rain_stack.pop(0)

    # return rain amount
    return rain_amount

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
