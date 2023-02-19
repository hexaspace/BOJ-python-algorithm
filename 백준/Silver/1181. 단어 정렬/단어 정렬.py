t = int(input())
# 중복된 단어는 한개만 - set이용
# list 후에 set을 하는거랑, set을 받고 list로 출력하는거랑 차이가 뭐....아!
# setㅇ은 순서가 없다!
arr = set()
for _ in range(t):
    arr.add(input().rstrip())
list_arr = list(arr)
list_arr.sort(key = lambda x: (len(x), x))

for i in list_arr:
    print(i)