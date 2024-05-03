import sys

num = int(sys.stdin.readline().rstrip())

for i in range(num):
    command = sys.stdin.readline().rstrip()
    str1 = []
    str2 = []
    for i in command:
        if i == "-":
            if str1:
                str1.pop()
        elif i == "<":
            if str1:
                str2.append(str1.pop())
        elif i == ">":
            if str2:
                str1.append(str2.pop())
        else:
            str1.append(i)

    str1.extend(reversed(str2))
    print(''.join(str1))
