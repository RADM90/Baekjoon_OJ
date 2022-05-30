n = int(input())
scores = list(map(float, input().split()))
new_arr = []
for score in scores:
    new_arr.append(score * 100 / max(scores))
print(sum(new_arr)/len(new_arr))
