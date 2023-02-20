import heapq
def solution(food_times, k):
    answer = 0
    if(sum(food_times) <= k):   # 다먹어도 시간 남음
        return -1
    h = []
    food_num = len(food_times)
    for f in range(food_num):
        heapq.heappush(h, (food_times[f], f+1)) # dish번호랑 시간이랑 같이 넣어줌
    eat_cycle_time = 0
    while (len(h)>0):
        # 가장 작은 음식을 다 먹어야함.
        min_data = heapq.heappop(h)
        min_time = min_data[0]-eat_cycle_time   # 저장된 시간 - 이전에 회전시킨 개수
        if(min_time * (len(h)+1) > k):  # 다먹을 시간이 남은시간보다 크면 그만 먹음
            #print("더 못먹음")
            break
        # 추가로 비운시간만큼 바퀴 돌린거임.
        eat_cycle_time += min_time
        k -= min_time * (len(h)+1)  # 시간이 흐름
        #print("남은시간", k)
    # 남은 음식들은 1부터 순서대로 처리, 나머지를 사용
    # 그전에, 빠진 마지막값을 넣어줘야함...
    h.append(min_data)
    #print(h)
    h.sort(key = lambda x : x[1])   # dish 번호순으로 정렬
    answer = h[k%len(h)][1]
    
    return answer