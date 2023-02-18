import math
climing, sleep, tree = map(int, input().split())
# tree < (climing - sleep)*(x-1) + climing
day = math.ceil((tree-climing) / (climing-sleep)) +1
# 올림을 하는 예시 :  4올라감 2떨어짐, 나무9, 2*3+4, 5/2 = 2
print(day)