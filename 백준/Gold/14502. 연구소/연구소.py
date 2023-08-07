import copy
from collections import deque


def bfs():
    global max_zero_count
    this_map = copy.deepcopy(origin_map)
    this_zero_count = zero_count - 3  # 벽 세워짐
    q = deque()
    for i in range(x):
        for j in range(y):
            if this_map[i][j] == 2:
                q.append([i, j])
    while q:
        virus_index = q.popleft()
        for move in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 상하좌우 이동
            next_index = [virus_index[0] + move[0], virus_index[1] + move[1]]
            # print([next_index[0], next_index[1]])
            if (0 <= next_index[0] < x) and (0 <= next_index[1] < y):  # map 안의 공간이라면
                if (this_map[next_index[0]][next_index[1]] == 0):  # 감염 가능한 공간이라면
                    this_map[next_index[0]][next_index[1]] = 2
                    q.append(next_index)
                    this_zero_count -= 1
    if max_zero_count < this_zero_count:
        max_zero_count = this_zero_count
    return


def create_wall(wall_count):
    if wall_count == 3:
        bfs()
        return
    for i in range(x):
        for j in range(y):
            if origin_map[i][j] == 0:
                origin_map[i][j] = 1
                create_wall(wall_count + 1)  # 해당 위치가 벽일때, 다음 벽 찾기
                origin_map[i][j] = 0  # 원상복구
    return


if __name__ == "__main__":
    x, y = map(int, input().split())
    origin_map = []
    zero_count = 0
    max_zero_count = 0
    for i in range(x):
        line = list(map(int, input().split()))
        origin_map.append(line)
        zero_count += line.count(0)
    create_wall(0)
    print(max_zero_count)