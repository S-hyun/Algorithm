import sys, statistics
nums = list()
for i in range(5):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

print(statistics.mean(nums))
print(statistics.median(nums))