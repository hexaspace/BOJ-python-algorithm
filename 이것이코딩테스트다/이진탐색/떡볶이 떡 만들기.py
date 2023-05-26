import sys
input = sys.stdin.readline


def binary_search(arr, item, start, end):
    if start > end:
        return False
    mid = (start+end) // 2
    remain_sum = 0
    # 잘린거 합하기
    for size in arr:
        if size > mid:
            remain_sum += (size - mid)

    if remain_sum == item:
        return mid
    elif remain_sum > item:
        return binary_search(arr, item, mid+1, end)
    else:
        return binary_search(arr, item, start, mid-1)

n, m = map(int, input().split())
rice_cake_list = list(map(int, input().split()))

# 잘릴 기준 사이즈를 start, mid, end이다
start = 0
end = max(rice_cake_list)

result = binary_search(rice_cake_list, m, start, end)
if result != False:
    print(result)