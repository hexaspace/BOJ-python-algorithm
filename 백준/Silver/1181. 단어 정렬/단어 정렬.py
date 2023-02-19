t = int(input())
# 중복된 단어는 한개만 - set이용
arr = set()
for _ in range(t):
    arr.add(input().rstrip())
list_arr = list(arr)
list_arr.sort(key = lambda x: (len(x), x))

for i in list_arr:
    print(i)