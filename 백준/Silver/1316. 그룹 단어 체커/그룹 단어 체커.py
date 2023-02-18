T = int(input())
group_count = 0
for _ in range(T):
    word = input()
    found_alpha = set([])
    is_pass = True
    last_alpha = ""
    for alpha in word:
        if(alpha in found_alpha and alpha != last_alpha):
            is_pass = False
            break
        else:
            found_alpha.add(alpha)
            last_alpha = alpha
    if(is_pass):
        group_count += 1
print(group_count)
        