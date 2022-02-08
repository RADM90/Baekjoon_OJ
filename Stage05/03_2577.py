num = 1
for _ in range(3):
    num *= int(input())

arr = [0 * i for i in range(10)]

str_num = str(num)
for i in str_num:
    arr[int(i)] += 1

for i in arr:
    print(i)