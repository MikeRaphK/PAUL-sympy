class Basic(Printable, metaclass=ManagedProperties):
    """
    Base class for all SymPy objects.

    ...
    """
    __slots__ = ('_mhash',              # hash value
                 '_args',               # arguments
                 '_assumptions',         # assumptions
                 # Add an empty __slots__ to prevent __dict__ creation
                 '__dict__'             # Allow __dict__ to exist
                )

    ...class DefaultPrinting:
    __slots__ = ()
    # Adding empty __slots__ to DefaultPrinting class to prevent __dict__ creation
    __slots__ = ()
class DefaultPrinting:
    __slots__ = ()
