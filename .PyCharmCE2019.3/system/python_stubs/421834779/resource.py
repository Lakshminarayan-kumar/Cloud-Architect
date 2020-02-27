# encoding: utf-8
# module resource
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/resource.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

RLIMIT_AS = 9
RLIMIT_CORE = 4
RLIMIT_CPU = 0
RLIMIT_DATA = 2
RLIMIT_FSIZE = 1
RLIMIT_MEMLOCK = 8
RLIMIT_NOFILE = 7
RLIMIT_NPROC = 6
RLIMIT_OFILE = 7
RLIMIT_RSS = 5
RLIMIT_STACK = 3

RLIM_INFINITY = -1

RUSAGE_CHILDREN = -1
RUSAGE_SELF = 0

# functions

def getpagesize(*args, **kwargs): # real signature unknown
    pass

def getrlimit(*args, **kwargs): # real signature unknown
    pass

def getrusage(*args, **kwargs): # real signature unknown
    pass

def setrlimit(*args, **kwargs): # real signature unknown
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class struct_rusage(object):
    """
    struct_rusage: Result from getrusage.
    
    This object may be accessed either as a tuple of
        (utime,stime,maxrss,ixrss,idrss,isrss,minflt,majflt,
        nswap,inblock,oublock,msgsnd,msgrcv,nsignals,nvcsw,nivcsw)
    or via the attributes ru_utime, ru_stime, ru_maxrss, and so on.
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

    ru_idrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """unshared data size"""

    ru_inblock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """block input operations"""

    ru_isrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """unshared stack size"""

    ru_ixrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """shared memory size"""

    ru_majflt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """page faults requiring I/O"""

    ru_maxrss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """max. resident set size"""

    ru_minflt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """page faults not requiring I/O"""

    ru_msgrcv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPC messages received"""

    ru_msgsnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPC messages sent"""

    ru_nivcsw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """involuntary context switches"""

    ru_nsignals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """signals received"""

    ru_nswap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number of swap outs"""

    ru_nvcsw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """voluntary context switches"""

    ru_oublock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """block output operations"""

    ru_stime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time used"""

    ru_utime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time used"""


    n_fields = 16
    n_sequence_fields = 16
    n_unnamed_fields = 0


