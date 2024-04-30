import sys
nums = []
for i in range(9):
    nums.append(int(sys.stdin.readline().rstrip().rstrip()))

num_max = max(nums)
print(num_max)
print(nums.index(num_max)+1)