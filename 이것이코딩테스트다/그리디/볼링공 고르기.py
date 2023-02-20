
num, max = map(int, input().split())
arr= list(map(int, input().split()))

count = 0
'''
O(n^2) 방식이라 오래걸림.
arr.sort()
for a in range(num):
  for b in range(a, num):
    if(arr[a] != arr[b]):
      count += 1
print(count)'''
#  ******** 답지보고 O(n)알게됨
weight = [0]*11

# 각 무게별 몇개인지 곱
for a in arr:
  weight[a] += 1

for i in range(1, 11):
  if(weight[i] != 0):
    num -= weight[i]  # 조합이라서, 영영 다시 뽑힐일 없음.
    count += weight[i] * num  # 해당 무게의 공 개수 * 남은 무게들의 공 개수
print(count)