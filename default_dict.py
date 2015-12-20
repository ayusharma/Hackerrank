"""
DefaultDict is a container in the collections class of Python. It is almost the same as the usual dictionary (dict) container but with one difference. The value fields' data-type is specified upon initialization. 
A basic snippet showing the usage follows:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
This prints:

('python', ['awesome', 'language'])
('something-else', ['not relevant'])

"""
"""
from collections import defaultdict
d = defaultdict(list)
e = defaultdict(list)

nums = map(int,raw_input().split())

print nums
for i in xrange(nums[0]):
	d['a'].append(raw_input())

for i in xrange(nums[1]):
	d['b'].append(raw_input())

for i in xrange(len(d['b'])):
	# try:
	if d['b'][i] in d['a']:
		e[i].append([ x+1 for x in xrange(len(d['a'])) if d['a'][x] == d['b'][i] ])
	else:
		e[i].append('-1')
print e 

for i in xrange(len(e)):
	print ' '.join(map(str,e[i][0]))

"""

from collections import defaultdict
a,b  = map(int,raw_input().split())
d = defaultdict(list)
for i in xrange(a):
    d['n'].append(raw_input())
    
for i in xrange(b):
    d['m'].append(raw_input())
    
m = defaultdict(list)

for i,k in enumerate(d['m']):
    l = [x+1 for x,y in enumerate(d['n']) if y == k] 
    m[k].append(l)
    if k not in d['n']:
         m[k][0].append(-1)
#    for x,y in enumerate(d['n']):
#        print y,k
#        if y == k :
#            m[y].append(x+1)
#        else:
#            m[y].append(-1)
            
#print m
for i in d['m']:
    print ' '.join(map(str,m[i][0]))





