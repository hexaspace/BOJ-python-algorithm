T = int(input())

for _ in range(T):
    floor= int(input())
    room = int(input())
    # 2층 = 1    4=1+3 10=4+5 20=10+10 35=20+15
    # 1층 = 1    3    6    10    15
    # 0층 = 1    2    3    4    5
    before_floor = [i+1 for i in range(room)]    # 0층부터 시작
    for f in range(1, floor+1):    # 1층부터 시작, floor는 0부터 센다 floor+1
        this_floor = [1]    # 1번째 룸은 항상 1
        for r in range(1, room):    # 2룸부터 시작
            this_floor.append(this_floor[r-1]+before_floor[r])
        before_floor = this_floor
    print(this_floor[room-1])
            