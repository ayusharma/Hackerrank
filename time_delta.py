"""
Problem Statement

Timestamps are given in the format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the timezone. See sample below for details.

Task 
Given 2 timestamps, print the absolute difference (in seconds) between them.

Input Format 
First line contains T representing T testcases. 
Each testcase contains 2 lines, representing time t1 and time t2.

Output Format 
Print the absolute difference (t1−t2) in seconds.

Constraints 
It is guaranteed that input contains only valid timestamps and the year can reach up to 3000.

Sample Input

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 +0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 +0000
Sample Output

25200
88200

"""

import email.utils
import time
import datetime

for i in xrange(input()):
    print int(round(float(email.utils.mktime_tz(email.utils.parsedate_tz(raw_input()))) - float(email.utils.mktime_tz(email.utils.parsedate_tz(raw_input())))))
