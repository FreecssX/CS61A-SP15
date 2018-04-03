def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert lower_bound(y) != upper_bound(y)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    y_lower = lower_bound(y)
    y_upper = upper_bound(y)
    negtive_y = interval(-y_upper, -y_lower)
    return add_interval(x, negtive_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
par1((8, 10), (12, 14)) != par2((8, 10), (12, 14))

def multiple_references_explanation():
    return """par2 computes the interval using r1 and r2 for only once"""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    f = lambda x: a * x ** 2 + b * x + c
    extreme = - b / 2 / a
    e, l, u = map(f, [extreme, lower_bound(x), upper_bound(x)])
    if e <= upper_bound(x) and e >= lower_bound(x):
        return interval(min([e, l, u]), max([e, l, u]))
    return interval(min(l, u), max(l, u))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
    """newton method"""
    def improve(update, close, guess = 1):
        while not close(guess):
            guess = update(guess)
        return guess
    
    def approx_eq(x, y, tolerance = 1e-15):
        return abs(x -y) < tolerance

    def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

    def find_zero(f, df, n):
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero, n)

    #############

    def add_f(k, c, f):
        return lambda x: c * pow(x, k) + f(x)
    def add_df(k, c, df):
        return lambda x: k * c * pow(x, k - 1) + df(x)
    def add_ddf(k, c, ddf):
        return lambda x: k * (k - 1) * c * pow(x, k - 2) + ddf(x)

    f = lambda x: 0
    df = lambda x: 0
    ddf = lambda x: 0
    i = 0 
    for co in c:
        f = add_f(i, co, f)
        if i > 0:
            df = add_df(i, co, df)
        if i > 1:
            ddf = add_ddf(i, co, ddf)
        i += 1
    upper = upper_bound(x)
    lower = lower_bound(x)

    steps = 20

    nums = [lower + i * (upper - lower) / 20 for i in range(1,steps)]

    extremes = [find_zero(df, ddf, n) for n in nums]

    extremes_new = [e for e in extremes if e <= upper and e >= lower] + [lower, upper]

    results = [f(x) for x in extremes_new]
    return interval(min(results), max(results))


