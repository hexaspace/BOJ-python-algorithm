row, col = map(int, input().split())
arr = dict()
for i in range(row):
  row_arr= list(map(int, input().split()))
  row_arr.sort()  # **검색 - min찾으려면 정렬 안하고 min(row_arr)가능
  arr[i] = row_arr[0]  # index 찾기 쉽도록 dictionary로 만듬
min_key = max(arr.keys(), key = lambda x : arr[x])
print(arr)
print(min_key)
