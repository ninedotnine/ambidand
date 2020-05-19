def dconst(x):
    """dconst(x) is a function which, when called with anything,
    returns x"""
    return lambda _: x

def dif(expr):
    """dif(expr) is a function which returns the first of its args if
    expr is True, the second otherwise."""
    return (lambda first, second: first if expr else second)

def dand(expr):
    """dand is a curried version of logical and."""
    if not expr:
        return dconst(False)
    return (lambda expr2: True if expr2 else False)

def dor(expr):
    """dor is a curried version of logical or."""
    if expr:
        return dconst(True)
    return (lambda expr2: True if expr2 else False)

def dxor(expr):
    """dxor is a curried version of logical xor."""
    if expr:
        return (lambda expr2: False if expr2 else True)
    else:
        return (lambda expr2: True if expr2 else False)
