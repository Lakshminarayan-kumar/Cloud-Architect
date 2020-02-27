# encoding: utf-8
# module zlib
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/zlibmodule.so
# by generator 1.147
"""
The functions in this module allow compression and decompression using the
zlib library, which is based on GNU zip.

adler32(string[, start]) -- Compute an Adler-32 checksum.
compress(string[, level]) -- Compress string, with compression level in 0-9.
compressobj([level]) -- Return a compressor object.
crc32(string[, start]) -- Compute a CRC-32 checksum.
decompress(string,[wbits],[bufsize]) -- Decompresses a compressed string.
decompressobj([wbits]) -- Return a decompressor object.

'wbits' is window buffer size.
Compressor objects support compress() and flush() methods; decompressor
objects support decompress() and flush().
"""
# no imports

# Variables with simple values

DEFLATED = 8

DEF_MEM_LEVEL = 8

MAX_WBITS = 15

ZLIB_VERSION = '1.2.7'

Z_BEST_COMPRESSION = 9
Z_BEST_SPEED = 1

Z_DEFAULT_COMPRESSION = -1
Z_DEFAULT_STRATEGY = 0

Z_FILTERED = 1
Z_FINISH = 4

Z_FULL_FLUSH = 3

Z_HUFFMAN_ONLY = 2

Z_NO_FLUSH = 0

Z_SYNC_FLUSH = 2

__version__ = '1.0'

# functions

def adler32(string, start=None): # real signature unknown; restored from __doc__
    """
    adler32(string[, start]) -- Compute an Adler-32 checksum of string.
    
    An optional starting value can be specified.  The returned checksum is
    a signed integer.
    """
    pass

def compress(string, level=None): # real signature unknown; restored from __doc__
    """
    compress(string[, level]) -- Returned compressed string.
    
    Optional arg level is the compression level, in 0-9.
    """
    pass

def compressobj(level=None): # real signature unknown; restored from __doc__
    """
    compressobj([level]) -- Return a compressor object.
    
    Optional arg level is the compression level, in 0-9.
    """
    pass

def crc32(string, start=None): # real signature unknown; restored from __doc__
    """
    crc32(string[, start]) -- Compute a CRC-32 checksum of string.
    
    An optional starting value can be specified.  The returned checksum is
    a signed integer.
    """
    pass

def decompress(string, wbits=None, bufsize=None): # real signature unknown; restored from __doc__
    """
    decompress(string[, wbits[, bufsize]]) -- Return decompressed string.
    
    Optional arg wbits is the window buffer size.  Optional arg bufsize is
    the initial output buffer size.
    """
    pass

def decompressobj(wbits=None): # real signature unknown; restored from __doc__
    """
    decompressobj([wbits]) -- Return a decompressor object.
    
    Optional arg wbits is the window buffer size.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



