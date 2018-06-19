thresh = THRESH_HERE
bgrp = BGRP_HERE

import csv
with open('nks.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        K = int(row['K'])
	Kq = int(row['Kq'])
	Kun = int(row['Kun'])

def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors[::-1]

def test_thresh(klist,t):
	for q in klist:
		if q <= t:
			kout = q
			break
	return kout

Klist = get_all_factors(K)
Kqlist = get_all_factors(Kq)
Kunlist= get_all_factors(Kun)

Kfin = test_thresh(Klist,thresh)
Kqfin =test_thresh(Kqlist,thresh)
Kunfin = test_thresh(Kunlist,thresh)

print("#!/bin/bash")
print("K=\"" + str(Kfin) + "\"\nKq=\"" + str(Kqfin) + "\"\nKun=\"" + str(Kunfin) + "\"")
print("Kproc=\"" + str(Kfin*bgrp) + "\"\nKqproc=\"" + str(Kqfin*bgrp) + "\"\nKunproc=\"" + str(Kunfin*bgrp) + "\"")
