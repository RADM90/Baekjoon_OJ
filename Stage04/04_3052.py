inp_arr = [int(input()) for _ in range(10)]
dic = set()
for i in inp_arr:
    dic.add(i % 42)
print(len(dic))
