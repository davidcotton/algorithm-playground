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


def time_method(fn, n):
    """Time how long each method takes.
    Return a string with the name of the function, the time it took and the result."""
    time, result = timeit.timeit(
        '{}({})'.format(fn.__name__, n),
        setup='from __main__ import {}'.format(fn.__name__),
        number=3
    )
    return '{} took {} and the result was \n  {}'.format(fn.__name__, time, result)
