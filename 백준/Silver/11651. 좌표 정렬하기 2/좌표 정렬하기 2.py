t = int(input())
arr = []
for _ in range(t):
    x, y = map(int, input().split())
    arr.append([x,y])
arr.sort(key=lambda x: (x[1],x[0]))
for i in range(t):   
    print(arr[i][0], arr[i][1])