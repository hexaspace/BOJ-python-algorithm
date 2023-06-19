# 타고타고 가장 조상값을 불러옴. 불러오면서 다 조상값으로 할당해줌.
def find_parent(parent_list, me):
    if parent_list[me] != me:
        return find_parent(parent_list, parent_list[me])
    return me

# 이전 부모값을 갖은 컴을 다 min 부모값으로 초기화해줘야함

def set_parent(parent_list, me, parent_value):
    past_parent = parent_list[me]
    for i in range(len(parent_list)):
        if parent_list[i] == past_parent:
            parent_list[i] = parent_value
    return


# input 
computer_num = int(input())
network_num = int(input())

parent_list = [c for c in range(computer_num+1)]

for i in range(network_num):
    a, b = map(int, input().split())
    a_parent = find_parent(parent_list, a)
    b_parent = find_parent(parent_list, b)
    # 더 작은 값이 부모가 되도록 만든다
    if a_parent < b_parent:
        set_parent(parent_list, b, a_parent)
    elif a_parent > b_parent:
        set_parent(parent_list, a, b_parent)
    # 두 부모가 같으면 바꿀 필요 없음


# 한번 돌면서 1이 조상인 개수 구하기
count = 0
for p in parent_list:
    if p == 1:
        count += 1
# 1번 컴퓨터 뺀 개수
print(count-1)

    
    
    