import sys
input = sys.stdin.readline

'''
집합
'''
n = int(input())
store_list = set(map(int, input().split()))

m = int(input())
customer_list = list(map(int, input().split()))
for c in customer_list:
    if c in store_list:
        print("yes", end=" ")
    else:
        print("no", end=" ")
