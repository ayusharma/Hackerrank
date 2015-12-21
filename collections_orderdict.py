"""

collections.OrderedDict

An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

Example

Code

>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
Task

You are the manager of a supermarket. 
You have a list of N items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, N. 
The next N lines contains the item's name and price, separated by a space.

Constraints

0<N≤100
Output Format

Print the item_name and net_price in order of its first occurrence.

Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
Explanation

BANANA FRIES: Quantity bought: 1, Price: 12 
Net Price: 12 
POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60 
APPLE JUICE: Quantity bought: 2, Price: 10 
Net Price: 20 
CANDY: Quantity bought: 4, Price: 5 
Net Price: 20

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict,defaultdict
od = OrderedDict()
m = defaultdict(list)
for i in xrange(input()):
    k = raw_input().split()
    k[0] = ' '.join(k[0:len(k)-1])
    k[1] = int(k[len(k)-1])
    k = k[0:2]
    m[k[0]].append(k[1])
    od[k[0]] = i

for i in od:
    print i,sum(m[i])