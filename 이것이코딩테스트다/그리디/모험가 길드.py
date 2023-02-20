
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
groub_count = 0
while(len(arr)>0):
  # 남은사람중 가장 공포높은사람
  max = arr[0]
  if(max > len(arr)):
    break
  arr= arr[max:]  # 앞에 자름
  groub_count += 1

print(groub_count)