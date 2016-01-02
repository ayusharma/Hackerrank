"""

zeros

The zeros tool returns a new array with a given shape and type filled with 0's.

import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]
ones

The ones tool returns a new array with a given shape and type filled with 1's.

import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]   
Task

Your task is to print an array of size N and integer type using the tools zeros and ones. N is the space separated list of the dimensions of the array.

Input Format

A single line containing the space separated list of N.

Output Format

First, print the array using the zeros tool and then print the array with the ones tool.

Sample Input

3 3 3
Sample Output

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]] 


  """

import numpy
k = map(int,raw_input().split())
print numpy.zeros(k,dtype = numpy.int)
print numpy.ones(k,dtype = numpy.int)