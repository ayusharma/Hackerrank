# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
I = raw_input().split()
I[0] = list(I[0])
I[0].sort()
M = list(map(''.join,combinations_with_replacement(I[0],int(I[1]))))
for i in M:
    print i