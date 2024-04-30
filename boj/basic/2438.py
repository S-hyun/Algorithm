import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    for __ in range(_+1):
        print('*', end='')
    print()