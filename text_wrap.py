"""
Textwrap

The textwrap module provides two convenience functions, wrap() and fill().

textwrap.wrap() 
Wraps the single paragraph in text (a string) so every line is at most width characters long. 
Returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
textwrap.fill() 
Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.

"""

import textwrap

a = raw_input()
b = input()

print textwrap.fill(a,b)