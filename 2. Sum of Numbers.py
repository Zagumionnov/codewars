"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""
"""
-2 -1 0 1 2 3 4 
"""

"""
def get_sum(a,b):
    print([x for x in range(a, b+1)])



get_sum(-2, 2)
"""


def get_sum(a, b):
    if a <= b:
        c = a
        v = b
    else:
        v = a
        c = b

    z = 0
    if a != b:
        for i in range(c, v+1):
            z += i
    else:
        z = a

    return z


print(get_sum(0, -1))

"""
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
"""