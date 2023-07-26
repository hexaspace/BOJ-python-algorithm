import sys




# 세로 0 가로 1 대각선2,
def check_range(x, y):
    if x >= n or y >= n:
        return False
    if house[x][y] == 1:  # 벽
        return False
    return True


def dfs(x, y, direction):
    global result
    if x == n - 1 and y == n - 1:  # 목적지 도착
        result += 1
        return
    elif direction == 0:    #세로
        # 세로이동
        if check_range(x + 1, y):
            dfs(x + 1, y, 0)
        # 대각
        if check_range(x + 1, y + 1) and check_range(x, y+1) and check_range(x+1, y):
            dfs(x + 1, y + 1, 2)
    elif direction == 1:    #가로
        # 가로이동
        if check_range(x, y + 1):
            dfs(x, y + 1, 1)
        # 대각
        if check_range(x + 1, y + 1) and check_range(x, y+1) and check_range(x+1, y):
            dfs(x + 1, y + 1, 2)
    elif direction == 2:    #대각
        # 세로이동
        if check_range(x + 1, y):
            dfs(x + 1, y, 0)
        # 가로이동
        if check_range(x, y + 1):
            dfs(x, y + 1, 1)
        # 대각
        if check_range(x + 1, y + 1) and check_range(x, y+1) and check_range(x+1, y):
            dfs(x + 1, y + 1, 2)


if __name__ == "__main__": 
    input = sys.stdin.readline
            # 입력
    n = int(input())
    house = []
    for i in range(n):
        this_list = list(map(int, input().split()))
        house.append(this_list)
    result = 0
    # 시작 0,1. 가로
    # x y dir
    if house[n-1][n-1] == 0:  # 최종목표가 벽 아닐때
        dfs(0, 1, 1)
    print(result)





