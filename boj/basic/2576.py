import sys
nums = []
for i in range(7):
    num = sys.stdin.readline().rstrip()
    num = int(num)
    if num%2 == 1:
        nums.append(num)

if nums:
    print(sum(nums))
    print(min(nums))
else:
    print("-1")