"""


Problem Statement

rsz_1438840048-2cf71ed69d-findangle.png ABC is a right angle triangle, right angled at B.
Therefore, ∡ABC=90°.

Point M is the mid-point of hypotenuse AC.

You are given the lengths AB and BC. 
Your task is to find ∡MBC ( angle θ°, as shown in figure ) in degrees.

Input Format

First line contains, length of side AB.
Second line contains, length of side BC.

Constraints

0<AB<100
0<BC<100
Lengths AB and BC are natural numbers.

Output Format

Output ∡MBC in degrees. 

Note: Round-off the angle to nearest integer. 
Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.

0°<θ°<90°
Sample Input

10
10
Sample Output

45°


"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan,degrees
a=input()
b=input()
k=atan(1.0*a/b)
print str(int(round(degrees(k))))+'°'