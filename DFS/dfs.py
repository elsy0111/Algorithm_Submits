import io
import sys

_INPUT = """\
12 15
X X _ _ _ _ _ _ _ _ _ _ _ _ _
X _ _ X _ _ _ _ _ _ _ _ _ _ _
X _ _ X _ _ _ _ _ _ _ _ _ _ _
X _ X X X X X _ _ _ _ X _ _ _
_ _ _ X _ _ _ _ _ _ _ X _ _ _
_ _ _ X X X X _ _ _ X X X _ _
_ X _ X _ _ _ _ _ _ _ X X _ _
X X _ X _ _ _ _ _ _ _ _ _ _ _
_ X _ X _ _ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _ X X X X X
_ _ _ _ _ _ _ _ _ _ _ _ X _ _
_ _ _ _ _ _ _ _ _ _ _ _ X _ _

"""

sys.stdin = io.StringIO(_INPUT)

#------------------------------------
from time import sleep
H,W = map(int,input().split())
A = []
cnt = 0

for _ in range(H):
    A.append(list(input().split()))

def print_arr(Arr):
    global ans
    global cnt
    cnt += 1
    print("cnt :",cnt)
    print("ans :",ans)
    print(" /",end = " ")
    for i in range(len(Arr[0])):
        if i+1 >= 10:
            print(i,end = "")
        else:
            print(i,end = " ")
    print()
    for i,a in enumerate(Arr):
        if i >= 10:
            print(i,end = " ")
        else:
            print(" " + str(i),end = " ")
        for ai in a:
            print(ai,end = " ")
        print()
    print()
    print("-----------------------------")
    print()

direc = [[0,1],[1,0],[0,-1],[-1,0]]
max_ans = 0

def dfs(i,j):
    global ans
    A[i][j] = "O"
    print_arr(A)
    sleep(.5)
    for d in direc:
        if i + d[0] < 0 or i + d[0] >= H or j + d[1] < 0 or j + d[1] >= W:
            continue
        else:
            if A[i + d[0]][j + d[1]] == "X":
                ans += 1
                dfs(i + d[0],j + d[1])
for i in range(H):
    for j in range(W):
        if A[i][j] == "X":
            ans = 1
            dfs(i,j)
            max_ans = max(max_ans,ans)
print(max_ans)