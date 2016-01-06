"""
Problem Statement

You are given a valid XML document and you have to print the maximum level of nesting in it. The first line of input is the number of XML lines followed by the XML lines. Take the depth of root as 0.

Input Format

The first line shows the number of lines in XML document followed by the XML document.

Output Format

An integer value

Sample Input

6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
Sample Output

1
Explanation

Here, the root is feed tag, which has depth 0. Tags title, subtitle, link and updated all have depth 1. Thus, the maximum depth is 1.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from xml.etree.ElementTree import XMLParser
class MaxDepth:                     
    maxDepth = 0
    depth = 0
    def start(self, tag, attrib):   
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
    def end(self, tag):             
        self.depth -= 1
    def data(self, data):
        pass            
    def close(self):
        return self.maxDepth
target = MaxDepth()
parser = XMLParser(target=target)
n = input()
k = ''
for i in xrange(n):
    k=k+raw_input()
parser.feed(k)
print parser.close() -1
