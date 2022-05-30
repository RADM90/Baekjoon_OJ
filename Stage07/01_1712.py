fixed, variable, price = list(map(int, input().split()))

cost_gap = price - variable
count = 1
if cost_gap <= 0:
    count = -1
else:
    count += fixed // cost_gap

print(count)