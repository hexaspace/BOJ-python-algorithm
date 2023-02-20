
def meet_range(x):
  x = int(x)
  if(x == 1 or (9-x) == 1):
    return 0
  elif(x == 2 or (9-x) == 2):
    return 1
  else:
    return 3

pos_chess = input().strip()
min_count = 2
alpha_list = ['a','b','c','d','e','f','g','h']
count = min_count
count += meet_range(alpha_list.index(pos_chess[0])+1)
count+= meet_range(pos_chess[1])
print(count)