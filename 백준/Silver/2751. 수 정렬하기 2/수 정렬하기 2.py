import sys
input = sys.stdin.readline
t = int(input())

# heap으로 풀기 - 시간초과
heap = []
for _ in range(t):
    heap.append(int(input()))

for i in sorted(heap):
    print(i)
