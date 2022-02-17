first, second, third = list(map(int, input().split()))
winning = 0

if first == second == third:
    winning = 10000 + first * 1000
elif (first == second != third) or (first == third != second):
    winning = 1000 + first * 100
elif second == third != first:
    winning = 1000 + second * 100
else:
    winning = max(first, second, third) * 100

print(winning)