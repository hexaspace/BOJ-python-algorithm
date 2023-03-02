import copy
def rotation(key):
    m = len(key)
    result = [[0]*m for _ in range(m)]
    for x in range(m):
        for y in range(m):
            # print(y, m-x-1)
            tmp = key[x][y]
            result[y][m-x-1] = tmp
            # print(tmp)
    return result
def check_open(background, m, n):
    for x in range(n):
        for y in range(n):
            if(background[m-1+x][m-1+y] != 1):
                # print(m-1+x, m-1+y)
                return False
    return True
def print_arr(back):
    for b in back:
        print(b)
    print("----------")
def solution(key, lock):
    answer = False
    # 자물쇠가 항상 더 크다.
    # 키가 넘어가도되니까, 전체 배열을 m-1 + n + m-1으로 한다
    n = len(lock)
    m = len(key)
    back_size =  n+ m*2 -2
    background = [[0] * back_size for _ in range(back_size) ]
    
    for x in range(n):
        for y in range(n):
            background[x+m-1][y+m-1] = lock[x][y]
    for i in range(back_size-m+1):
        for j in range(back_size-m+1):
            # 여기가 키의 시작점
            # 4방향으로 회전한 키를 더해야함.
            for r in range(4):
                temp_background =  copy.deepcopy(background)
                for kx in range(m):
                    for ky in range(m):
                        temp_background[i+kx][j+ky] += key[kx][ky]
                # print_arr(temp_background)
                if(check_open(temp_background, m, n)):
                    # print("성공")
                    return True
                key = rotation(key) # 실패시 회전
    # 지금까지 성공한게 없으면 초기값 실패 반환
    return answer