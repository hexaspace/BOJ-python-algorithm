from heapq import heappush, heappop
heap = []
n = int(input())
for i in range(n):
    heappush(heap, int(input()))
sum_count = 0
while len(heap)>1:
    # 합칠 두 묶음 추출
    a = heappop(heap)
    b = heappop(heap)    
    this_count = a+b
    # 전체 카운트에 더하기
    sum_count += this_count
    # 묶여진 묶음을 다시 리스트에 추가
    heappush(heap, this_count)

print(sum_count)
    