s = input()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# rarr = ['č', 'ć', 'dž', 'đ', 'lj', 'nj', 'š', 'ž']

for item in arr:
    if s.__contains__(item):
        s = s.replace(item, "_")
print(len(s))