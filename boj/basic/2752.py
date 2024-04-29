import sys

nums = sys.stdin.readline().rstrip().split()

nums = [int(i) for i in nums]

nums.sort()

for i in nums:
    print(i, end=' ')