def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
    	return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3) 

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    g1 = 1
    g2 = 2
    g3 = 3
    index = 1
    while index < n:
    	g1, g2, g3 = g2, g3, g3 + 2 * g2 + 3 * g1
    	index += 1
    return g1



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
    	return False
    return k % 10 == 7 or has_seven(k // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    def countup(dir, start, end):
    	if start == end:
    		return 1
    	if has_seven(start) or start % 7 == 0:
    		dir = not dir
    	if dir:
    		return countup(dir, start + 1, end) + 1
    	else:
    		return countup(dir, start + 1, end) - 1
    return countup(True, 1, n)



def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    coins = []
    i = 0
    while 2 ** i <= amount:
    	coins.append(2 ** i)
    	i += 1
    def count(m, c):
    	if m == 0:
    		return 1
    	if m < 0:
    		return 0
    	if len(c) == 0:
    		return 0
    	return count(m - c[len(c) - 1], c) + count(m, c[: -1])
    return count(amount, coins)



def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
    	print_step(start, end)
    	return
    middle = 6 - start - end
    towers_of_hanoi(n - 1, start, middle)
    towers_of_hanoi(1, start, end)
    towers_of_hanoi(n - 1, middle, end)


def print_step(start, end):
	print("Move the top disk from rod", str(start), "to rod", str(end))

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
