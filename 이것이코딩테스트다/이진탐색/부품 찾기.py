import sys
input = sys.stdin.readline

'''
이진탐색
'''

def binary_search(arr, item, start, end):
    if start > end:
        return False
    mid = (start+end) // 2
    if arr[mid] == item:
        return True
    elif arr[mid] < item:
        return binary_search(arr, item, mid+1, end)
    else:
        return binary_search(arr, item, start, mid-1)


n = int(input())
store_list = list(map(int, input().split()))
store_list.sort()

m = int(input())
customer_list = list(map(int, input().split()))

for c in customer_list:
    if (binary_search(store_list, c, 0, n-1) == True):
        print("yes", end=" ")
    else:
        print("no", end=" ")


