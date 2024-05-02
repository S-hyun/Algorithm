import sys

count = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

sum = int(sys.stdin.readline().rstrip())

numbers.sort()

dap = 0

start = 0
end = count-1

while start < end:
    hap = numbers[start] + numbers[end]

    if hap == sum:
        dap = dap + 1
        start = start + 1
    elif hap > sum:
        end = end - 1
    else:
        start = start + 1

print(dap)