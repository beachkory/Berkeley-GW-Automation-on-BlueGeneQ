nkpts=KPTS_HERE
kperpool=KPERPOOL_HERE

def divide_nkpt(nkpt):
    return [nkpt/kperpool, nkpt%kperpool]

pools = divide_nkpt(nkpts)[0]
remainder = divide_nkpt(nkpts)[1]


print("NumPools=" + "\"" + str(pools) + "\"")
q =kperpool + remainder
print("NK=\"" + str(q)) 
for i in range(pools-1):
    q += kperpool
    print(str(q))
    if i == pools-2:
        print("\"")

