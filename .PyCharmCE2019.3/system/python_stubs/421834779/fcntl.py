# encoding: utf-8
# module fcntl
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/fcntlmodule.so
# by generator 1.147
"""
This module performs file control and I/O control on file 
descriptors.  It is an interface to the fcntl() and ioctl() Unix
routines.  File descriptors can be obtained with the fileno() method of
a file or socket object.
"""
# no imports

# Variables with simple values

DN_ACCESS = 1
DN_ATTRIB = 32
DN_CREATE = 4
DN_DELETE = 8
DN_MODIFY = 2
DN_MULTISHOT = 2147483648
DN_RENAME = 16

FASYNC = 8192

FD_CLOEXEC = 1

F_DUPFD = 0
F_EXLCK = 4
F_GETFD = 1
F_GETFL = 3
F_GETLEASE = 1025
F_GETLK = 5
F_GETLK64 = 5
F_GETOWN = 9
F_GETSIG = 11
F_NOTIFY = 1026
F_RDLCK = 0
F_SETFD = 2
F_SETFL = 4
F_SETLEASE = 1024
F_SETLK = 6
F_SETLK64 = 6
F_SETLKW = 7
F_SETLKW64 = 7
F_SETOWN = 8
F_SETSIG = 10
F_SHLCK = 8
F_UNLCK = 2
F_WRLCK = 1

LOCK_EX = 2
LOCK_MAND = 32
LOCK_NB = 4
LOCK_READ = 64
LOCK_RW = 192
LOCK_SH = 1
LOCK_UN = 8
LOCK_WRITE = 128

# functions

def fcntl(fd, opt, arg=None): # real signature unknown; restored from __doc__
    """
    fcntl(fd, opt, [arg])
    
    Perform the requested operation on file descriptor fd.  The operation
    is defined by op and is operating system dependent.  These constants are
    available from the fcntl module.  The argument arg is optional, and
    defaults to 0; it may be an int or a string.  If arg is given as a string,
    the return value of fcntl is a string of that length, containing the
    resulting value put in the arg buffer by the operating system.  The length
    of the arg string is not allowed to exceed 1024 bytes.  If the arg given
    is an integer or if none is specified, the result value is an integer
    corresponding to the return value of the fcntl call in the C code.
    """
    pass

def flock(fd, operation): # real signature unknown; restored from __doc__
    """
    flock(fd, operation)
    
    Perform the lock operation op on file descriptor fd.  See the Unix 
    manual page for flock(3) for details.  (On some systems, this function is
    emulated using fcntl().)
    """
    pass

def ioctl(fd, opt, arg=None, mutate_flag=None): # real signature unknown; restored from __doc__
    """
    ioctl(fd, opt[, arg[, mutate_flag]])
    
    Perform the requested operation on file descriptor fd.  The operation is
    defined by opt and is operating system dependent.  Typically these codes are
    retrieved from the fcntl or termios library modules.
    
    The argument arg is optional, and defaults to 0; it may be an int or a
    buffer containing character data (most likely a string or an array). 
    
    If the argument is a mutable buffer (such as an array) and if the
    mutate_flag argument (which is only allowed in this case) is true then the
    buffer is (in effect) passed to the operating system and changes made by
    the OS will be reflected in the contents of the buffer after the call has
    returned.  The return value is the integer returned by the ioctl system
    call.
    
    If the argument is a mutable buffer and the mutable_flag argument is not
    passed or is false, the behavior is as if a string had been passed.  This
    behavior will change in future releases of Python.
    
    If the argument is an immutable buffer (most likely a string) then a copy
    of the buffer is passed to the operating system and the return value is a
    string of the same length containing whatever the operating system put in
    the buffer.  The length of the arg buffer in this case is not allowed to
    exceed 1024 bytes.
    
    If the arg given is an integer or if none is specified, the result value is
    an integer corresponding to the return value of the ioctl call in the C
    code.
    """
    pass

def lockf(fd, operation, length=0, start=0, whence=0): # real signature unknown; restored from __doc__
    """
    lockf (fd, operation, length=0, start=0, whence=0)
    
    This is essentially a wrapper around the fcntl() locking calls.  fd is the
    file descriptor of the file to lock or unlock, and operation is one of the
    following values:
    
        LOCK_UN - unlock
        LOCK_SH - acquire a shared lock
        LOCK_EX - acquire an exclusive lock
    
    When operation is LOCK_SH or LOCK_EX, it can also be bitwise ORed with
    LOCK_NB to avoid blocking on lock acquisition.  If LOCK_NB is used and the
    lock cannot be acquired, an IOError will be raised and the exception will
    have an errno attribute set to EACCES or EAGAIN (depending on the operating
    system -- for portability, check for either value).
    
    length is the number of bytes to lock, with the default meaning to lock to
    EOF.  start is the byte offset, relative to whence, to that the lock
    starts.  whence is as with fileobj.seek(), specifically:
    
        0 - relative to the start of the file (SEEK_SET)
        1 - relative to the current buffer position (SEEK_CUR)
        2 - relative to the end of the file (SEEK_END)
    """
    pass

# no classes
