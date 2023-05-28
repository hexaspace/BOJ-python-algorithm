    
memory= [0]*12
memory[1] = 1    # 1
memory[2] = 2    # 1+1, 2
memory[3] = 4    # 1+1+1, 1+2, 2+1, 3
for i in range(4, 12):
    case1 = memory[i-1]    # +1
    case2 = memory[i-2]    # +2
    case3 = memory[i-3]    # +3
    memory[i] = case1+case2 + case3

t = int(input())
test_case = []
for i in range(t):
    n = int(input())
    print(memory[n])
    
    