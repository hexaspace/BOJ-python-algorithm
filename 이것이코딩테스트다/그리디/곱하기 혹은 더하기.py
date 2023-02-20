
str_arr = input().strip()
arr = list(map(int, str_arr))
result = arr[0]
for i in range(1, len(arr)):
  if(result <= 1 or arr[i] <= 1):  # 두 수 모두가 0, 1 일때 더하는거임*******
    result += arr[i]
  else:
    result *= arr[i]
print(result)