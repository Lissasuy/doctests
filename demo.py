def fibonacci(n):
    '''
    Return the nth fibonacci number.
    Recall that the fibonacci numbers are calculated by the following formula:

        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    HINT:
    The following "pseudocode" describes how to calculate the nth fibonacci number:

    Let f0 = 0
    Let f1 = 1
    In a for loop from 0 to n,
        Let fn = f0 + f1
        Let f0 = f1
        Let f1 = fn


    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(4)
    3
    >>> fibonacci(5)
    5
    >>> fibonacci(6)
    8
    >>> fibonacci(7)
    13
    >>> fibonacci(1000)
    43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    >>> type(fibonacci(4))
    <class 'int'>
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    f0 = 0
    f1 = 1
    for _ in range(2, n + 1):
       fn = f0 + f1
       f0 = f1
       f1 = fn
    return f1

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
    return max(xs)      
    '''
    Convert a list of lists into a single list that contains only the even elements.

    >>> nested_filter_odd([[2, 4, 5], [1, 3, 6]])
    [2, 4, 6]
    >>> nested_filter_odd([[1, 3, 6]])
    [6]
    >>> nested_filter_odd([[4, 5], [6, 7]])
    [4, 6]
    >>> nested_filter_odd([[20],[13,4,16,8,19],[10], [15, 13, 1]])
    [20, 4, 16, 8, 10]
    '''
    result = []
    for sublist in xss:
        for x in sublist:
            if x % 2 != 0:
                result.append(x)
    return result