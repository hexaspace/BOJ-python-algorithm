n = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
result_list = []
def dfs(index, operator, middle_result):
    global result_list
    if index == n:    # 연산 끝
        result_list.append(middle_result)
        return 
    for oper in range(4):
        if operator[oper] >0:    # 해당 연산자가 남아있다면
            operator_copy = operator.copy()
            next_index = index+1
            operator_copy[oper] -= 1    #연산자 하나 씀
            if oper == 0:
                middle_result_copy = middle_result + num_list[index]
            elif oper == 1:
                middle_result_copy = middle_result - num_list[index]
            elif oper == 2:
                middle_result_copy = middle_result * num_list[index]
            elif oper == 3:
                middle_result_copy = int(middle_result / num_list[index])
            
            dfs(next_index, operator_copy, middle_result_copy)
    return
dfs(1, operator, num_list[0])


print(max(result_list))
print(min(result_list))
