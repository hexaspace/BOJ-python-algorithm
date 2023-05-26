import sys
input = sys.stdin.readline

'''
계수정렬
'''
n = int(input())
store_list = list(map(int, input().split()))

arr = [0]*10000001

for s in store_list:
    arr[s] = 1

m = int(input())
customer_list = list(map(int, input().split()))
for c in customer_list:
    if arr[c] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
