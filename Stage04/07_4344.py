c = int(input())
arr = [list(map(int, input().split())) for _ in range(c)]

for seq in arr:
    seq.remove(seq[0])
    seq_avg = sum(seq) / len(seq)
    counter = 0
    seq.sort(reverse=True)
    for i in seq:
        if i > seq_avg:
            counter += 1
        else:
            break
    print("%.3f" % round(counter / len(seq) * 100, 3), end="%\n")