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
max = -100
for i in a:
    if i > max:
        max = i
print(max)