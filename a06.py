import io
import sys

_INPUT = """\
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10
"""

sys.stdin = io.StringIO(_INPUT)

#==============================
N,Q = map(int,input().split())
A = list(map(int,input().split()))
for i in range(1,N):
    A[i] += A[i - 1]
for i in range(Q):
    L,R = map(int,input().split())
    if L - 2 >= 0:
        print(A[R - 1]-A[L - 2])
    else:
        print(A[R - 1]-0)