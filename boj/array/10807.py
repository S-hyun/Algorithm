import sys

count = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

x = int(sys.stdin.readline().rstrip())

print(numbers.count(x))