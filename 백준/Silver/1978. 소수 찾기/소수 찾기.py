t = int(input())
num_list = list(map(int, input().split()))
sosu_count = 0
for num in num_list:
    is_sosu = True
    if(num == 1):
        continue
    for div in range(2, num):
        if(num % div == 0):
            is_sosu = False
            break
    if(is_sosu):
        sosu_count += 1
print(sosu_count)