import io
import sys

_INPUT = """\
4 8
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
a,b = map(int,input().split())
gcd = 1
for i in range(2,min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)