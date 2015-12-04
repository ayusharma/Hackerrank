"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
"""

import string
from collections import defaultdict
d = defaultdict(list)
num = input()
alph = list(string.ascii_lowercase)
# print alph


# for i in xrange(num):
# 	print ((alph[num])+'-'*i).rjust(num*2,'-')+'#-'+('#-'*i).ljust(num*2,'-')

# for i in xrange(1,num):
# 	print (('#-'*(num-i-1)).rjust(num*2,'-')+'#-'+('#-'*(num-i-1)).ljust(num*2,'-'))

for i in range(1,(2*num-1)+1):
	for j in range(1,(2*(2*num-1)-1)+1):
		d[i].append('-')

k = (len(d)*2)//2
temp = (len(d)//2 )
for i in range(1,len(d)+1):
	if i <= (len(d)+1)//2:
		index = num
		middle  = (len(d[i])+1)//2
		for j in range(k,k+4*i-3,2):
			d[i][j-1] = alph[index-1]
			if j >= middle:
				index = index +1
			else:
				index = index -1
		k = k-2
	else:
		d[i] = d[temp]
		temp = temp -1
		
# print d

for i in range(1,len(d)+1):
	print ''.join(d[i])
