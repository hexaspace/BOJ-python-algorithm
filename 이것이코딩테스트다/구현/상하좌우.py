
def out_of_range(size, x, y):
  if(x<=0 or x>size or y<=0 or y>size):
    return True
  return False

size = int(input())
dir_arr = list(map(str, input().split()))
dir_cal = dict({"R":(0,1), "L":(0, -1), "U":(-1, 0), "D":(1, 0)})
pos = (1,1)
for i in dir_arr:
  if(out_of_range(size, pos[0]+dir_cal[i][0], pos[1]+dir_cal[i][1])):
    continue
  pos = (pos[0]+dir_cal[i][0], pos[1]+dir_cal[i][1])
print(pos[0], pos[1])