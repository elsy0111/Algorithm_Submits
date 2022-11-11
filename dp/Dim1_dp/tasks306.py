import io
import sys

_INPUT = """\
11 6
2 4 6 8 10 12
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
# In
n,m = map(int,input().split())
D = list(map(int,input().split()))

dp = [0 for _ in range(n+2)]        # 0~n+1 dp[-1] = 0
dp[0] = 1
for i in range(1,n+1):
    for j in D:
        dp[i] += dp[max(-1,i-j)]    # dp[i-j] is not exist -> 0

# Out
if dp[n] != 0:
    print("Yes")
else:
    print("No")
