n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

for query in arr:
    score = 0
    streak = 0
    for boool in query:
        if boool != 'X':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)