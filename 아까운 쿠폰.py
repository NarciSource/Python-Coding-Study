import sys
n = int(sys.stdin.readline())
coupons = [50000,10000,5000,1000,500,100,50,10]
count = 0
for coupon in coupons:
    count += n//coupon
    n %= coupon
print(count)