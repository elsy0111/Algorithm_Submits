import io
import sys

_INPUT = """\
10
1 5 2 9 6 4 9 3 4 9
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------

n = int(input())
a = list(map(int,input().split()))
cnt = [0]*9
for i in a:
    for j in range(1,9+1):
        if i == j:
            cnt[j-1] += 1
max = 0
idx = 0
for i in range(9):
    if max < cnt[i]:
        max = cnt[i]
        idx = i
print(idx + 1)