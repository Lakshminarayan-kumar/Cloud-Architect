# encoding: utf-8
# module grp
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/grpmodule.so
# by generator 1.147
"""
Access to the Unix group database.

Group entries are reported as 4-tuples containing the following fields
from the group database, in order:

  name   - name of the group
  passwd - group password (encrypted); often empty
  gid    - numeric ID of the group
  mem    - list of members

The gid is an integer, name and password are strings.  (Note that most
users are not explicitly listed as members of the groups they are in
according to the password database.  Check both databases to get
complete membership information.)
"""
# no imports

# functions

def getgrall(): # real signature unknown; restored from __doc__
    """
    getgrall() -> list of tuples
    Return a list of all available group entries, in arbitrary order.
    An entry whose name starts with '+' or '-' represents an instruction
    to use YP/NIS and may not be accessible via getgrnam or getgrgid.
    """
    return []

def getgrgid(id): # real signature unknown; restored from __doc__
    """
    getgrgid(id) -> tuple
    Return the group database entry for the given numeric group ID.  If
    id is not valid, raise KeyError.
    """
    return ()

def getgrnam(name): # real signature unknown; restored from __doc__
    """
    getgrnam(name) -> tuple
    Return the group database entry for the given group name.  If
    name is not valid, raise KeyError.
    """
    return ()

# classes

class struct_group(object):
    """
    grp.struct_group: Results from getgr*() routines.
    
    This object may be accessed either as a tuple of
      (gr_name,gr_passwd,gr_gid,gr_mem)
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

    gr_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group id"""

    gr_mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group memebers"""

    gr_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group name"""

    gr_passwd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """password"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0


