student, reward = map(int, input().split())


scores = list(map(int, input().split()))
scores.sort()
print(scores[-reward])