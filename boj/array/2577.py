import sys

numbers = []
for i in range(3):
    numbers.append(int(sys.stdin.readline().rstrip()))

number = numbers[0]*numbers[1]*numbers[2]

number_list = [0]*10

for i in str(number):
    number_list[int(i)] += 1

for i in number_list:
    print(i)