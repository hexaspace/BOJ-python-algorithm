min_num = int(input())
max_num = int(input())
sosu_list=[]
for num in range(min_num, max_num+1):
    is_sosu = True
    if(num == 1):
        continue
    for div in range(2, num):
        if(num % div == 0):
            is_sosu = False
            break
    if(is_sosu):
        sosu_list.append(num)
if(len(sosu_list) == 0):
    print('-1')
else:
    print(sum(sosu_list))
    print(sosu_list[0])