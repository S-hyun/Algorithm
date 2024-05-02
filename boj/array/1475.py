import sys
import math
number = int(sys.stdin.readline().rstrip())


number_list = [0]*10

for i in str(number):
    if i == "9":
        number_list[int("6")] += 1
    else:
        number_list[int(i)] += 1

number_list[6] = math.ceil(number_list[6]/2)


print(max(number_list))