n = int(input())
classroom = []
for _ in range(n):
    classroom.append(list(map(str, input().split())))
    
def sort_person(data):
    return -int(data[1]), int(data[2]), -int(data[3]), data[0]
classroom.sort(key=sort_person)
for i in range(n):
    print(classroom[i][0])