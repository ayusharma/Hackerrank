"""
Problem Statement

Exceptions

Errors detected during execution are called exceptions.

Examples:

ZeroDivisionError 
Raised when the second argument of a division or modulo operation is zero.

>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
ValueError 
Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
To know more about different built-in exceptions click here.

Handling Exceptions

try and except statements can be used to handle selected exceptions. A try statement may have more than one except clause, to specify handlers for different exceptions.

#Code
try:
    print 1/0
except ZeroDivisionError as e:
print "Error Code:",e

#Output
Error Code: integer division or modulo by zero
Task

You are given two values a and b. 
Your task is to do integer division and print a/b.

Input Format

First line contains, number of testcases T. 
Next T line contains, space separated values of a and b.

Constraints

0<T<10
Output Format

Print value of a/b. 
In case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note: 
For integer division in Python 3 use //.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in xrange(input()):
    try:
        k = map(int,raw_input().split())
        print k[0]//k[1]
    except ZeroDivisionError as e:
            print "Error Code:",e
    except ValueError as e:        
            print "Error Code:",e