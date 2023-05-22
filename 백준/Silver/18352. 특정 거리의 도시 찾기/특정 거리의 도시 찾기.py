from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
# 인접 리스트 저장
graph = [[] for _ in range(n+1)]    # 0번 도시는 없어서 1부터 시작해서 n까지 담음
inf = 9999999
weight = [inf for _ in range(n+1)]
for edge in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

queue = deque([x])
weight[x] = 0


def bfs(k):
    while queue:
        this_node = queue.popleft()
        this_weight = weight[this_node]
        if(this_weight > k):
            break    # 목표 거리까지 가능한 도시는 bfs로 다 얻음
        next_weight = this_weight +1
        this_edges = graph[this_node]
        for target in this_edges:
            if weight[target] == inf:
                weight[target] = next_weight
                queue.append(target)    # 다음에 뻗을 곳
            else:
                continue    # 이미 최단거리 할당됨
                
# bfs 돌리기
bfs(k)

# 목표 거리인 도시만 출력
is_success = 0
for city in range(1, n+1):
    if weight[city] == k:
        print(city)
        is_success = 1
if is_success == 0:
    print(-1)
