str_nums = input().strip()
list_nums = list(map(int, str_nums))
list_nums.sort(reverse = True)

for i in list_nums:
    print(i, end="")
    
print("")