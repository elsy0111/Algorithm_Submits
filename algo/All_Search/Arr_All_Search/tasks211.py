import io
import sys

_INPUT = """\
5
3 5 1 9 2
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------

n = int(input())
a = list(map(int,input().split()))
max = 0
idx = 0
for i in range(n):
    if a[i] > max:
        max = a[i]
        idx = i
print(idx)