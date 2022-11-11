import io
import sys

_INPUT = """\
5
180 186 189 191 218

"""

sys.stdin = io.StringIO(_INPUT)

#================================

N = int(input())
A = list(map(int,input().split()))
# a,b = map(int,input().split())

if N > 8:
    A = A[:8]
