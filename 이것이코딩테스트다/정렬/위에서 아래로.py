n = int(input())
input_array = []
for i in range(n):
    input_value = int(input())
    input_array.append(input_value)
# 정렬
input_array.sort(reverse=True)

for i in input_array:
    print(i, end=" ")