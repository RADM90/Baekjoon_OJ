n = int(input())

counter = 0
while n >= 0:
    if n % 5 == 0:
        counter += n // 5
        print(counter)
        break
    n -= 3
    counter += 1
else:
    print(-1)
