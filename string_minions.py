"""
Problem Statement

Kevin and Stuart want to play the 'The Minion Game'.
Bob is the match referee. Bob's task is to declare the winner and ensure that no rules are broken.
Stuart is Player 1 and Kevin is Player 2.

About Game

Rules
The game is a two player game. Players are given a string S.
Both the players have to make words using the letters of string S.
Player 1 has to make words starting with consonants.
Player 2 has to make words starting with vowels. 
Game ends when both players have made all possible substrings. 

Scoring
A player gets +1 Point for each occurence of the word in the string S.
Example:
If string S = BANANA
Word made by Player 2 = ANA
'ANA' is occuring twice in 'BANANA'. Hence, Player 2 will get 2 Points. 

For better understanding, see the image below: banana.png

Your task is to help Bob.

Input Format

Single line containing string S. 
Note: String S contains only capital alphabets [A-Z].

Constraints

0<len(S)≤106

Output Format

Print the name of the winner along with the total score.

If the game is draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12
Note : 
I would like to suggest mentioning that the vowels here are defined as AEIOU (since Y is sometimes considered a vowel, but not in this problem)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
string  = raw_input()
word = list(string)

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

vow = list('AEIOU')

kv = set()
sc = set()

kwl = set()
swl = set()

swlp = 0
kwlp = 0

for i in word:
    if i in vow:
        kv.add(i)
    else:
        sc.add(i)

for i in xrange(len(word)):
    for j in range(i,len(word)):
        if word[i] in kv:
            kwl.add(string[i:j+1])
#            print '% %',(i,j+1)
        else:
            swl.add(string[i:j+1])
        
#For points

for i in swl:
    swlp = swlp+occurrences(string,i)
    
for i in kwl:
    kwlp = kwlp+occurrences(string,i)
    
if swlp > kwlp:
    print 'Stuart',swlp
elif kwlp > swlp:
    print 'Kevin',kevin
else:
    print 'Draw'