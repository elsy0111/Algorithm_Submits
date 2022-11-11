import io
import sys

_INPUT = """\
5 1
3 5 1 9 2

"""

sys.stdin = io.StringIO(_INPUT)

n,p = map(int,input().split())
a = list(map(int,input().split()))

for i in a:
    if i == p:
        print("Yes")
        exit()

print("No")