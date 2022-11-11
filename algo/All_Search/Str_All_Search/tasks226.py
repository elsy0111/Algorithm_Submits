import io
import sys

_INPUT = """\
level
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
s = list(input())

if s == list(reversed(s)):
    print("Yes")
else:
    print("No")