import sys
input = sys.stdin.readline
t = int(input())

arr = list(map(int, input().split()))
sorted_unique = list(set(arr))
sorted_unique.sort()
# ****검색, list.index는 O(N)이다. 딕셔너리는 찾는데 시간복잡도 O(1)
dic = {sorted_unique[i] : i for i in range(len(sorted_unique))}
for a in arr:
    print(dic[a], end=" ")
print("")