import io
import sys

_INPUT = """\
10
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
cnt = 0
for i in range(n):
    i += 1
    if i % 2:
        if i % 3:
            if i % 5:
                cnt += 1
print(cnt)