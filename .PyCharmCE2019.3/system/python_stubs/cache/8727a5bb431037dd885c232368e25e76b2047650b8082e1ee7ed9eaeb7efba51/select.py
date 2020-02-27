# encoding: utf-8
# module select
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/selectmodule.so
# by generator 1.147
"""
This module supports asynchronous I/O on multiple file descriptors.

*** IMPORTANT NOTICE ***
On Windows and OpenVMS, only sockets are supported; on Unix, all file descriptors.
"""
# no imports

# Variables with simple values

EPOLLERR = 8
EPOLLET = 2147483648
EPOLLHUP = 16
EPOLLIN = 1
EPOLLMSG = 1024
EPOLLONESHOT = 1073741824
EPOLLOUT = 4
EPOLLPRI = 2
EPOLLRDBAND = 128
EPOLLRDNORM = 64
EPOLLWRBAND = 512
EPOLLWRNORM = 256

PIPE_BUF = 4096

POLLERR = 8
POLLHUP = 16
POLLIN = 1
POLLMSG = 1024
POLLNVAL = 32
POLLOUT = 4
POLLPRI = 2
POLLRDBAND = 128
POLLRDNORM = 64
POLLWRBAND = 512
POLLWRNORM = 256

# functions

def poll(*args, **kwargs): # real signature unknown
    """
    Returns a polling object, which supports registering and
    unregistering file descriptors, and then polling them for I/O events.
    """
    pass

def select(rlist, wlist, xlist, timeout=None): # real signature unknown; restored from __doc__
    """
    select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)
    
    Wait until one or more file descriptors are ready for some kind of I/O.
    The first three arguments are sequences of file descriptors to be waited for:
    rlist -- wait until ready for reading
    wlist -- wait until ready for writing
    xlist -- wait for an ``exceptional condition''
    If only one kind of condition is required, pass [] for the other lists.
    A file descriptor is either a socket or file object, or a small integer
    gotten from a fileno() method call on one of those.
    
    The optional 4th argument specifies a timeout in seconds; it may be
    a floating point number to specify fractions of seconds.  If it is absent
    or None, the call will never time out.
    
    The return value is a tuple of three lists corresponding to the first three
    arguments; each contains the subset of the corresponding file descriptors
    that are ready.
    
    *** IMPORTANT NOTICE ***
    On Windows and OpenVMS, only sockets are supported; on Unix, all file
    descriptors can be used.
    """
    pass

# classes

class epoll(object):
    """
    select.epoll([sizehint=-1])
    
    Returns an epolling object
    
    sizehint must be a positive integer or -1 for the default size. The
    sizehint is used to optimize internal data structures. It doesn't limit
    the maximum number of monitored events.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None
        
        Close the epoll control file descriptor. Further operations on the epoll
        object will raise an exception.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> int
        
        Return the epoll control file descriptor.
        """
        return 0

    @classmethod
    def fromfd(cls, fd): # real signature unknown; restored from __doc__
        """
        fromfd(fd) -> epoll
        
        Create an epoll object from a given control fd.
        """
        return epoll

    def modify(self, fd, eventmask): # real signature unknown; restored from __doc__
        """
        modify(fd, eventmask) -> None
        
        fd is the target file descriptor of the operation
        events is a bit set composed of the various EPOLL constants
        """
        pass

    def poll(self, timeout=-1, maxevents=-1): # real signature unknown; restored from __doc__
        """
        poll([timeout=-1[, maxevents=-1]]) -> [(fd, events), (...)]
        
        Wait for events on the epoll file descriptor for a maximum time of timeout
        in seconds (as float). -1 makes poll wait indefinitely.
        Up to maxevents are returned to the caller.
        """
        pass

    def register(self, fd, eventmask=None): # real signature unknown; restored from __doc__
        """
        register(fd[, eventmask]) -> None
        
        Registers a new fd or raises an IOError if the fd is already registered.
        fd is the target file descriptor of the operation.
        events is a bit set composed of the various EPOLL constants; the default
        is EPOLL_IN | EPOLL_OUT | EPOLL_PRI.
        
        The epoll interface supports all file descriptors that support poll.
        """
        pass

    def unregister(self, fd): # real signature unknown; restored from __doc__
        """
        unregister(fd) -> None
        
        fd is the target file descriptor of the operation.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, sizehint=-1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the epoll handler is closed"""



class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



