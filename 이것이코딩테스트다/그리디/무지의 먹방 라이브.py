# 이 코드는 heap을 사용하지 않아서 효율성에서 0점맞은 코드입니다.
def solution(food_times, k):
    answer = 0
    food_num = len(food_times)
    food_index = [i for i in range(food_num)]
    remain_index = 0
    for i in range(k):
        # print(str(i), "번째 ", str(remain_index))
        # print(food_times)
        food_times[remain_index] -= 1
        if (food_times[remain_index] == 0):
            # idx = food_index.index(remain_index)
            del food_times[remain_index]
            del food_index[remain_index]
            # 하나가 사라져서, remain_index가 제자리가 되어야함
            remain_index -= 1
            food_num -= 1
            print("사라짐")
            if (food_num == 0):  # 남은음식 없음
                break
        # 다음 음식으로 넘어가기
        remain_index += 1
        remain_index = remain_index % food_num
    # 다음 인덱스의 food_index 원래 순서를 구하기
    if (food_num == 0):
        answer = -1
    else:
        answer = food_index[remain_index] + 1

    return answer