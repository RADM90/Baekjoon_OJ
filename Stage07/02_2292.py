n = int(input())
layer = 1
counter = 1

while layer < n:
    layer += counter * 6
    counter += 1
print(counter)