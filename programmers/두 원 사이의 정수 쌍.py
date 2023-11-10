from math import sqrt, floor, ceil
solution = lambda r1, r2: (
    sum(map(lambda x: floor(sqrt(r2**2-x**2)), range(r2)))
    - sum(map(lambda x: ceil(sqrt(r1**2-x**2)-1), range(r1)))
    )*4