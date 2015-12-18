from itertools import combinations
I = raw_input().split()
m = list()
I[0] = list(I[0])
I[0].sort()
for i in xrange(1,int(I[1])+1):
    m.append(list(map(''.join,combinations(I[0],i))))

for i in m:
	for k in i:
		print k