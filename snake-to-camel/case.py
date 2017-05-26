"""Given a variable name in snake_case, return camelCase of name.

For example::

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'

"""

def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    variable_name = variable_name.split('_')
    res = variable_name[0]
    for i in range(1, len(variable_name)):
        res += variable_name[i].capitalize()
    return res
    
print "Camelcased hi_balloonicorn looks like this: " + snake_to_camel("hi_balloonicorn")
print "Camelcased snake_to_camel looks like this: " + snake_to_camel("snake_to_camel")       

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"
