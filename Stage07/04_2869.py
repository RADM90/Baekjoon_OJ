a, b, v = map(int, input().split())
days, last = divmod(v - b, a - b)
print(days + (0 if last == 0 else 1))