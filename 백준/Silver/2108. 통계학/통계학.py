import math
import sys
input = sys.stdin.readline

t = int(input())
arr = list()
for _ in range(t):
    arr.append(int(input()))
arr.sort()
# 최빈값 구하기
count_max = 0
max_value = 4444    # 입력값이 불가능한 절대값 4000을 넘는 특정수로 결정
count_this = 0
last_value = 4444
second_count_flag = 4444    # 두번째 최빈값을 저장
for a in arr:
    if(a == last_value):    # 같은 값을 계속 셀때
        count_this += 1
    else:    # 새로운 값으로 넘어갔을때
        if(count_this > count_max):
            count_max = count_this
            max_value = last_value    # 이전 값을 max로 저장
            # 초기화
            second_count_flag = 4444
        elif(count_this == count_max and second_count_flag == 4444):    # 같은 최빈 최초 두번째
            second_count_flag = last_value
            max_value = last_value
        #  현재 값 저장, 세기 시작
        count_this = 1
        last_value = a
# 마지막 value의 카운트 비교
if(count_this > count_max):
    count_max = count_this
    max_value = last_value    # 이전 값을 max로 저장
elif(count_this == count_max and second_count_flag == 4444):    # 같은 최빈 최초 두번째
    second_count_flag = last_value
    max_value = last_value
print(round((sum(arr)/t)+0.0001))    # 산술평균
print(arr[int(t/2)])    #중앙값
print(max_value)    #최빈값
print(abs(arr[-1]-arr[0]))    # 범위