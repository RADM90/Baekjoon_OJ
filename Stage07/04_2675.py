n = int(input())
for i in range(n):
    st = ''
    m, s = input().split()
    for j in s:
        st += j * int(m)
    print(st)