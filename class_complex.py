"""

Problem Statement

For this challenge, you are given two complex numbers and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The precision of both the real and imaginary part should be two digits after decimal.

Input Format

Real and imaginary part of a number separated by space.

Output Format

For two complex numbers C and D, the output should be in the following sequence
C + D
C - D
C * D
C / D
mod(C)
mod(D) 

For complex numbers with non-zero real(A) and complex part(B), the output should be in the following format : 
A+Bi
Replace the plus symbol (+) with a minus symbol (-) when B < 0.

For complex numbers with a zero complex part i.e. real numbers, the output should br : 
A+0.00i 
For complex numbers where the real part is zero and the complex part(B) is non-zero, the output should be :
0.00+Bi

Sample Input

2 1
5 6
Sample Output

7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
Concept

Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here. 

Method with double underscore before and after their name are considered as built-in methods i.e. they are used by interpreter and are generally used in implementation of overloaded operators or other built-in functionality. 

__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation



"""
import math
class Complex(object):

    def __init__(self, a, b):
        '''Creates Complex Number'''
        self.a = a
        self.b = b

    def __str__(self):
        '''Returns complex number as a string'''
        if self.b>=0:
            return '%s+%si' % ("{0:.2f}".format(self.a), "{0:.2f}".format(self.b)) 
        else:
            return '%s%si' % ("{0:.2f}".format(self.a), "{0:.2f}".format(self.b)) 
        
    def __add__(self, rhs):
        '''Adds complex numbers'''
        return Complex(self.a + rhs.a, self.b + rhs.b)
    
    def __sub__(self, rhs):
        '''Subtract complex numbers'''
        return Complex(self.a - rhs.a, self.b - rhs.b)
    
    def __mul__(self, rhs):
        '''Multiply complex numbers'''
        return Complex(self.a*rhs.a+self.b*rhs.b*(-1), self.b*rhs.a+self.a*rhs.b)
    
    def __div__(self, rhs):
        '''Division complex numbers'''
        return Complex(self.a*rhs.a+self.b*rhs.b*(-1), self.b*rhs.a+self.a*rhs.b)
    
    def __div__(self, rhs):
        sr, si, oor, oi = self.a, self.b, rhs.a, rhs.b # short forms
        r = float(oor**2 + oi**2)
        return Complex((sr*oor+si*oi)/r, (si*oor-sr*oi)/r)
    
    def __abs__(self):
        return '%s+0.00i'%"{0:.2f}".format(math.sqrt(self.a**2 + self.b**2))
    

A,B= (map(float,raw_input().split()) for _ in xrange(2))
print Complex(A[0],A[1])+Complex(B[0],B[1])
print Complex(A[0],A[1])-Complex(B[0],B[1])
print Complex(A[0],A[1])*Complex(B[0],B[1])
print Complex(A[0],A[1])/Complex(B[0],B[1])
print abs(Complex(A[0],A[1]))
print abs(Complex(B[0],B[1]))
