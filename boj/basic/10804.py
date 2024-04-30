import sys

nums = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    nums_a = nums[:a-1]
    nums_b = nums[a-1:b][::-1]
    nums_c = nums[b:]

    nums = nums_a + nums_b + nums_c

for j in nums:
    print(j, end=" ")
