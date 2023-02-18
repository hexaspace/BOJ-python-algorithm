score = input().strip()
zero = ['D','C','B','A']
if(score == 'F'):
    score_num = 0.0
else:
    score_num = zero.index(score[0]) + 1
    if(score[1] == '+'):
        score_num += 0.3
    elif(score[1] == '-'):
        score_num -= 0.3
print("{:.1f}".format(score_num))