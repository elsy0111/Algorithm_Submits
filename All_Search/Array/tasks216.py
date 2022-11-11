import io
import sys

_INPUT = """\
5 5
3 5 5 9 5
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------

n,v = map(int,input().split())
a = list(map(int,input().split()))
a.reverse()
for i in range(n):
    if a[i] == v:
        print(n - i - 1)
        exit()
print(-1)
