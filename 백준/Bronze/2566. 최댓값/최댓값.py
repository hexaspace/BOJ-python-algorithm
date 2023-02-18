last_max = -1
max_row = -1
max_column = -1
for row in range(1,10):
    line_list = list(map(int, input().split()))
    curr_max = max(line_list)
    if(last_max < curr_max):
        column = line_list.index(curr_max)+1
        max_row = row
        max_column = column
        last_max = curr_max
print(last_max)
print(max_row, max_column)