
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
        for i in range(bomb_size):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print("".join(stack))
