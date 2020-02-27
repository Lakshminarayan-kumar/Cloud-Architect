# encoding: utf-8
# module _locale
# from /root/PycharmProjects/FirstDockerProject/venv/lib64/python2.7/lib-dynload/_localemodule.so
# by generator 1.147
""" Support for POSIX locales. """
# no imports

# Variables with simple values

ABDAY_1 = 131072
ABDAY_2 = 131073
ABDAY_3 = 131074
ABDAY_4 = 131075
ABDAY_5 = 131076
ABDAY_6 = 131077
ABDAY_7 = 131078

ABMON_1 = 131086
ABMON_10 = 131095
ABMON_11 = 131096
ABMON_12 = 131097
ABMON_2 = 131087
ABMON_3 = 131088
ABMON_4 = 131089
ABMON_5 = 131090
ABMON_6 = 131091
ABMON_7 = 131092
ABMON_8 = 131093
ABMON_9 = 131094

ALT_DIGITS = 131119

AM_STR = 131110

CHAR_MAX = 127

CODESET = 14

CRNCYSTR = 262159

DAY_1 = 131079
DAY_2 = 131080
DAY_3 = 131081
DAY_4 = 131082
DAY_5 = 131083
DAY_6 = 131084
DAY_7 = 131085

D_FMT = 131113

D_T_FMT = 131112

ERA = 131116

ERA_D_FMT = 131118

ERA_D_T_FMT = 131120

ERA_T_FMT = 131121

LC_ALL = 6
LC_COLLATE = 3
LC_CTYPE = 0
LC_MESSAGES = 5
LC_MONETARY = 4
LC_NUMERIC = 1
LC_TIME = 2

MON_1 = 131098
MON_10 = 131107
MON_11 = 131108
MON_12 = 131109
MON_2 = 131099
MON_3 = 131100
MON_4 = 131101
MON_5 = 131102
MON_6 = 131103
MON_7 = 131104
MON_8 = 131105
MON_9 = 131106

NOEXPR = 327681

PM_STR = 131111

RADIXCHAR = 65536

THOUSEP = 65537

T_FMT = 131114

T_FMT_AMPM = 131115

YESEXPR = 327680

_DATE_FMT = 131180

# functions

def bindtextdomain(domain, dir): # real signature unknown; restored from __doc__
    """
    bindtextdomain(domain, dir) -> string
    Bind the C library's domain to dir.
    """
    return ""

def bind_textdomain_codeset(domain, codeset): # real signature unknown; restored from __doc__
    """
    bind_textdomain_codeset(domain, codeset) -> string
    Bind the C library's domain to codeset.
    """
    return ""

def dcgettext(domain, msg, category): # real signature unknown; restored from __doc__
    """
    dcgettext(domain, msg, category) -> string
    Return translation of msg in domain and category.
    """
    return ""

def dgettext(domain, msg): # real signature unknown; restored from __doc__
    """
    dgettext(domain, msg) -> string
    Return translation of msg in domain.
    """
    return ""

def gettext(msg): # real signature unknown; restored from __doc__
    """
    gettext(msg) -> string
    Return translation of msg.
    """
    return ""

def localeconv(*args, **kwargs): # real signature unknown
    """ () -> dict. Returns numeric and monetary locale-specific parameters. """
    pass

def nl_langinfo(key): # real signature unknown; restored from __doc__
    """
    nl_langinfo(key) -> string
    Return the value for the locale information associated with key.
    """
    return ""

def setlocale(*args, **kwargs): # real signature unknown
    """ (integer,string=None) -> string. Activates/queries locale processing. """
    pass

def strcoll(*args, **kwargs): # real signature unknown
    """ string,string -> int. Compares two strings according to the locale. """
    pass

def strxfrm(*args, **kwargs): # real signature unknown
    """ string -> string. Returns a string that behaves for cmp locale-aware. """
    pass

def textdomain(domain): # real signature unknown; restored from __doc__
    """
    textdomain(domain) -> string
    Set the C library's textdmain to domain, returning the new domain.
    """
    return ""

# classes

class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



