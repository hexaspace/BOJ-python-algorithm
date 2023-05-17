from collections import deque

'''
n, m = map(int, input().split())

graph = []

for line in range(n):
    graph.append(list(map(int, input())))

'''
# n=3
# m=3
# graph = [[1,1,0],[0,1,0],[0,1,1]]
n=5
m=6
graph = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

queue = deque([[0,0]])

def check_can_move(x, y):

    if x<0 or y<0 or x>=n or y>=m:
        return False
    if graph[x][y] != 1:    # 미방문노드 = 1, 방문노드 = 2이상, 몬스터 =0
        return False
    print(x,y)
    return True
def bfs(start_node):
    move_count = 0
    # queue.append(start_node)

    while queue:
        this_node = queue.popleft()
        weight = graph[this_node[0]][this_node[1]]
        print("this node ", this_node, weight)
        print(queue)
        if this_node[0] == n-1 and this_node[1] == m-1: # 목적지 도착
            break
        if check_can_move(this_node[0]-1, this_node[1]):
            print("add!")
            queue.append([this_node[0]-1, this_node[1]])    # 큐에 넣기
            graph[this_node[0]-1][this_node[1]] = weight+1    # 거리+1 적기
        if check_can_move(this_node[0]+1, this_node[1]):
            print("add!")
            queue.append([this_node[0]+1, this_node[1]])
            graph[this_node[0]+1][this_node[1]] = weight+1
        if check_can_move(this_node[0], this_node[1]-1):
            print("add!")
            queue.append([this_node[0], this_node[1]-1])
            graph[this_node[0]][this_node[1]-1] = weight+1
        if check_can_move(this_node[0], this_node[1]+1):
            print("add!")
            queue.append([this_node[0], this_node[1]+1])
            graph[this_node[0]][this_node[1]+1] = weight+1
    print(weight)
    return

bfs([0,0])