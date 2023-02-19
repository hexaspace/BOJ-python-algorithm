t = int(input())
arr = list()
for enter in range(t):
    age, name = map(str, input().split())
    arr.append([age, name, str(enter)])
arr.sort(key = lambda x: (int(x[0]), int(x[2])))
for i in range(t):
    print(str(arr[i][0]), arr[i][1])