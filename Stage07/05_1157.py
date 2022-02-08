"""
### 32820KB	260ms
s = input().upper()
arr = {chr(i): 0 for i in range(ord("A"), ord("Z") +1)}
for char in s:
    arr[char] = arr.get(char) + 1
val_arr = arr.values()
val_max = max(val_arr)
max_counter = 0
for val in val_arr:
    max_counter += 1 if val == val_max else 0
print(list(arr.keys())[list(val_arr).index(val_max)] if max_counter == 1 else "?")
"""

### 32820KB	108ms
s = input().upper()
unique = list(set(s))

count_list = []
for char in unique:
    count = s.count(char)
    count_list.append(count)
if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(unique[count_list.index(max(count_list))])