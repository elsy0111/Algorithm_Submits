import io
import sys

_INPUT = """\
15
"""

sys.stdin = io.StringIO(_INPUT)

#-------------------------------------
n = int(input())
for i in range(1,n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)