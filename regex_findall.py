"""

re.findall()

The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
Code

>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
re.finditer()

The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
Code

>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
Task
You are given a string SS. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of SS that contains 22 or more vowels.
Also, these substrings must lie in between 22 consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string SS.

Constraints

0<len(S)<1000<len(S)<100
Output Format

Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
Explanation

ee is located between consonant dd and ff.
Ioo is located between consonant kk and mm.
Oeo is located between consonant pp and rr.
eeeee is located between consonant tt and tt.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

k = re.findall(r'(?<=[^aeiouAEIOU ])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU ])',raw_input())

if k:
    for i in k:
        print i
else:
    print -1
