"""

Problem Statement

dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
Task

You are given two arrays A and B. Both have dimensions of NXN. 
Your task is to compute their matrix product.

Input Format

The first line contains the integer N. 
The next N lines contains N space separated integers of array A. 
The following N lines contains N space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.

Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]

 """


 import numpy
k = map(int,raw_input().split())
l,m = [ map(int,raw_input().split()) for _ in xrange(k[0]) ],[map(int,raw_input().split()) for _ in xrange(k[0]) ]
a,b = numpy.array(l),numpy.array(m)
print numpy.dot(a,b)