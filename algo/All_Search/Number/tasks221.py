import io
import sys

_INPUT = """\
6
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
cnt = 0
for i in range(n):
    i += 1
    if n % i == 0:
        cnt += 1
print(cnt)