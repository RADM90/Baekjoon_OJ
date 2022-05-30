inp = input().zfill(2)
new_inp = inp
switch = True
counter = 0
while switch:
    counter += 1
    inp_sum = str(int(new_inp[0]) + int(new_inp[1])).zfill(2)
    new_inp = new_inp[1] + inp_sum[1]
    if new_inp == inp:
        switch = False
print(counter)