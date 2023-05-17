from collections import deque
# 스택
print("자료구조 스택")
stack = []
stack.append(1)
stack.append(2)
stack.pop()
print(stack)

#자료구조 큐
print("자료구조 큐")

queue = deque()

queue.append(3)
queue.append(4)
queue.append(5)
queue.append(6)
queue.popleft()
print(queue)
queue.reverse()

print(list(queue))

