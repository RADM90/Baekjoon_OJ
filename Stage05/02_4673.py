all_nums = set(range(1, 10001))
self_nums_with_generator = set()

for i in all_nums:
    for j in str(i):
        i += int(j)
    self_nums_with_generator.add(i)

self_nums_wo_generator = sorted(all_nums - self_nums_with_generator)
for i in self_nums_wo_generator:
    print(i)