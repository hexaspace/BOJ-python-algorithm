n, k = map(int, input().split())
count = 0
while (n != 1):
    # 나눠질때까지 나누기
    while (n % k == 0):
        n /= k
        count += 1
    # 1빼는 개수
    minus = n % k
    if (minus == n):
        count += (minus - 1)  # 1은 남겨두고 빼기
        break;
    else:
        count += minus
        n -= minus

print(count)