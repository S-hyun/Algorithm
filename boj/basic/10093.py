import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

b = max(A, B)
a = min(A, B)

if a == b or b-a ==1:
    print("0")
else:
    print(b-a-1)
for i in range(a+1, b):
    print(i, end=' ')