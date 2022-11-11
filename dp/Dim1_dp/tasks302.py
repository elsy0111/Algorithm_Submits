import io
import sys

_INPUT = """\
6 1 1
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------

n,x,y = map(int,input().split())
A = [[] for i in range(n + 1)]
A[0],A[1] = x,y
for i in range(2,n):
    A[i] = (A[i - 2] + A[i - 1]) % 100
print(A[n - 1])