h, m = list(map(int, input().split()))
cooking_time = int(input())
m += cooking_time

if m >= 60:
    up = m // 60
    h += up
    m = abs(60 * up - m)

if h >= 24:
    h = abs(24 - h)

print(h, m)