import math
class_count = int(input())
class_people_list = list(map(int, input().split()))
b_control_count, c_control_count = map(int, input().split())
controller_count = 0
for i in range(class_count):
    remain_people = class_people_list[i] - b_control_count
    if remain_people > 0:
        controller_count += math.ceil(remain_people/c_control_count) +1
    else:
        controller_count += 1
print(controller_count)