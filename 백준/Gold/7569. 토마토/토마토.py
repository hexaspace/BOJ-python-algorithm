box = []
n = 0
m = 0
h = 0
def check_change(z,x,y):
    if z < 0 or z >= h or x < 0 or x >=n or y < 0 or y >= m:    # 범위밖
        return False
    if box[z][x][y] == 0:   # 변화가능
        box[z][x][y] = 1    # 익힘
        return True
    return False
def day_after(success_tomato):
    global box
    next_success_tomato = []    # 새롭게 익은 것들만

    for s in range(len(success_tomato)):
        for near in [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]:
            if check_change(success_tomato[s][0]+near[0],success_tomato[s][1]+near[1],success_tomato[s][2]+near[2]):
                next_success_tomato.append([success_tomato[s][0]+near[0],success_tomato[s][1]+near[1],success_tomato[s][2]+near[2]])
    return next_success_tomato


if __name__ == "__main__":
    box = []
    m, n, h = map(int, input().split())

    count = [0, 0, 0]  # [없음-1,안익음0,익음1]

    success_tomato = []
    for k in range(h):

        this_floor = []
        for i in range(n):
            this_line = list(map(int, input().split()))
            this_floor.append(this_line)
            count[1] += this_line.count(0)  # 안익은 개수 저장
            for j in range(m):
                if this_line[j] == 1:
                    success_tomato.append([k, i, j])  # 익은 토마토 위치저장
                    count[2] += 1  # 익은 개수 저장
        box.append(this_floor)
    count[0] = (m * n * h) - count[1] - count[2]


    day = 0

    while len(success_tomato) != 0:
        next_success_tomato = day_after(success_tomato)
        new_success_count = len(next_success_tomato)
        if new_success_count == 0 :   # 더이상 갱신없음
            break
            # break해서 나가고, 안익은거 있으면 -1출력
        else:
            count[1] -= new_success_count
            count[2] += new_success_count
        success_tomato = next_success_tomato
        day += 1

    if count[1] > 0:
        print(-1)
    else:
        print(day)