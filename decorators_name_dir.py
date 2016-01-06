"""
Problem Statement

Lets use decorators for building a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. You have to print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people having the same age, the printing should be done in the order of their input. For Henry Davids, the output should be

Mr. Henry Davids
For Mary George, the output should be

Ms. Mary George
Input Format

The first lines contain integer N followed by N lines. Each line contains firstname, lastname, age and sex separated by a single space character.

Constraints 
1≤N≤10
Output Format

N names printed in N different lines.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
Concept

For sorting a nested list based on some parameter you can use itemgetter library. You can read more about it here. 

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = input()
k = OrderedDict()
for i in xrange(n):
    k[i]= raw_input().split()

l = sorted(k.items(),key = lambda x:x[1][2])
for x in l:
    if x[1][3] == 'F':
        print 'Ms.',x[1][0],x[1][1]
    else:
        print 'Mr.',x[1][0],x[1][1]