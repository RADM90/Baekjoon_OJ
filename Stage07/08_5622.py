s = input()
arr = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
offset = 3
time = 0
for char in s:
    for item in arr:
        if char in item:
            time += arr.index(item) + offset
print(time)