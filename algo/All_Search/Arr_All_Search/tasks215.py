import io
import sys

_INPUT = """\
5
31 41 59 26 53
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(1,n):
    if a[i-1] < a[i]:
        cnt += 1
print(cnt)