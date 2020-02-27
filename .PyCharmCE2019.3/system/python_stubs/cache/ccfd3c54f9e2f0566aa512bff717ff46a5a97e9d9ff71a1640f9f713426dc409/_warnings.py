# encoding: utf-8
# module _warnings
# from (built-in)
# by generator 1.147
"""
_warnings provides basic warning filtering support.
It is a helper module to speed up interpreter start-up.
"""
# no imports

# Variables with simple values

default_action = 'default'

# functions

def warn(*args, **kwargs): # real signature unknown
    """ Issue a warning, or maybe ignore it or raise an exception. """
    pass

def warn_explicit(*args, **kwargs): # real signature unknown
    """ Low-level inferface to warnings functionality. """
    pass

# no classes
# variables with complex values

filters = [
    (
        'ignore',
        None, # (!) real value is '<_sre.SRE_Pattern object at 0x7fbd76ec6030>'
        DeprecationWarning,
        None, # (!) real value is '<_sre.SRE_Pattern object at 0x7fbd7723b348>'
        0,
    ),
    (
        'ignore',
        None,
        '<value is a self-reference, replaced by this string>',
        None,
        0,
    ),
    (
        'ignore',
        None,
        PendingDeprecationWarning,
        None,
        0,
    ),
    (
        'ignore',
        None,
        ImportWarning,
        None,
        0,
    ),
    (
        'ignore',
        None,
        BytesWarning,
        None,
        0,
    ),
]

once_registry = {}

