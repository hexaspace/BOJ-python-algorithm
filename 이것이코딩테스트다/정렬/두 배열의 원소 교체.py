n, k = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))

# a에서 최소 정렬로 k개 추출
a_array.sort()
remain_a_array = a_array[k:]
# b에서 최대 정렬로 k개 추출
b_array.sort(reverse=True)
# 두개 합친 리스트 만듬
select_array = a_array[:k] + b_array[:k]
# 그 리스트에서 최대 k개 뽑아서, a나머지랑 합쳐버림
# 왜냐면, a에서 더 큰수가 있다면, 바꿀 필요가 없기 때문
select_array.sort(reverse=True)
result_array = remain_a_array + select_array[:k]
print(result_array)
print(sum(result_array))
