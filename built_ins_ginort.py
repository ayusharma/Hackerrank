"""

You are given a string S. 
S contains alphanumeric characters only. 
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string S.

Constraints

0<len(S)<1000
Output Format

Output the sorted string S.

Sample Input

Sorting1234
Sample Output

ginortS1324
Note: 
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0. 
b) You can only use one sorted function in your code. A 0 score will be awarded for using sorted more than once. 

Hint: Success is not the key, but key is success.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function
k = raw_input()
def even(x):
    if x.isdigit():
        if int(x)%2 ==0:
            return True
        else: return False
    else: return True
print (*sorted(k,key = lambda x:(x.isdigit(),even(x),x.isupper(),x)),sep='')