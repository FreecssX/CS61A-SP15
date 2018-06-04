## Extra Linked Lists and Sets ##

from lab08 import *

# Set Practice

def add_up(n, lst):
    """Returns True if any two non identical elements in lst add up to any n.

    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    >>> add_up(7, [1, 2, 3, 4, 2])
    True
    >>> add_up(10, [5, 5])
    False
    """
    "*** YOUR CODE HERE ***"
    # new_lst=list(set(lst))
    # sum_lst=[]
    # for i in range(len(new_lst)-1):
    #     for j in range(i+1,len(new_lst)):
    #         sum_lst.append(new_lst[i]+new_lst[j])
    # sum_lst=set(sum_lst)
    # sum_lst=list(sum_lst)
    # sum_lst.append(n)
    # return len(set(sum_lst))!=len(sum_lst)
    check_set=set()
    for elem in lst:
        if n-elem!=elem:
            check_set.add(n-elem)
    return bool(intersection(check_set,set(lst)))
def pow(n,k):
    """Computes n^k.

    >>> pow(2, 3)
    8
    >>> pow(4, 2)
    16
    """
    "*** YOUR CODE HERE ***"
    if k==0:
        return 1
    if k%2==0:
        return pow(n,k//2)**2
    else:
        return pow(n,k-1)*n

def missing_no(lst):
    """lst contains all the numbers from 1 to n for some n except some
    number k. Find k.

    >>> missing_no([1, 0, 4, 5, 7, 9, 2, 6, 3])
    8
    >>> missing_no(list(filter(lambda x: x != 293, list(range(2000)))))
    293
    """
    "*** YOUR CODE HERE ***"
    max_num=max(lst)
    return list(set(range(max_num+1))-set(lst))[0]
    # return sum(list(range(max(lst)+1)))-sum(lst)
def find_duplicates_k(k, lst):
    """Returns True if there are any duplicates in lst that are within k
    indices apart.

    >>> find_duplicates_k(3, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k(4, [1, 2, 3, 4, 1])
    True
    """
    "*** YOUR CODE HERE ***"
    return len(set(lst[:k+1]))!=len(lst[:k+1])

def find_duplicates_k_l(k, l, lst):
    """Returns True if there are any two values who in lst that are within k
    indices apart AND if the absolute value of their difference is less than
    or equal to l.

    >>> find_duplicates_k_l(4, 0, [1, 2, 3, 4, 5])
    False
    >>> find_duplicates_k_l(4, 1, [1, 2, 3, 4, 5])
    True
    >>> find_duplicates_k_l(4, 0, [1, 2, 3, 4, 1])
    True
    >>> find_duplicates_k_l(2, 0, [1, 2, 3, 4, 1])
    False
    >>> find_duplicates_k_l(1, 100, [100, 275, 320, 988, 27])
    False
    >>> find_duplicates_k_l(1, 100, [100, 199, 275, 320, 988, 27])
    True
    >>> find_duplicates_k_l(1, 100, [100, 23, 199, 275, 320, 988, 27])
    True
    >>> find_duplicates_k_l(2, 100, [100, 23, 199, 275, 320, 988, 27])
    True
    """
    "*** YOUR CODE HERE ***"
    new_list=lst[0:k+1]
    check_set=set()
    for j in new_list:
        if True in [i in range(j-l,j+l+1) for i in check_set]:
            return True
        check_set.add(j)
    return False



