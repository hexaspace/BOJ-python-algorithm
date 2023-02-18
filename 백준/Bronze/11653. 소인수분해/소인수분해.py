num = int(input())
div_list = []
if(num != 1):
    for div in range(2, num+1):
        while(num % div == 0):
            num = num/div
            div_list.append(div)
    for i in div_list:
        print(i)