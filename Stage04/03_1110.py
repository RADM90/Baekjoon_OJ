"""
inp = input().zfill(2)
new_inp = ""
switch = True

counter = 0
while switch:
    counter += 1
    num_sum = "%2d" % (int(inp[0]) + int(inp[1]) if counter == 1 else int(new_inp[0]) + int(new_inp[1]))
    new_inp = inp[1] + str(num_sum)[1] if counter == 1 else (new_inp[1] + num_sum[1])
    if new_inp == inp:
        switch = False
print(counter)

"""
#########################################

inp = input().zfill(2)
new_inp = inp
counter = 0
while new_inp != inp:
    counter += 1
    inp_sum = str(int(new_inp[0]) + int(new_inp[1])).zfill(2)
    new_inp = new_inp[1] + inp_sum[1]
print(counter)
