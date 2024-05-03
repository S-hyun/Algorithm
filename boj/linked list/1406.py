import sys

first_strings = list(sys.stdin.readline().rstrip())
edited_strings = []


num = int(sys.stdin.readline().rstrip())

for i in range(num):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "L":
        if first_strings:
            edited_strings.append(first_strings.pop())
    elif command[0] == "D":
        if edited_strings:
            first_strings.append(edited_strings.pop())
    elif command[0] == "B":
        if first_strings:
            first_strings.pop()
    else:
        first_strings.append(command[1])
first_strings.extend(reversed(edited_strings))
print(''.join(first_strings))
