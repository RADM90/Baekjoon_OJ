swtc = False

while swtc is False:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        swtc = True
    else:
        print(a + b)
