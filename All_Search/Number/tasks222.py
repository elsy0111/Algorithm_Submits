import io
import sys

_INPUT = """\
11
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
for i in range(2,n):
    if n % i == 0:
        break
    if i == n - 1:
        print("Yes")
        exit()
print("No")