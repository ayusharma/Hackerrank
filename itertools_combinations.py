from itertools import combinations
I = raw_input().split()
m = list()
for i in xrange(1,int(I[1])):
    m.append(list(map(''.join,combinations(I[0],i))))

for i in m:
	for k in i:
		print k