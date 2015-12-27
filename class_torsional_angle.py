"""
Problem Statement

You are given four points A, B, C and D in the 3-dimensional cartesian coordinate system. You are required to print the angle between the plane made by points A, B, C and B, C, D in degrees(NOT RADIAN). Let the angle be PHI. Cos(PHI) = (X . Y)/|X||Y| where X = AB x BC and Y = BC x CD. Here X.Y means the dot product of X and Y. AB x BC means the cross product of vectors AB and BC. AB = B - A.

Input Format

X, Y and Z coordinates of a point in one line separated by space, where they are floating numbers.

Output Format

Angle with precision of two digits after decimal.

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2
Sample Output

8.19

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c
def absolute(X):
    return math.sqrt(X[0]**2+X[1]**2+X[2]**2)
def dotp(X,Y):
    return sum(p*q for p,q in zip(X, Y))

A,B,C,D = (map(float,raw_input().split()) for _ in xrange(4))
AB = [B[0] - A[0],B[1] - A[1],B[2] - A[2]]
BC = [C[0] - B[0],C[1] - B[1],C[2] - B[2]]
CD = [D[0] - C[0],D[1] - C[1],D[2] - C[2]] 

X = cross(AB,BC)
Y = cross(BC,CD)
theta = dotp(X,Y)/(absolute(X)*absolute(Y))
print '{0:.2f}'.format(math.degrees(math.acos(theta)))