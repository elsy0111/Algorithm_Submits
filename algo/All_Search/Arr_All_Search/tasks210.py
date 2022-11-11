import io
import sys

_INPUT = """\
5 1
3 5 1 9 1
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------

n,v = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
for ai in a:
    if ai == v:
        cnt += 1

print(cnt)