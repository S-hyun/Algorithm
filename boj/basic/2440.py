import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    for __ in range(n-_, 0, -1):
        print('*', end='')
    print()