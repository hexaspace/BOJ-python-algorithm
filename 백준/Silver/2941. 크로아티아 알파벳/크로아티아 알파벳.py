# replace를 사용하는 방법
sent = input().rstrip()
cro = ['c=','c-','dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in cro:
    sent = sent.replace(c, '#')

print(len(sent))