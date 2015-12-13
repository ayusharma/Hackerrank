"""

Problem Statement

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

A complex number z Capture.PNG
z=x+yj
is completely determined by its real part x and imaginary part y. 
j is the imaginary unit.

A polar coordinate (r,φ) Capture.PNG

is completely determined by modulus r and phase angle φ.

If we convert complex number z to its polar coordinate, we find,
r : Distance from z to origin, i.e., x2+y2‾‾‾‾‾‾‾√
φ : Counter clockwise angle measured from the positive x-axis to the line segment that joins z to origin.

Python's cmath module provides acces to mathematical functions for complex numbers.

cmath.phase 
Return phase of complex number z (also known as argument of z).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931
abs 
Return modulus (absolute value) of complex number z.

>>> abs(complex(-1.0, 0.0))
1.0
Task 
You are given a complex z. Your task is to convert it to polar coordinate.

Input Format

Single line containing complex number z.

Output Format

Two lines: 
First line contains, value of r. 
Second line contains, value of φ.

Sample Input

  1+2j
Sample Output

 2.23606797749979 
 1.1071487177940904
Note : Output should be correct up to 3 decimal places.

"""

from cmath import sqrt,phase
c = complex(input())

print sqrt(pow(c.real,2)+pow(c.imag,2)).real
print phase(complex(c.real,c.imag))