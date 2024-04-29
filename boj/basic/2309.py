import sys
nums = list()

for i in range(9):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

nums.sort()

for i in range(1, 9):
    for j in range(0, i):
        if (sum(nums) - nums[i] - nums[j] == 100):
            nums.remove(nums[i])
            nums.remove(nums[j])

            for k in nums:
                print(k)
            exit()

