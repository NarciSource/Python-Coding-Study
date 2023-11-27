n = int(input())+1
mod = 1000000007

def FastDoubling(n):
    if n > 0:
        fn, fn_1 = FastDoubling((n // 2))

        f2n = (fn * (2*fn_1 - fn)) % mod
        f2n_1 = (fn**2 + fn_1**2) % mod
        
        return [f2n, f2n_1] if n%2==0 else [f2n_1, f2n_1 + f2n]
    else:
        return [0,1]
print(FastDoubling(n)[0])





"""
import math

mod = 1000000007
def binets_formula(n):
    sqrt5 = math.sqrt(5)

    F_n = int((( (1 + sqrt5) ** n - (1 - sqrt5) ** n ) / ( 2 ** n * sqrt5 )))
    return F_n
print(binets_formula(int(input())+1)%mod)
"""