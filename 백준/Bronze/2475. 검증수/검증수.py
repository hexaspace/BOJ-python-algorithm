serial = list(map(int, input().split()))
double = [i**2 for i in serial]
print(sum(double)%10)