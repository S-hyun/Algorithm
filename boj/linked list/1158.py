import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

arr = [i for i in range(1, n+1)]
re = 0
dap = []

for i in range(n):
    re = re + k - 1
    if re >= len(arr):
        re = re%len(arr)

    dap.append(str(arr.pop(re)))
print('<' + ", ".join(dap) + '>')