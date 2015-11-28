"""

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat. 
Design specifications are as follows:
1. Size of mat must be NXM. (N is an odd natural number and M is 3 times N.)
2. Design should have 'WELCOME' written in the center. 
3. Design pattern should only use '|', '.' and '-' characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

"""


N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1,N,2): 
    print ('.|.'*i).rjust(M-N,'-')+'.|.'+('.|.'*i).ljust(M-N,'-')
print 'WELCOME'.center(M,'-')
for i in xrange(N-2,-1,-2): 
    print ('.|.'*i).rjust(M-N,'-')+'.|.'+('.|.'*i).ljust(M-N,'-')
