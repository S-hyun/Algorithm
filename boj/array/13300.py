import sys
import math

max_s, max_r = map(int, sys.stdin.readline().rstrip().split())

sex_grade = [0]*12

for i in range(max_s):
    sex, grade = map(int, sys.stdin.readline().rstrip().split())
    if sex == 0 and grade == 1:
        sex_grade[0] = sex_grade[0] + 1
    elif sex == 1 and grade == 1:
        sex_grade[1] = sex_grade[1] + 1
    elif sex == 0 and grade == 2:
        sex_grade[2] = sex_grade[2] + 1
    elif sex == 1 and grade == 2:
        sex_grade[3] = sex_grade[3] + 1
    elif sex == 0 and grade == 3:
        sex_grade[4] = sex_grade[4] + 1
    elif sex == 1 and grade == 3:
        sex_grade[5] = sex_grade[5] + 1
    elif sex == 0 and grade == 4:
        sex_grade[6] = sex_grade[6] + 1
    elif sex == 1 and grade == 4:
        sex_grade[7] = sex_grade[7] + 1
    elif sex == 0 and grade == 5:
        sex_grade[8] = sex_grade[8] + 1
    elif sex == 1 and grade == 5:
        sex_grade[9] = sex_grade[9] + 1
    elif sex == 0 and grade == 6:
        sex_grade[10] = sex_grade[10] + 1
    else:
        sex_grade[11] = sex_grade[11] + 1

for i in range(len(sex_grade)):
    sex_grade[i] = math.ceil(sex_grade[i]/max_r)

print(sum(sex_grade))
