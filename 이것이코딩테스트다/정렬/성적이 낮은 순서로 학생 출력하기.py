n = int(input())
array = []
for i in range(n):
    name, score = input().split()
    array.append((name, int(score)))
# def sort_definition(data):
#     return data[1]

# array.sort(key=sort_definition)
array.sort(key = lambda person: person[1])

for person in array:
    print(person[0], end=" ")