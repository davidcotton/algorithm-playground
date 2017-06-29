import timeit


def time_method(fn, n):
    """Time how long each method takes."""
    return '{} took {}'.format(
        fn.__name__,
        timeit.timeit(
            '{}({})'.format(fn.__name__, n),
            setup='from __main__ import {}'.format(fn.__name__),
            number=3
        )
    )
