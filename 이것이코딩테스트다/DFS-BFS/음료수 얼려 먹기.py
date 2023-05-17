
n, m = map(int, input().split())
graph = []
for row in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 범위 밖인지 체크
    # print("check ",x,y)
    if(x<0 or y<0 or x>=n or y>=m):
        return False
    if(graph[x][y] == 0):
        # 방문처리 = 1
        graph[x][y] = 1
        # 상하좌우 체크
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

ice_group_count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            ice_group_count += 1
print(ice_group_count)

