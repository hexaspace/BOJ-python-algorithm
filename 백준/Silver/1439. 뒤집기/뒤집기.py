sent = input().strip()
reverse = 0
last = sent[0]    # *** 처음엔 뒤집는게 아니라
# 바뀌는 개수 세기
for i in sent:
    if(last != i):
        last = i
        reverse += 1
# ababa = 4, 맨 앞뒤가 같은숫자면 짝수번 바뀌고, 중앙부터 뒤집으면 절반(2)만 뒤집늗다
# ababab = 5, 다른숫자면 홀수번바뀌고 , 중앙부터 뒤집으면 int(5/2)+1만큼 뒤집는다
print(round(reverse/2+0.000001))