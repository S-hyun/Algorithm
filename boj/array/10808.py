import sys

word = sys.stdin.readline().rstrip()

abc = [0 for i in range(26)]

for i in word:
    abc[ord(i)-97] = abc[ord(i)-97] + 1

for i in abc:
    print(i, end=' ')