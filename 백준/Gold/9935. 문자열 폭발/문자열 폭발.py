data = input()
bomb = input()
bomb_list = []
for b in bomb:
    bomb_list.append(b)
bomb_size = len(bomb)
stack = []

for d in data:
    stack.append(d)
    if stack[-bomb_size:] == bomb_list:
        del stack[-bomb_size:]
        # for문 안에서 pop 하는것도 통과

if len(stack) == 0:
    print('FRULA')
else:
    print("".join(stack))
