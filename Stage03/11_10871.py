n, x = map(int, input().split())
arr = list(input().split())
result = ""
for i in range(n):
    if int(arr[i]) < x:
        print(arr[i], end=" ")