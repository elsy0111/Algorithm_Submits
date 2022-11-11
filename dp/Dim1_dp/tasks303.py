import io
import sys

_INPUT = """\
8
3 1 4 1 5 9 2 6
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
A = list(map(int,input().split()))
dp = [[] for i in range(n)]
dp[0] = 0
dp[1] = dp[0] + A[1]
for i in range(2,n):
    dp[i] = min(dp[i-1] + A[i],dp[i-2] + 2 * A[i])
print(dp[n-1])