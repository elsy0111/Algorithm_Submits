import io
import sys

_INPUT = """\
1
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = dp[1-1]
if n >= 2:
    dp[2] = dp[2-1] + dp[2-2]
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
print(dp[n])