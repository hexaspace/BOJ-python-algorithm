
size, plus_num, sequence = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
second_sum_count = plus_num // (sequence + 1)
first_sum_count = plus_num - second_sum_count
sum = first_sum_count * arr[0]
sum += second_sum_count * arr[1]
print(sum)