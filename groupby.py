from itertools import groupby

even = lambda x: x % 2 is 0
odd  = lambda x: not even(x)
data = [1, 2, 3, 4]

assert filter(even, data) == [2, 4]
assert filter(odd, data) == [1, 3]