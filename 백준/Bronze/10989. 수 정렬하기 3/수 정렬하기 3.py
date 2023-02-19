import sys
input = sys.stdin.readline
t = int(input())

index_list = [0]*10000
for _ in range(t):
    a = int(input())
    # 개수세기 -검색 입력받으면서 바로 list에 넣어두기
    index_list[a-1] += 1
# 검색 - 누적개수 만들지 말고 그냥 바로 한번씩 돌면서 출력
for i in range(10000):
    if(index_list[i] != 0):    # 0이 아닌거 발견시
        for count in range(index_list[i]):    # 카운트 한만큼 출력
            print(i+1)
    