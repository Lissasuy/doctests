def largest(xs):
    '''
    Return the largest element in a list.

    HINT:
    There is a built-in function on your cheat sheet that performs this task.

    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    None
    '''
    if not xs:
        return None
    current_max = xs[0]
    for x in xs:
        if x > current_max:
            current_max = x
    return current_max  