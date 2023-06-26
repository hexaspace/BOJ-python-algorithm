import math

        
n_count = int(input())
n_list = list(map(int, input().split()))

right_select = 0
left_select = 0
difference = 100000000000
left_pointer = 0
right_pointer = n_count-1

while left_pointer < right_pointer:
    this_diff = n_list[left_pointer] + n_list[right_pointer]
    if difference >= abs(this_diff):    # diff갱신할 필요 있을때
        left_select = n_list[left_pointer]
        right_select = n_list[right_pointer]
        difference = abs(this_diff)
        
    if this_diff == 0:    # 0 완성
        difference = this_diff
        left_select = n_list[left_pointer]
        right_select = n_list[right_pointer]
        break
    elif this_diff < 0:    # 포인터 이동
        left_pointer +=1
    else:
        right_pointer -=1     



print(left_select, right_select)
        
