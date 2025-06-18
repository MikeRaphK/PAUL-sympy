from sympy.core.basic import Basic

class DefaultPrinting(Basic):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _repr_latex_(self):
        """
        LaTeX representation of the expression.

        This method should be overloaded in subclasses to provide custom LaTeX
        representation. The default implementation falls back to string
        representation.

        """
        return str(self)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return super().__repr__()
