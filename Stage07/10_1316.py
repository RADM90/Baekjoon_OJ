ans = n = int(input())

for _ in range(n):
    string = input()
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            pass
        elif string[i] in string[i + 1:]:
            ans -= 1
            break
print(ans)