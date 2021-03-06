from legacy import *

__test__ = {'': r"""
    Simple transform
    >>> transform_to(
    ...    None,
    ...    '/event/%s/', {'a': 1}, to_url=['a'],
    ...    resolver=format_resolver
    ... )
    '/event/1/'

    Transform with custom processing
    >>> transform_to(
    ...    None,
    ...    '/event/%s/', {'a': 1, 'b': 2},
    ...    to_url=['ab'], process={('a', 'b'): lambda req, a, b: {'ab': '%s%s' % (a, b)}},
    ...    resolver=format_resolver
    ... )
    '/event/12/'

    Transform with processing and rewrite
    >>> transform_to(
    ...    None,
    ...    '/event/%s/%s/', {'a': 1, 'b': 2},
    ...    to_url=['a', 'c'], process={'c': lambda req, c: c + 1},rewrites={'b': 'c'},
    ...    resolver=format_resolver
    ... )
    '/event/1/3/'

    Transform with list in params
    >>> transform_to(
    ...    None,
    ...    '/event/%s/', {'a': 1, 'b': [2, 3]},
    ...    to_url=['a'], to_query=['b'],
    ...    resolver=format_resolver
    ... )
    '/event/1/?b=2&b=3'
"""
}
