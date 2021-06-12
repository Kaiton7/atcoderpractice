P = float(input())

import math

x  = 1.5 * math.log2(2.0/3.0 * P * math.log(2))

if x>=0:
    ans = x + P/math.pow(2.0, 2.0/3.0*x)
else:
    ans = P

print(ans)