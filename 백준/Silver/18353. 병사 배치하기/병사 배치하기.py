 # 전투력 개수, 해당 전투력에서 가장 많은 인원

n = int(input())
input_arr = list(map(int, input().split()))
count_dp = [1]*n   
for i in range(n):
    for j in range(i):
        if input_arr[j] > input_arr[i]:
            count_dp[i] = max(count_dp[i], count_dp[j]+1)
print(n-max(count_dp))
        