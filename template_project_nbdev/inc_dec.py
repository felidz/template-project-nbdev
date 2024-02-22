# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/00_inc_dec.ipynb.

# %% auto 0
__all__ = ['inc', 'dec']

# %% ../nbs/api/00_inc_dec.ipynb 4
from .module.submodule import Foo


# %% ../nbs/api/00_inc_dec.ipynb 5
def inc(x: int) -> int:
    """ increment
    """
    foo = Foo()
    foo.bar()
    return x + 1


# %% ../nbs/api/00_inc_dec.ipynb 9
def dec(x: int) -> int:
    """ decrement
    """
    return x - 1

