# 1, 2~3, 4~6, 7~10, 계차수열 1,3,6,10,15, 차이가 등차수열 12345
num = int(input())    # 분수숫자
sum_line = 1    # 앞뒤 숫자를 합쳤을때 값 
while(num >0):
    num -= sum_line
    sum_line += 1
a = -num+1    # 1, 3, 6 ,10에 해당하는 범위의 마지막 숫자가 1이됨.
b = sum_line-a    

if(sum_line%2 == 0):    # 위에서 아래로, 
    print(str(a)+"/"+str(b))
else:
    print(str(b)+"/"+str(a))