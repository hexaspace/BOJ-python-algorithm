n = int(input())
house = list(map(int, input().split()))

house.sort()
middle_index = int((n+0.0001-1)/2)

print(house[middle_index])