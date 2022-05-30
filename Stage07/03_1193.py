x = int(input())
level = 0
last_idx = 0
while x > last_idx:
    level += 1
    last_idx += level

gap = last_idx - x
if level % 2 == 0:
    head = level - gap
    body = gap + 1
else:
    head = gap + 1
    body = level - gap

print("%d/%d" % (head, body))