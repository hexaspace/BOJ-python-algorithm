n = int(input())

triangle = []
for i in range(n):
    this_input = list(map(int, input().split()))
    triangle.append(this_input)
for i in range(n-1, 0, -1):    # root는 하지 않는다.
    for j in range(i):    # j와 j+1을 비교해야해서 i-1까지 센다
        win = max(triangle[i][j], triangle[i][j+1])
        triangle[i-1][j] += win
print(triangle[0][0])