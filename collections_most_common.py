"""
Problem Statement

You are given a string S. 
The string contains only lowercase alphabetic characters.

Your task is to find top three most common characters in the string S.

Input Format

Single line containing string S.

Constraints

3<len(S)<104
Output Format

Print the most common characters along with their count of occurences in three lines.
Output must sorted in descending order of count of occurences.
If count of occurences is same then sort in ascending order of characters.

Sample Input

aabbbccde
Sample Output

b 3
a 2
c 2
Explanation

b is occuring 3 times. Hence, it is printed first.
Both a and c occur 2 times. So, a is printed in second line and c in third line because in ascending order of alphabets a comes ahead of c.

Note: The string S has at least 3 distinct characters.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
a = list(raw_input())
c = Counter(a)
for i in sorted(c.items(), key=lambda x:(-x[1], x[0]))[:3]:
    print i[0], i[1]