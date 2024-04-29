import sys
count, comp = sys.stdin.readline().rstrip().split()

nums = sys.stdin.readline().rstrip().split()
nums = [int(i) for i in nums]
for i in range(int(count)):
    if (nums[i] < int(comp)):
        print(nums[i], end= ' ')

