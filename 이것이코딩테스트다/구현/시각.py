
max_h = int(input())
'''
# 0~59 숫자에서, 즉 초에서 3이 등장하는 횟수
s3 = 10 + (6-1)  # 30대 전체 + 각 1의 자리일때 - 겹치는거
# 분까지 3이 등장하는 횟수
m3 = 60 * s3 + (60-s3) * s3  # 분에서 3이 등장하는거 15번 + 나머지 경우에서 초로 등장하는거
# 시에서 3이 등장하는 횟수
# 시에서 3이 등장하는 시간 * 60*60 + 나머지에서 3이 등장할때
result = 0
for i in range(5):
  if(i%10 == 3):  # 1의자리가 3이라면
    result += 60*60
  else:
    result += m3
print(result)
********수식으로 풀려다 실패하고 그냥 답지봄
'''
count = 0
for h in range(max_h+1):
  for m in range(60):
    for s in range(60):
      if('3' in str(h)+str(m)+str(s)):
        count+= 1

print(count)

