"""

Problem Statement

You are given a positive integer N. 
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you. 
You have to complete the code using exactly one print statement.

Note: 
Using anything related to strings will give a score of 0. 
Using more than one for-statement will give a score of 0.

Input Format

A single line of input containing the integer N.

Constraints

0<N<10
Output Format

Print the palindromic triangle of size N as explained above.

Sample Input

5
Sample Output

1
121
12321
1234321
123454321


"""
"""
Sol 1:

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ''.join(map(str,range(1,i+1)))+''.join(map(str,range(i-1,0,-1)))

"""

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
     print pow((pow(10,i)-1)/9,2)