import sys

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    for __ in range(_+1):
        print('*', end='')
    for __ in range(n-_, 1, -1):
        print(' ', end='')
    for __ in range(n-_, 1, -1):
        print(' ', end='')
    for __ in range(_+1):
        print('*', end='')
    print()
for _ in range(n):
    for __ in range(n-_, 1, -1):
        print('*', end='')
    for __ in range(_+1):
        print(' ', end='')
    for __ in range(_+1):
        print(' ', end='')
    for __ in range(n-_, 1, -1):
        print('*', end='')
    print()