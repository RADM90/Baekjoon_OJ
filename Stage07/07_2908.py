a, b = input().split()
# ar = int("".join(reversed(a)))
# br = int("".join(reversed(b)))
ar = a[::-1]
br = b[::-1]
print(ar if ar > br else br)