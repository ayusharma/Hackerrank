"""

Python has in built string validation methods for basic data validation such as checking if a string is alphabetical, alphanumeric, digit etc.

str.isalnum() 
Check if all characters of string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha() 
Check if all characters of string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit() 
Check if all characters of string are digit (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower() 
Check if all characters of string are lowercase characters.

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper() 
Check if all characters of string are uppercase characters.

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
Task

You are given a string S. 
Your task is to find if string S contains, alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

Single line containing, string S.

Constraints

0<len(S)<1000
Output Format

In First line, print True if S has any alphanumeric character, otherwise print False. 
In Second line, print True if S has any alphabetical character, otherwise print False. 
In Third line, print True if S has any digits, otherwise print False. 
In Fourth line, print True if S has any lowercase character, otherwise print False. 
In Fifth line, print True if S has any uppercase character, otherwise print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""

string = raw_input()
print string
a = list(string)
print a

print any(c.isalnum() for c in string)
print any(c.isalpha() for c in string)
print any(c.isdigit() for c in string)
print any(c.islower() for c in string)
print any(c.isupper() for c in string)













        