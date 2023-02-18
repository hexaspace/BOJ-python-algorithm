import math
arr = list()
for i in range(5):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/5))
print(arr[2])