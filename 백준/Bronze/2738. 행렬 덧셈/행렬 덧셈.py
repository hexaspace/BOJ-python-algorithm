row, column = map(int, input().split())
arr1 = []
arr2 = []
for r in range(row):
    r_arr = list(map(int, input().split()))
    arr1.append(r_arr)
    r_arr=[]
for r in range(row):
    r_arr = list(map(int, input().split()))
    arr2.append(r_arr)
    r_arr=[]
for r in range(row):
    for c in range(column):
        print(arr1[r][c]+arr2[r][c], end=" ")
    print("")