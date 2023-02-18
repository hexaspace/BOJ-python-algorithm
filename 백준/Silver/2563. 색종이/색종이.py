t = int(input())
# (0,0)~(99,99)까지 중복되지 않은 개수를 set에 넣어서, set의 크기를 반환해서 넓이를 구할것
# 색종이는 10*10
occupy = set([])
for _ in range(t):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            occupy.add((i,j))
print(len(list(occupy)))