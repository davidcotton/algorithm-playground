import timeit

# override timeit to return the function result
timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""


def time_method_pp(fn, n):
    """Pretty print a method's run time."""
    name, time, result = time_method(fn, n)
    return '{} took {} and the result was \n  {}'.format(name, time, result)


def time_method(fn, n):
    """Time how long each method takes.
    Return the name of the function, the time it took and the result."""
    time, result = timeit.timeit(
        '{}({})'.format(fn.__name__, n),
        setup='from __main__ import {}'.format(fn.__name__),
        number=3
    )
    return fn.__name__, time, result
