n = int(input())

direct_target_list = [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8]]
# 0~9 숫자에서 바로 다음으로 갈수있는 숫자
stairs_list = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]  # 자리수 2일때, 0~9로 시작할때 각 개수, ex) 01, 10, 12, 21, 23....
# 30분 풀고 찾아봄~~~
mod = 1000000000
# dp 동적 프로그래밍
# 비트 연산자를 사용해서 1111111111(=1023)일때 10개의 숫자를 다 쓴것이다.
# 이외에 작은 자리수부터 하나씩 증가시켜서, 이전 값에서 합산하는건 30분동안 내가 생각했던거랑 같다

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n)]
for i in range(10):
    bit = 1 << i
    dp[0][i][bit] = 1
for ni in range( n-1):
    for start_num in range(10):
        for direct_next_num in direct_target_list[start_num]:
            # 다음 숫자로 넘어갈수 있는 값: direct target
            for used_bit in range(1024):
                next_bit = used_bit | (1 << direct_next_num)
                if dp[ni][start_num][used_bit] > 0:
                    dp[ni + 1][direct_next_num][next_bit] += dp[ni][start_num][used_bit]
                    dp[ni + 1][direct_next_num][next_bit] %= mod

result = 0
for s in range(1, 10):
    result += dp[n - 1][s][1023]

print(result % mod)


