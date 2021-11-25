n, k = map(int, input().split())

scores = list(map(int, input().split()))
scores.insert(0, 0)
print(sum([1 if i >= scores[k] and i > 0 else 0 for i in scores]))
