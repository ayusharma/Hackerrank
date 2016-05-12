"""
start() & end()

These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
Task 
You are given a string . 
Your task is to find the indices of the start and end of string  in .

Input Format

The first line contains the string . 
The second line contains the string .

Constraints

 

Output Format

Print the tuple in this format: (start _index, end _index). 
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from collections import OrderedDict
od = OrderedDict()
S = raw_input().strip()
k = raw_input().strip()
i = 0
l = list()
if re.search(k,S) == None:
    print (-1,-1)
else :
    while i<len(S):
        m = re.search(k,S[i:])
        if m == None:
            break;
        else:
            p = i+m.start()
            n = (p,p+len(k)-1)
            od[i] = n
        i = i+1

    for p,s in enumerate(od.values()):
        if od.values()[p] != od.values()[p-1]:
            print s