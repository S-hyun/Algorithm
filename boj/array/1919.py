import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

a_ = a
for i in a_:
    if i in b:
        a = a.replace(i, '', 1)
        b = b.replace(i, '', 1)

print(len(a)+len(b))