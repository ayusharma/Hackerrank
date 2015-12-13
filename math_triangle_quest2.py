"""

Problem Statement

You are given a positive integer N. You have to print a numerical triangle of height N−1 as shown below:

1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

You can't take more than two lines; the first line (for - statement) is already written for you. You have to complete the print statement.

Note Using anything related to strings will give a score of 0.

Input Format 
Given N in the first line.

Constraints 
1≤N≤9

Output Format 
Print N−1 lines as explained above.

Sample Input

5
Sample Output

1
22
333
4444

"""

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((pow(10,i)-1)/9)*i
