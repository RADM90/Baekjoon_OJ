s = input()
tup = sorted(set(chr(i) for i in range(ord("a"), ord("z") + 1)))
for i in tup:
    print(s.index(i) if i in s else -1, end=" ")