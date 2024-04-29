import sys

n = sys.stdin.readline().rstrip()

nums = map(int, sys.stdin.readline().rstrip().split())
m = 0
y = 0

for i in nums:
    m = m + int(i / 60 + 1) * 15
    y = y + int(i / 30 + 1) * 10

if y == m:
    print("Y M", y)
elif y > m:
    print("M", m)
else:
    print("Y", y)