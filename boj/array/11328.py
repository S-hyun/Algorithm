import sys

count = int(sys.stdin.readline().rstrip())

for i in range(count):
    a, b = sys.stdin.readline().rstrip().split()

    possible = 1
    for i in a:
        if i in b:
            b = b.replace(i, '', 1)
        else:
            possible = 0
            break

    if possible==1 and b == "":
        print("Possible")
    else:
        print("Impossible")
