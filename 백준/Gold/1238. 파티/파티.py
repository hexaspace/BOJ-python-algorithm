from heapq import heappush, heappop
import sys
input = sys.stdin.readline
inf = 99999    # 최대 edge값 10,000


def short_route(target, edge_list, distance_list):
    heap = []
    
    heappush(heap, (0, target))
    distance_list[target]=0
    
    while heap:
        distance, this_node = heappop(heap)
        # 기존 저장된게 더 작다면 pass
        if distance_list[this_node] < distance:
            continue
        # 연결 노드들 확인
        for this_edges in edge_list[this_node]:
            next_node = this_edges[0]
            next_weight = this_edges[1]
            connect_weight = distance + next_weight    # edgh ; (end, weight)
            if distance_list[next_node] > connect_weight:
                distance_list[next_node] = connect_weight
                heappush(heap, (connect_weight, next_node))
    return distance_list

# 입력
node_num, edge_num, target = map(int, input().split())

distance_list = [inf]*(node_num+1)
reverse_distance_list = [inf]*(node_num+1)
sum_distance_list = [0]*(node_num+1)
edge_list = [[] for i in range(node_num+1)]
reverse_edge_list = [[] for i in range(node_num+1)]

for e in range(edge_num):
    start, end, weight = map(int, input().split())
    edge_list[start].append((end, weight))
    reverse_edge_list[end].append((start, weight))
    
distance_list = short_route(target, edge_list, distance_list)
reverse_distance_list = short_route(target, reverse_edge_list, reverse_distance_list)


max_distance = 0
for n in range(node_num):
    if max_distance < distance_list[n+1] + reverse_distance_list[n+1]:
        max_distance = distance_list[n+1] + reverse_distance_list[n+1]
print(max_distance)

