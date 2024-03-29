test_list = []
# 입력
while True:
    input_str = input()
    if input_str[0] == '-':
        break
    test_list.append(input_str)
    
def check_balance(string):    #사용안함
    middle = 0
    for s in string:
        if s == '{':
            middle += 1
        else:
            middle -= 1
        if middle < 0:
            return False
    return True


def turn_balance(string):
    middle = 0
    turn_num=0
    for s in string:
        if s == '{':
            middle += 1
        else:
            middle -= 1
        if middle < 0:
            # 반대방향 { 으로 치환한다고 침
            middle += 2
            turn_num += 1
     
    return turn_num + int(middle/2)   # {가 오버된부분의 개수 middle은, }로 치환하면서 -2씩 빠짐. 그러므로 /2함

# }{
for t in range(len(test_list)):
    over_num = turn_balance(test_list[t])
    print(str(t+1)+". "+str(abs(over_num)))
    