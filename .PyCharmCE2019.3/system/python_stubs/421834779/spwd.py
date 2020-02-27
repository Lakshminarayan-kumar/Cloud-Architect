# encoding: utf-8
# module spwd
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/spwdmodule.so
# by generator 1.147
"""
This module provides access to the Unix shadow password database.
It is available on various Unix versions.

Shadow password database entries are reported as 9-tuples of type struct_spwd,
containing the following items from the password database (see `<shadow.h>'):
sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max, sp_warn, sp_inact, sp_expire, sp_flag.
The sp_namp and sp_pwdp are strings, the rest are integers.
An exception is raised if the entry asked for cannot be found.
You have to be root to be able to use this module.
"""
# no imports

# functions

def getspall(): # real signature unknown; restored from __doc__
    """
    getspall() -> list_of_entries
    Return a list of all available shadow password database entries, in arbitrary order.
    See spwd.__doc__ for more on shadow password database entries.
    """
    pass

def getspnam(name): # real signature unknown; restored from __doc__
    """
    getspnam(name) -> (sp_namp, sp_pwdp, sp_lstchg, sp_min, sp_max,
                        sp_warn, sp_inact, sp_expire, sp_flag)
    Return the shadow password database entry for the given user name.
    See spwd.__doc__ for more on shadow password database entries.
    """
    pass

# classes

class struct_spwd(object):
    """
    spwd.struct_spwd: Results from getsp*() routines.
    
    This object may be accessed either as a 9-tuple of
      (sp_nam,sp_pwd,sp_lstchg,sp_min,sp_max,sp_warn,sp_inact,sp_expire,sp_flag)
    or via the object attributes as named in the above tuple.
    """
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    sp_expire = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days since 1970-01-01 until account is disabled"""

    sp_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """reserved"""

    sp_inact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days after pw expires until account is blocked"""

    sp_lstchg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """date of last change"""

    sp_max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max #days between changes"""

    sp_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """min #days between changes"""

    sp_nam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """login name"""

    sp_pwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """encrypted password"""

    sp_warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """#days before pw expires to warn user about it"""


    n_fields = 9
    n_sequence_fields = 9
    n_unnamed_fields = 0


