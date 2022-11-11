import io
import sys

_INPUT = """\
5
-1 3 5 -7 -9
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------

n = int(input())
a = list(map(int,input().split()))
min = 100
for i in range(n):
    if a[i] < min:
        min = a[i]
print(min)