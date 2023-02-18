import math
T =int(input())
for _ in range(T):
    height, width, customer = map(int, input().split())
    xx = math.ceil(customer / height)
    y = customer % height
    if(y == 0):
        y = height
    print(y, end="")
    if(xx // 10 == 0):
        print("0", end="")
    print(xx)