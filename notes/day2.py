Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # HOW -> WHAT     (declarative programming)
>>> 
>>> n = 10
>>> squares = []
>>> for i in range(n):
	s = i ** 2
	squares.append(s)

	
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> sum(squares)
285
>>> 
>>> # Make an empty list
>>> # Loop n times, counting with i
>>> #    Compute a square
>>> #    Add that result to the list
>>> # Add-up the list
>>> 
>>> # ^-- How to compute the sum of squares
>>> 
>>> # A list of squares of number from the range 0 to n-1.#
>>> # ^-- What
>>> 
>>> # List comprehension:
>>> [i**2 for i in range(n)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> # [ <expr> for <var> in  <iterable> ]
>>> sum([i**2 for i in range(n)])
285
>>> # Sum of squares of numbers from 0 to n-1
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow
>>> 
>>> # My friend say Python is just a beginner language.
>>> # Why does the think that?
>>> # My friend says Python code is really easy.
>>> # You say that like it is a bad thing.
>>> 
>>> # Cobol Fortran APL Basic Prolog PL/1 ...
>>> # Overtime, we learned to make languages better.
>>> 
>>> 
>>> # LOC per programmer on team by language -> Constant
>>> # The higher level language you use the more productive you are.
>>> 
>>> 
>>> # One really good interpreted lang:  Python Ruby Perl Tcl
>>> # One really good low level compiled:  C  C++  Go  Rust   D   ObjectiveC
>>> # Java (enormous ecosystem)
>>> # Mind expanders:  Lisp/Scheme Forth Prolog APL Haskell(hard) Erlang
>>> 
>>> # GoLang  ErLang   Swift
>>> # Google  Ericsson Apple
>>> 
>>> # C# Microsoft
>>> 
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow
>>> # O(n log n)
>>> from math import log2
>>> log2(32)
5.0
>>> n = 1_000_000
>>> n = 1000000
>>> 
>>> round(n * log2(n))
19931569
>>> format(round(n * log2(n)), ',d')
'19,931,569'
>>> # strlen: O(n)
>>> asl = 100
>>> n = 1000000
>>> n * log2(n) * 2 * asl
3986313713.864835
>>> format(n * log2(n) * 2 * asl, ',d')
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    format(n * log2(n) * 2 * asl, ',d')
ValueError: Unknown format code 'd' for object of type 'float'
>>> format(round(n * log2(n) * 2 * asl), ',d')
'3,986,313,714'
>>> 
>>> 
>>> deco = [(len(s), s) for s in colors]
>>> deco
[(3, 'red'), (4, 'blue'), (6, 'yellow'), (5, 'green')]
>>> deco.sort()
>>> deco
[(3, 'red'), (4, 'blue'), (5, 'green'), (6, 'yellow')]
>>> 
>>> [color for size, color in deco]
['red', 'blue', 'green', 'yellow']
>>> 
>>> len('hello')         # Arity one
5
>>> # I don't think that is the right solution to the problem.
>>> # It is contraindicated.
>>> 
>>> colors
['red', 'blue', 'yellow', 'green']
>>> colors[1]
'blue'
>>> len(colors[1])
4
>>> def second_letter(word):
    return word[1]

>>> second_letter('yellow')
'e'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
>>> # e e l r
>>> 
>>> 
>>> s = 'the tale of two cities
SyntaxError: EOL while scanning string literal
>>> 
>>> 
>>> s = 'the tale of two cities'
>>> s[0]
't'
>>> s[1]
'h'
>>> len(s)
22
>>> s[50]
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s[50]
IndexError: string index out of range
>>> s[22]
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s[22]
IndexError: string index out of range
>>> s[len(s) - 1]             # rightmost character -- 1st character from the right
's'
>>> s = 'the tale of two cities'
>>> s[len(s) - 1]
's'
>>> s[len(s) - 2]             # 2nd character from the right
'e'
>>> s[len(s) - 5]             # 5th character from right
'i'
>>> s[-1]
's'
>>> s[-2]
'e'
>>> s[-5]
'i'
>>> s
'the tale of two cities'
>>> s[0] + s[1] + s[2]
'the'
>>> s[4] + s[5] + s[6] + s[7]
'tale'
>>> list(range(3))
[0, 1, 2]
>>> list(range(0, 3))
[0, 1, 2]
>>> list(range(4, 8))
[4, 5, 6, 7]
>>> 
>>> s[0:3]
'the'
>>> s[4:8]
'tale'
>>> 
>>> 
>>> s[9 : len(s)]
'of two cities'
>>> 
>>> s[:3]              # same as s[0:3]
'the'
>>> s[9:]              # same as s[9:len(s)]
'of two cities'
>>> 
>>> # A characters can be indexed from the left or from the right
>>> s
'the tale of two cities'
>>> len(s)
22
>>> s[4]
't'
>>> s[22 - 18]
't'
>>> s[len(s) - 18]
't'
>>> s[-18]
't'
>>> 22 - 6
16
>>> s[16]
'c'
>>> s[-6]
'c'
>>> s[16:]
'cities'
>>> s[-6:]
'cities'
>>> s[-6:]            # Give me the six rightmost characters
'cities'
>>> 
>>> 
>>> s = 'download.html'
>>> i = s.index('.')
>>> i
8
>>> s[i]
'.'
>>> s[:8]
'download'
>>> s[8:]
'.html'
>>> s[:-5]
'download'
>>> s[-5:]
'.html'
>>> s = 'index.html'
>>> s[:8]
'index.ht'
>>> s[8:]
'ml'
>>> s[:-5]
'index'
>>> s[-5:]
'.html'
>>> # Cute saying: I would give my right arm to be ambidextorous
>>> 
>>> 
>>> # Easy way to make something harder:
>>> #     Use a greek letter
>>> 
>>> # make_function --> lambda
>>> 
>>> def f(x):
	return 3*x**2 - 5*x + 4

>>> f(10)
254
>>> f = lambda x: 3*x**2 - 5*x + 4
>>> f(10)
254
>>> # The "def" requires you give the function a name
>>> # The "def" stores the name for you
>>> # The "def" is a statement, so it has to be on a separate line from the function call
>>> 
>>> (lambda x: 3*x**2 - 5*x + 4)(10)
254
>>> list(map(lambda x: 3*x**2 - 5*x + 4, range(10)))
[4, 2, 6, 16, 32, 54, 82, 116, 156, 202]
>>> [f(0), f(1), f(2), f(3)]
[4, 2, 6, 16]
>>> # temporary function
>>> # anonymous function
>>> # in-line function
>>> # "lambda" -> make_function
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
red
yellow
blue
green
>>> lambda x: 3*x**2 - 5*x + 4
<function <lambda> at 0x10a549048>
>>> 
>>> 
>>> 
>>> colors
['red', 'blue', 'yellow', 'green']
>>> for color in colors:
	print(color.upper())

	
RED
BLUE
YELLOW
GREEN
>>> for c in colors:
	print(c.upper())

	
RED
BLUE
YELLOW
GREEN
>>> lot = [('raymond', 'red'), ('rachel', 'blue')]
>>> for t in lot:
	print(t)

	
('raymond', 'red')
('rachel', 'blue')
>>> for t in lot:
	name, color = t
	print(name, '-->', color)

	
raymond --> red
rachel --> blue
>>> for name, color in lot:
	print(name, '-->', color)

	
raymond --> red
rachel --> blue
>>> names
['raymond', 'rachel', 'matthew']
>>> colors
['red', 'blue', 'yellow', 'green']
>>> list(zip(names, colors))
[('raymond', 'red'), ('rachel', 'blue'), ('matthew', 'yellow')]
>>> for name, color in zip(names, colors):
	print(name, '-->', color)

	
raymond --> red
rachel --> blue
matthew --> yellow
>>> list(enumerate(colors))
[(0, 'red'), (1, 'blue'), (2, 'yellow'), (3, 'green')]
>>> for index, color in enumerate(names, start=1):
	print(index, '-->', color)

	
1 --> raymond
2 --> rachel
3 --> matthew
>>> 
>>> 
>>> 
>>> colors
['red', 'blue', 'yellow', 'green']
>>> deco = [(len(s), s) for s in colors]
>>> deco
[(3, 'red'), (4, 'blue'), (6, 'yellow'), (5, 'green')]
>>> for size, color in deco:
	print(size, '-->', color)

	
3 --> red
4 --> blue
6 --> yellow
5 --> green
>>> [size for size, color in deco]
[3, 4, 6, 5]
>>> pow(2, 5)             # Arity two
32
>>> lon = [-4, -9, 7, 2, 10]
>>> sorted(lon, key=lambda x: x**2)
[2, -4, 7, -9, 10]
>>> sorted(lon, key=abs)
[2, -4, 7, -9, 10]
>>> 
>>> 
>>> # lambdas   map()  sorting()    unpacking   list comprehensions
>>> persons = [
	('raymond', 'hettinger', 0x36),
	('susan', 'peters', 0x38),
	('dee', 'camp', 0x30),
	('juliet', 'schmidt', 0x40),
	('sarah', 'brenkus', 0x2D),
]
>>> person = persons[2]
>>> person
('dee', 'camp', 48)
>>> 
>>> age = 20 + 7
>>> age
27
>>> hex(age)
'0x1b'
>>> 
>>> 
>>> x = 0b1101
>>> x
13
>>> x = 0o15
>>> x
13
>>> x = 0xd
>>> x
13
>>> x = 13
>>> x
13
>>> # For most people, most of the time, when they a number, they want to see it decimal.
>>> # The default is to display in decimal
>>> x = 54
>>> str(x)
'54'
>>> bin(x)
'0b110110'
>>> oct(x)
'0o66'
>>> hex(x)
'0x36'
>>> 
>>> chr(0x52)
'R'
>>> chr(0x65)
'e'
>>> chr(0x64)
'd'
>>> chr(0x20)
' '
>>> chr(0x42)
'B'
>>> chr(0x75)
'u'
>>> chr(0x6c)
'l'
>>> chr(0x6c)
'l'
>>> # Red Bull has Wiiings
>>> 
>>> persons = [
	('raymond', 'hettinger', 0x36),
	('susan', 'peters', 0x38),
	('dee', 'camp', 0x30),
	('juliet', 'schmidt', 0x40),
	('sarah', 'brenkus', 0x2D),
]
>>> person
('dee', 'camp', 48)
>>> persons
[('raymond', 'hettinger', 54), ('susan', 'peters', 56), ('dee', 'camp', 48), ('juliet', 'schmidt', 64), ('sarah', 'brenkus', 45)]
>>> from pprint import pprint
>>> pprint(persons)
[('raymond', 'hettinger', 54),
 ('susan', 'peters', 56),
 ('dee', 'camp', 48),
 ('juliet', 'schmidt', 64),
 ('sarah', 'brenkus', 45)]
>>> person
('dee', 'camp', 48)
>>> person[2]
48
>>> def get_age(person):
	return person[2]

>>> get_age(person)
48
>>> hex(48)
'0x30'
>>> 
>>> 
>>> 
>>> persons = [
	('raymond', 'hettinger', 0x36),
	('susan', 'peters', 0x38),
	('dee', 'camp', 0x30),
	('juliet', 'schmidt', 0x40),
	('sarah', 'brenkus', 0x2D),
]
>>> from pprint import pprint
>>> person = persons[2]
>>> def get_age(person):
	return person[2]

>>> list(map(get_age, persons))          # projection
[54, 56, 48, 64, 45]
>>> list(map(lambda p: p[2], persons))
[54, 56, 48, 64, 45]
>>> from operator import itemgetter
>>> 
>>> get_age = itemgetter(2)
>>> get_age(person)
48
>>> 
>>> list(map(itemgetter(2), persons))
[54, 56, 48, 64, 45]
>>> 
>>> # def get_age(p): p[2]       lambda p: p[2]           itemgetter(2)
>>> get_age( ('raymond', 'hettinger', 54) )
54
>>> get_age( ['raymond', 'hettinger', 54] )
54
>>> get_age('raymond')
'y'
>>> ord('A')
65
>>> hex(65)
'0x41'
>>> 
>>> list(map(ord, 'Raymond'))
[82, 97, 121, 109, 111, 110, 100]
>>> list(map(hex, map(ord, 'Raymond')))
['0x52', '0x61', '0x79', '0x6d', '0x6f', '0x6e', '0x64']
>>> print(' '.join(map(hex, map(ord, 'Raymond'))))
0x52 0x61 0x79 0x6d 0x6f 0x6e 0x64
>>> map(ord, 'Raymond')
<map object at 0x10a58f2b0>
>>> list(map(ord, 'Raymond'))
[82, 97, 121, 109, 111, 110, 100]
>>> tuple(map(ord, 'Raymond'))
(82, 97, 121, 109, 111, 110, 100)
>>> set(map(ord, 'Raymond'))
{97, 100, 109, 110, 111, 82, 121}
>>> dict.fromkeys(map(ord, 'Raymond'))
{82: None, 97: None, 121: None, 109: None, 111: None, 110: None, 100: None}
>>> 
>>> 
>>> # What is the signature for map()?
>>> #       map(callable, iterable) -> iterator
>>> 
>>> # What is the signature for ord()?
>>> #       ord(string) -> int
>>> 
>>> # What is the signature for chr()?
>>> #       chr(int) -> string
>>> 
>>> # How do you get a iterator into a container so you can look at it?
>>> #       list(iterator)    tuple(iterator)    set(iterator)  ' '.join(iterator)   dict.fromkeys(iterator)
>>> 
>>> # What is the signature of sorted()?
>>> #       sorted(iterable, key=callable)
>>> #                              ^-- arity 1
>>> 
>>> # How do I make an arity one function?
>>> #       def get_age(p): p[0]                        # gives it a name, stores it, and is a statement
>>> #       lambda p: p[0]                              # anonymous, temporary, in-line
>>> #       itemgetter(0)                               # anonymous, temporary, in-line, and clearer about its goal
>>> 
>>> persons = [
	('raymond', 'hettinger', 0x36),
	('susan', 'peters', 0x38),
	('dee', 'camp', 0x30),
	('juliet', 'schmidt', 0x40),
	('sarah', 'brenkus', 0x2D),
]
>>> from pprint import pprint
>>> from operator import itemgetter
>>> list(map(itemgetter(0), persons))
['raymond', 'susan', 'dee', 'juliet', 'sarah']
>>> list(map(lambda p: p[0], persons))
['raymond', 'susan', 'dee', 'juliet', 'sarah']
>>> pprint(sorted(persons, key=itemgetter(0)))
[('dee', 'camp', 48),
 ('juliet', 'schmidt', 64),
 ('raymond', 'hettinger', 54),
 ('sarah', 'brenkus', 45),
 ('susan', 'peters', 56)]
>>> pprint(sorted(persons, key=itemgetter(1)))
[('sarah', 'brenkus', 45),
 ('dee', 'camp', 48),
 ('raymond', 'hettinger', 54),
 ('susan', 'peters', 56),
 ('juliet', 'schmidt', 64)]
>>> pprint(sorted(persons, key=itemgetter(2)))
[('sarah', 'brenkus', 45),
 ('dee', 'camp', 48),
 ('raymond', 'hettinger', 54),
 ('susan', 'peters', 56),
 ('juliet', 'schmidt', 64)]
>>> 
>>> def last_first(person):
	return (person[1], person[0])

>>> pprint(list(map(last_first, persons)))
[('hettinger', 'raymond'),
 ('peters', 'susan'),
 ('camp', 'dee'),
 ('schmidt', 'juliet'),
 ('brenkus', 'sarah')]
>>> 
>>> person
('dee', 'camp', 48)
>>> last_person(person)
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    last_person(person)
NameError: name 'last_person' is not defined
>>> last_first(person)
('camp', 'dee')
>>> pprint(list(map(lambda p: (p[1], p[0]), persons)))
[('hettinger', 'raymond'),
 ('peters', 'susan'),
 ('camp', 'dee'),
 ('schmidt', 'juliet'),
 ('brenkus', 'sarah')]
>>> pprint(list(map(itemgetter(1, 0), persons)))
[('hettinger', 'raymond'),
 ('peters', 'susan'),
 ('camp', 'dee'),
 ('schmidt', 'juliet'),
 ('brenkus', 'sarah')]
>>> pprint(sorted(persons, key=itemgetter(1, 0)))
[('sarah', 'brenkus', 45),
 ('dee', 'camp', 48),
 ('raymond', 'hettinger', 54),
 ('susan', 'peters', 56),
 ('juliet', 'schmidt', 64)]
>>> # SELECT * FROM Persons ORDER BY lastname, firstname;
>>> 
>>> from statistics import mean, median, stdev
>>> list(map(itemgetter(2), persons))
[54, 56, 48, 64, 45]
>>> min(map(itemgetter(2), persons))
45
>>> max(map(itemgetter(2), persons))
64
>>> sum(map(itemgetter(2), persons))
267
>>> mean(map(itemgetter(2), persons))
53.4
>>> stdev(map(itemgetter(2), persons))
7.402702209328699
>>> median(map(itemgetter(2), persons))
54
>>> # SELECT MEDIAN(age) FROM Persons'
>>> 
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
red
yellow
blue
green

Task 8:  Show all of the cities, just once, in alpha order
austin
dallas
chicago
austin
houston
austin
chicago
dallas
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
red
yellow
blue
green

Task 8:  Show all of the cities, just once, in alpha order
chicago
houston
dallas
austin
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
red
yellow
blue
green

Task 8:  Show all of the cities, just once, in alpha order
austin
chicago
dallas
houston
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
red
yellow
blue
green
red
yellow
blue
green

Task 8:  Show all of the cities, just once, in alpha order
austin
chicago
dallas
houston
>>> chicago
houston
dallas
austin
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> # What is an iterator?
>>> # How does join work?
>>> # Why is set output sorted or not, randomly?
>>> 
>>> 
>>> 
>>> # Dictionaries and sets are implemented using hash tables.
>>> # In Python 3.7, dicts remember insertion order.  So, their display order is deterministics.
>>> # Howevers, display according to hash values, which a randomized on restart.
>>> 
>>> d = dict(raymond='red', rachel='blue', matthew='yellow')
>>> d            # Guaranteed: it will display raymond, then rachel, then matthew
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
>>> d = dict(matthew='yellow', rachel='blue', raymond='red')
>>> d
{'matthew': 'yellow', 'rachel': 'blue', 'raymond': 'red'}
>>> # https://www.youtube.com/watch?v=npw4s1QTmPg&t=1s        <== How dictionaries work internally
>>> s = {'raymond', 'rachel', 'matthew'}
>>> s
{'matthew', 'rachel', 'raymond'}
>>> abs(hash(matthew))
Traceback (most recent call last):
  File "<pyshell#377>", line 1, in <module>
    abs(hash(matthew))
NameError: name 'matthew' is not defined
>>> abs(hash('matthew'))
6454236455028489742
>>> abs(hash('matthew')) % 8
6
>>> abs(hash('raymond')) % 8
1
>>> abs(hash('rachel')) % 8
5
>>> 
=============================== RESTART: Shell ===============================
>>> abs(hash('matthew'))
7080549980732175302
>>> # In Python 3.7, dicts remember insertion order.  So, their display order is deterministics.
>>> # Sets just display in their hash order.  That hash is randomised on restart, so its order is non-deterministic.
>>> 
>>> # How does join work?
>>> 
>>> #   str.join(iterable-of-strings) -> a single string
>>> 
>>> names = 'raymond rachel matthew numtwo'.split()
>>> names
['raymond', 'rachel', 'matthew', 'numtwo']
>>> #   str.split() -> list_of_strings
>>> 
>>> #                  list_of_strings         ~   pile of bricks
>>> #   combine a pile of bricks to make a wall by putting mortar in between the bricks
>>> 
>>> #   mortar.join(pile_of_bricks) --> wall
>>> names = 'raymond rachel matthew numtwo'.split()
>>> names
['raymond', 'rachel', 'matthew', 'numtwo']
>>> ''.join(names)
'raymondrachelmatthewnumtwo'
>>> ' '.join(names)
'raymond rachel matthew numtwo'
>>> ', '.join(names)
'raymond, rachel, matthew, numtwo'
>>> '_'.join(names)
'raymond_rachel_matthew_numtwo'
>>> print('\n'.join(names))
raymond
rachel
matthew
numtwo
>>> print('\t'.join(names))
raymond	rachel	matthew	numtwo
>>> print(' <--> '.join(names))
raymond <--> rachel <--> matthew <--> numtwo
>>> print(' <--> '.join(sorted(names)))
matthew <--> numtwo <--> rachel <--> raymond
>>> 
>>> csv = 'raymond,rachel,matthew'
>>> csv.split(',')
['raymond', 'rachel', 'matthew']
>>> '\t'.join(csv.split(','))
'raymond\trachel\tmatthew'
>>> # 12:34:56.7
>>> #  1:35
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew

Task 2: Show all the colors and their ordinal position
1 -> red
2 -> blue
3 -> yellow
4 -> green
1 -> red
2 -> blue
3 -> yellow
4 -> green

Task 3: Show all the colors in reverse order
GREEN
YELLOW
BLUE
RED
Green
Yellow
Blue
Red

Task 4: Show the name and corresponding color, ignoring mismatches
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow
raymond -> red
rachel -> blue
matthew -> yellow

Task 5: Show all the colors in alphabetical order
blue
green
red
yellow

Task 6: Show all the colors by the length of the name
red
blue
green
yellow

Task 7: Sort the colors by the second letter of the color
red
yellow
blue
green
red
yellow
blue
green
red
yellow
blue
green

Task 8:  Show all of the cities, just once, in alpha order
austin
chicago
dallas
houston

Task 9: Show the names in reverse alphabetical order
raymond
rachel
matthew
>>> 
>>> 
>>> 
>>> # Database:                     Can be looped over                  ITERABLE
>>> # Query -> Cursor               Finger / reference / index          ITERATOR
>>> 
>>> # ITERABLEs can be IMMUTABLE == UNCHANGEABLE == READ-ONLY
>>> # ITERATORS change state so they can keep track of your current position
>>> states = ('delaware', 'pennsylvania',
	      'new jersey', 'alaska', 'hawaii')
>>> type(states)
<class 'tuple'>
>>> states[0] = 'california'
Traceback (most recent call last):
  File "<pyshell#426>", line 1, in <module>
    states[0] = 'california'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # The tuple is ITERABLE: has a method __iter__
>>> dir(states)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> states.__str__()
"('delaware', 'pennsylvania', 'new jersey', 'alaska', 'hawaii')"
>>> # print()                 __str__
>>> # with-statement          __enter__ __exit__
>>> # for-statement           __iter__
>>> # len()                   __len__
>>> # + operator              __add__
>>> # [] operator             __getitem__
>>> # in-operator             __contains__
>>> print(states)
('delaware', 'pennsylvania', 'new jersey', 'alaska', 'hawaii')
>>> with states:
	pass

Traceback (most recent call last):
  File "<pyshell#442>", line 1, in <module>
    with states:
AttributeError: __enter__
>>> for state in states:
	print(state.upper())

	
DELAWARE
PENNSYLVANIA
NEW JERSEY
ALASKA
HAWAII
>>> len(states)
5
>>> states + ('maryland', 'virginia')
('delaware', 'pennsylvania', 'new jersey', 'alaska', 'hawaii', 'maryland', 'virginia')
>>> states[0]
'delaware'
>>> states[2]
'new jersey'
>>> states[-1]
'hawaii'
>>> 'texas' in states
False
>>> 'alaska' in states
True
>>> states / 50
Traceback (most recent call last):
  File "<pyshell#453>", line 1, in <module>
    states / 50
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> states * 3
('delaware', 'pennsylvania', 'new jersey', 'alaska', 'hawaii', 'delaware', 'pennsylvania', 'new jersey', 'alaska', 'hawaii', 'delaware', 'pennsylvania', 'new jersey', 'alaska', 'hawaii')
>>> 
>>> 
>>> states = ('delaware', 'pennsylvania',
	      'new jersey', 'alaska', 'hawaii')
>>> # ITERABLE because it has __iter__
>>> it = iter(states)
>>> 
>>> type(states)
<class 'tuple'>
>>> type(it)
<class 'tuple_iterator'>
>>> dir(it)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
>>> # iter() -> iterator
>>> # next() -> value or StopIteration
>>> 
>>> states = ('delaware', 'pennsylvania',
	      'new jersey', 'alaska', 'hawaii')
>>> it = iter(states)
>>> it[0]
Traceback (most recent call last):
  File "<pyshell#469>", line 1, in <module>
    it[0]
TypeError: 'tuple_iterator' object is not subscriptable
>>> next(it)
'delaware'
>>> next(it)
'pennsylvania'
>>> next(it)
'new jersey'
>>> next(it)
'alaska'
>>> next(it)
'hawaii'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#475>", line 1, in <module>
    next(it)
StopIteration
>>> 
>>> 
>>> it = map(ord, 'Raymond')
>>> type(it)
<class 'map'>
>>> dir(it)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> next(it)
82
>>> next(it)
97
>>> next(it)
121
>>> next(it)
109
>>> next(it)
111
>>> next(it)
110
>>> next(it)
100
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#488>", line 1, in <module>
    next(it)
StopIteration
>>> 
>>> it = map(ord, 'Raymond')
>>> it
<map object at 0x111290e10>
>>> def mylist(iterator):
	result = []
	while True:
		try:
			value = next(iterator)
		except StopIteration:
			return result
		result.append(value)

		
>>> it = map(ord, 'Raymond')
>>> it
<map object at 0x111290dd8>
>>> mylist(it)
[82, 97, 121, 109, 111, 110, 100]
>>> it = map(ord, 'Raymond')
>>> list(it)
[82, 97, 121, 109, 111, 110, 100]
>>> 
>>> 
>>> def mylist(iterator):
	result = set()
	while True:
		try:
			value = next(iterator)
		except StopIteration:
			return result
		result.add(value)

		
>>> def myset(iterator):
	result = set()
	while True:
		try:
			value = next(iterator)
		except StopIteration:
			return result
		result.add(value)

		
>>> myset(map(ord, 'abracadabra'))
{97, 98, 99, 100, 114}
>>> 
>>> set(map(ord, 'abracadabra'))
{97, 98, 99, 100, 114}
>>> 
>>> # Hardware
>>> # Demming
>>> # Just in Time Manufacturing
>>> 
>>> 
>>> 
>>> 
>>> 
>>> range(100)
range(0, 100)
>>> it = iter(range(100))
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> sum(range(10_000_000))
49999995000000
>>> # 320Mb in Long Beach
>>> #          DRAM
>>> 
>>> # 56 bytes in Showroom
>>> #          L1
>>> 
>>> # You should learn to love iterators
>>> # They save memory
>>> # They let you do computation in L1 (cycle memory)
>>> 
>>> 
>>> s = range(10000000)
>>> import sys
>>> sys.getsizeof(s)
48
>>> it = iter(s)
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> del it
>>> def f(x):
	x += 10
	print(x)
	x += 100
	print(x)
	x += 1000
	print(x)

	
>>> f(1)      # += fast/doesn't burn bldg   print:slow/doesn't burn/puts data where you can't use it
11
111
1111
>>> import time
>>> start = time.perf_counter(); for i in range(10): f(i); time.perf_counter() - start
SyntaxError: invalid syntax
>>> def time_loop(n):
	start = time.perf_counter()
	for i in range(n):
		f(i)
	end = time.perf_counter()
	return end - start

>>> time_loop(10)
10
110
1110
11
111
1111
12
112
1112
13
113
1113
14
114
1114
15
115
1115
16
116
1116
17
117
1117
18
118
1118
19
119
1119
1.5838448290000997
>>> _ / 10
0.15838448290000998
>>> 0.158384482 * 10**9
158384482.0
>>> # 158,384,000 ns
>>> f(1)
11
111
1111
>>> def f(x):
	x += 10
	return x
	x += 100
	return x
	x += 1000
	return x

>>> f(1)
11
>>> y = f(1)
>>> y ** 2
121
>>> time_loop(10)
4.740999884234043e-06
>>> time_loop(10) / 10
4.5239999053592327e-07
>>> 1.5838448290000997 / time_loop(10) / 10
30605.69542383593
>>> def f(x):
	x += 10
	yield x
	x += 100
	yield x
	x += 1000
	yield x

	
>>> g = f(1)                    # A generator is a kind of iterator that runs code when you call next()
>>> g
<generator object f at 0x1112a71b0>
>>> dir(g)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
>>> y = next(g)
>>> y
11
>>> y = next(g)
>>> y
111
>>> y = next(g)
>>> y
1111
>>> y = next(g)
Traceback (most recent call last):
  File "<pyshell#591>", line 1, in <module>
    y = next(g)
StopIteration
>>> 
>>> 
>>> sum(f(1))
1233
>>> 
>>> 
>>> 
>>> # Iterators beat lists because 1) Lists eat memory like crazy 2) DRAM accesses slow 3) data can be wasted
>>> # Generator is a kind of iterator that runs code on demand (just-in-time)
>>> # Generators are the easiest way to create a new iterator from scratch
>>> # Write a simple function that prints what you want.  Turn the print() into a yield.
>>> 
>>> 
>>> for i, c in enumerate('Raymond'):
	print(i, '-->', c)

	
0 --> R
1 --> a
2 --> y
3 --> m
4 --> o
5 --> n
6 --> d
>>> for i, c in enumerate('Raymond', start=1):
	print(i, '-->', c)

	
1 --> R
2 --> a
3 --> y
4 --> m
5 --> o
6 --> n
7 --> d
>>> enumerate = None
>>> for i, c in enumerate('Raymond', start=1):
	print(i, '-->', c)

	
Traceback (most recent call last):
  File "<pyshell#611>", line 1, in <module>
    for i, c in enumerate('Raymond', start=1):
TypeError: 'NoneType' object is not callable
>>> 
>>> 
>>> def myenumerate(iterable, start=0):
	i = start
	for x in iterable:
		result = (i, x)
		print(result)
		i += 1

		
>>> myenumerate('Raymond')
(0, 'R')
(1, 'a')
(2, 'y')
(3, 'm')
(4, 'o')
(5, 'n')
(6, 'd')
>>> myenumerate('Raymond', start=1)
(1, 'R')
(2, 'a')
(3, 'y')
(4, 'm')
(5, 'o')
(6, 'n')
(7, 'd')
>>> def myenumerate(iterable, start=0):
	i = start
	for x in iterable:
		result = (i, x)
		yield result
		i += 1

		
>>> it = myenumerate('Raymond', start=1)
>>> it
<generator object myenumerate at 0x1112a7228>
>>> next(it)
(1, 'R')
>>> next(it)
(2, 'a')
>>> next(it)
(3, 'y')
>>> next(it)
(4, 'm')
>>> 
>>> 
>>> it = zip('Raymond', 'xyzpdqt')
>>> it
<zip object at 0x10e0ea648>
>>> next(it)
('R', 'x')
>>> next(it)
('a', 'y')
>>> next(it)
('y', 'z')
>>> zip = None
>>> it = zip('Raymond', 'xyzpdqt')
Traceback (most recent call last):
  File "<pyshell#639>", line 1, in <module>
    it = zip('Raymond', 'xyzpdqt')
TypeError: 'NoneType' object is not callable
>>> 
>>> 
>>> def myzip(s1, s2):
	it1 = iter(s1)
	it2 = iter(s2)
	while True:
		try:
			v1 = next(it1)
			v2 = next(it2)
		except StopIteration:
			return
		result = (v1, v2)
		print(result)

		
>>> myzip('Raymond', 'xyzpdqt')
('R', 'x')
('a', 'y')
('y', 'z')
('m', 'p')
('o', 'd')
('n', 'q')
('d', 't')
>>> def myzip(s1, s2):
	it1 = iter(s1)
	it2 = iter(s2)
	while True:
		try:
			v1 = next(it1)
			v2 = next(it2)
		except StopIteration:
			return
		result = (v1, v2)
		yield result

		
>>> it = myzip('Raymond', 'xyzpdqt')
>>> it
<generator object myzip at 0x1112a72a0>
>>> next(it)
('R', 'x')
>>> next(it)
('a', 'y')
>>> next(it)
('y', 'z')
>>> 
>>> 
>>> help(enumerate)
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> del None
SyntaxError: can't delete keyword
>>> del enumerate
>>> help(enumerate)
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |  
 |  Return an enumerate object.
 |  
 |    iterable
 |      an object supporting iteration
 |  
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |  
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

>>> list(enumerate('raymond', 0))
[(0, 'r'), (1, 'a'), (2, 'y'), (3, 'm'), (4, 'o'), (5, 'n'), (6, 'd')]
>>> list(enumerate('raymond'))
[(0, 'r'), (1, 'a'), (2, 'y'), (3, 'm'), (4, 'o'), (5, 'n'), (6, 'd')]
>>> list(enumerate('raymond', None))
Traceback (most recent call last):
  File "<pyshell#670>", line 1, in <module>
    list(enumerate('raymond', None))
TypeError: 'NoneType' object cannot be interpreted as an integer
>>> list(enumerate('raymond', start=None))
Traceback (most recent call last):
  File "<pyshell#671>", line 1, in <module>
    list(enumerate('raymond', start=None))
TypeError: 'NoneType' object cannot be interpreted as an integer
>>> def myenumerate(iterable, start=0):
	if start is None:
		start = 0
	i = start
	for x in iterable:
		result = (i, x)
		yield result
		i += 1

		
>>> list(myenumerate('abc', start=None))
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> 
>>> 
>>> enumerate = None
>>> 
>>> # locals()    ->    globals()     ->   builtins
>>> #                  enumerate=None      real enumerate
>>> 
>>> enumerate('abc', start=None)
Traceback (most recent call last):
  File "<pyshell#682>", line 1, in <module>
    enumerate('abc', start=None)
TypeError: 'NoneType' object is not callable
>>> 
>>> 
>>> 
>>> def count(start=0):
	i = start
	while True:
		print(i)
		i += 1

		
>>> count(start=5)
5
6
7
8
9
10
11
12
13
Traceback (most recent call last):
  File "<pyshell#692>", line 1, in <module>
    count(start=5)
  File "<pyshell#691>", line 4, in count
    print(i)
KeyboardInterrupt
>>> def count(start=0):
	i = start
	while True:
		yield i
		i += 1

		
>>> it = count(start=5)
>>> next(it)
5
>>> next(it)
6
>>> next(it)
7
>>> next(it)
8
>>> def count(start=0):
	i = start
	while True:
		yield i
		i += 1

		
>>> import time
>>> def timestamp():
	while True:
		yield time.ctime()

		
>>> it = timestamp()
>>> next(it)
'Tue Feb 12 15:05:08 2019'
>>> next(it)
'Tue Feb 12 15:05:12 2019'
>>> list(zip('abc', 'xyzpdq'))
Traceback (most recent call last):
  File "<pyshell#710>", line 1, in <module>
    list(zip('abc', 'xyzpdq'))
TypeError: 'NoneType' object is not callable
>>> del zip
>>> list(zip('abc', 'xyzpdq'))
[('a', 'x'), ('b', 'y'), ('c', 'z')]
>>> list(zip('abcdefghi', 'xyzpdq'))
[('a', 'x'), ('b', 'y'), ('c', 'z'), ('d', 'p'), ('e', 'd'), ('f', 'q')]
>>> 
>>> del zip
Traceback (most recent call last):
  File "<pyshell#715>", line 1, in <module>
    del zip
NameError: name 'zip' is not defined
>>> 
>>> 
>>> import time
>>> def count(start=0):
	i = start
	while True:
		yield i
		i += 1

		
>>> def timestamp():
	while True:
		yield time.ctime()

		
>>> it = zip('raymond', count(), timestamp())
>>> it
<zip object at 0x10e124cc8>
>>> next(it)
('r', 0, 'Tue Feb 12 15:08:15 2019')
>>> next(it)
('a', 1, 'Tue Feb 12 15:08:25 2019')
>>> next(it)
('y', 2, 'Tue Feb 12 15:08:31 2019')
>>> next(it)
('m', 3, 'Tue Feb 12 15:09:07 2019')
>>> def user_request():
	while True:
		req = input('State your business: ')
		if req == 'quit':
			break
		print(req)

		
>>> user_request()
State your business: get index.html
get index.html
State your business: post formdata
post formdata
State your business: head records.html
head records.html
State your business: get games.html
get games.html
State your business: quit
>>> def user_request():
	while True:
		req = input('State your business: ')
		if req == 'quit':
			break
		yield req

		
>>> 
>>> 
>>> import time
>>> def timestamp():
	while True:
		yield time.ctime()

		
>>> def count(start=0):
	i = start
	while True:
		yield i
		i += 1

		
>>> def user_request():
	while True:
		req = input('State your business: ')
		if req == 'quit':
			break
		yield req

		
>>> from pprint import pprint
>>> log = list(zip(count(), user_request(), timestamp()))
State your business: get index.html
State your business: post form.json
State your business: head games.html
State your business: quit
>>> pprint(log)
[(0, 'get index.html', 'Tue Feb 12 15:13:22 2019'),
 (1, 'post form.json', 'Tue Feb 12 15:13:45 2019'),
 (2, 'head games.html', 'Tue Feb 12 15:13:50 2019')]
>>> # RDH
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
>>> __doc__
' Fast, whirlwind tour of most of Pyton.\n    No time to stop and linger.\n    We can come back later and go into more detail.\n'
>>> print(__doc__)
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

>>> # repr, "repper", "reprsentation"
>>> #     shows the quotes,  \n, whitespace
>>> #     informative, but not pretty
>>> # str, "stir", "string"
>>> #     no quotes and the newlines actually print
>>> #     pretty but less informative
>>> 
>>> 30
30
>>> print(30)
30
>>> '30'
'30'
>>> print('30')
30
>>> 
>>> 
>>> 
>>> print('Three\nblind\nmice\n')
Three
blind
mice

>>> print('''Three
blind
mice
''')
Three
blind
mice

>>> print('Three\\nblind\\nmice\\n')
Three\nblind\nmice\n
>>> print('Three\nblind\nmice\n')  # Cooking the string
Three
blind
mice

>>> print(r'Three\nblind\nmice\n') # Raw string
Three\nblind\nmice\n
>>> print('C:\\\\My Documents and Settings\\Raymond\\text files\\course outline.doc')
C:\\My Documents and Settings\Raymond\text files\course outline.doc
>>> print(r'C:\\My Documents and Settings\Raymond\text files\course outline.doc')
C:\\My Documents and Settings\Raymond\text files\course outline.doc
>>> 
>>> # ' " ''' """
>>> print('don\'t you forget about me')
don't you forget about me
>>> print("don't you forget about me")
don't you forget about me
>>> # She said, "Hello, Raymond!"
>>> print('She said, "Hello, Raymond!"')
She said, "Hello, Raymond!"
>>> # She said, "Don't you forget about me"
>>> print('''She said, "Don't you forget about me"''')
She said, "Don't you forget about me"
>>> print("She said, \"Don't you forget about me\"")
She said, "Don't you forget about me"
>>> 
>>> 
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

>>> import grand_tour
Hello my name is: grand_tour
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

>>> # Mechanism:
>>> #    By default, the value of __name__ is '__main__'
>>> #    When you import, the __name__ is changed
>>> #    to filename of the module without the .py
>>> 
>>> # We can exploit this mechanism to learn
>>> #    whether the module was imported of not.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
>>> import grand_tour
Hello my name is: grand_tour
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Oh no! I was imported
>>> import random
>>> random.randrange(1000)
851
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
>>> square.__class__
<class 'function'>
>>> type(square)
<class 'function'>
>>> square.__name__
'square'
>>> square.__doc__
'Return a value times itself'
>>> square.__code__.co_code
b'|\x00|\x00\x14\x00S\x00'
>>> list(_)
[124, 0, 124, 0, 20, 0, 83, 0]
>>> square.__module__
'__main__'
>>> type(square).__name__
'function'
>>> 
>>> 
>>> __doc__
' Fast, whirlwind tour of most of Pyton.\n    No time to stop and linger.\n    We can come back later and go into more detail.\n'
>>> square.__doc__
'Return a value times itself'
>>> __name__
'__main__'
>>> square.__name__
'square'
>>> 
>>> 
>>> help(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> help = None
>>> help(square)
Traceback (most recent call last):
  File "<pyshell#818>", line 1, in <module>
    help(square)
TypeError: 'NoneType' object is not callable
>>> type(square)
<class 'function'>
>>> type(square).__name__
'function'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
>>> myhelp(square)
Help on function
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
>>> myhelp(square)
Help on function in module __main__:
>>> 
>>> type(square)
<class 'function'>
>>> type(square).__name__
'function'
>>> square.__module__
'__main__'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
>>> print()

>>> myhelp(square)
Help on function in module __main__:

>>> x = 10
>>> print(f'The answer is {x ** 2}')
The answer is 100
>>> print(f'The answer')
The answer
>>> print(f"The answer")
The answer
>>> print(F"Yes!")
Yes!
>>> #       F"Yes!"
>>> print(f'The answer is {x ** 2}')
The answer is 100
>>> print('The answer is {x ** 2}')
The answer is {x ** 2}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
>>> help(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> myhelp(square)
Help on function in module __main__:

Return a value times itself

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
>>> square.__code__.co_varnames
('x',)
>>> varnames = ('abc', 'x', 'lmno')
>>> varnames
('abc', 'x', 'lmno')
>>> ', '.join(varnames)
'abc, x, lmno'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function in module __main__:

square(x)
Return a value times itself

>>> square.__name__
'square'
>>> 
>>> varnames = ('abc', 'x', 'lmno')
>>> print(''.join(varsnames))
Traceback (most recent call last):
  File "<pyshell#846>", line 1, in <module>
    print(''.join(varsnames))
NameError: name 'varsnames' is not defined
>>> print(''.join(varnames))
abcxlmno
>>> print('_'.join(varnames))
abc_x_lmno
>>> print(', '.join(varnames))
abc, x, lmno
>>> print(", ".join(varnames))
abc, x, lmno
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function in module __main__:

square(x)
Return a value times itself

>>> s = 'three\nblind    mice\n'
>>> s.split()
['three', 'blind', 'mice']
>>> s.splitlines()
['three', 'blind    mice']
>>> 
>>> 
>>> for line in s.splitlines():
	print(line)

	
three
blind    mice
>>> print(s)
three
blind    mice

>>> for line in s.splitlines():
	print('   ', line)

	
    three
    blind    mice
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function in module __main__:

square(x)
    Return a value times itself

>>> ne)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> myhelp(square)
Help on function in module __main__:

square(x)
    Return a value times itself

>>> help(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> myhelp(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> myhelp(myhelp)
Help on function myhelp in module __main__:

myhelp(obj, line)
     Home built help utility
    
            Runs something like help
            to instropsect an object
            to learn more about it
        

>>> print(myhelp.__doc__)
 Home built help utility

        Runs something like help
        to instropsect an object
        to learn more about it
    
>>> from textwrap import dedent
>>> print(dedent(myhelp.__doc__))
Home built help utility

       Runs something like help
       to instropsect an object
       to learn more about it

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> myhelp(pow)
Help on builtin_function_or_method pow in module builtins:

Traceback (most recent call last):
  File "<pyshell#874>", line 1, in <module>
    myhelp(pow)
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 35, in myhelp
    print(f'{obj.__name__}({", ".join(obj.__code__.co_varnames)})')
AttributeError: 'builtin_function_or_method' object has no attribute '__code__'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> '__code__'
'__code__'

>>> 
>>> 
>>> 
>>> myhelp(pow)
Help on builtin_function_or_method pow in module builtins:

pow()
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
>>> list(map(pow, range(10), [2]*10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [2] * 10
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
>>> list(zip(range(10), [2]*10))
[(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2)]
>>> [pow(0, 2), pow(1, 2), pow(3, 2), pow(4, 2)]
[0, 1, 9, 16]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
>>> raise ClassOverError('5:30pm')
Traceback (most recent call last):
  File "<pyshell#885>", line 1, in <module>
    raise ClassOverError('5:30pm')
ClassOverError: 5:30pm
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
>>> myhelp(ClassOverError)
Help on type ClassOverError in module __main__:

ClassOverError()
    Signals the end of the Python course

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 57, in <module>
    print(s[10])
IndexError: list index out of range
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Oops, I did it again. I indexed too far. I'm not that innocent.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Oops, I did it again. I indexed too far. I'm not that innocent.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Oops, I did it again. I indexed too far. I'm not that innocent.
This always runs
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
piece of me
This always runs
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
piece of me
Hey, it ran perfectly
This always runs
>>> # SyntaxError  TypeError   ValueError   IndexError   KeyError  IOError   OSError  RuntimeError
>>> # ZeroDivisionError
>>> 1 / 0
Traceback (most recent call last):
  File "<pyshell#889>", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
>>> 0 / 0
Traceback (most recent call last):
  File "<pyshell#890>", line 1, in <module>
    0 / 0
ZeroDivisionError: division by zero
>>> 0 / 0
Traceback (most recent call last):
  File "<pyshell#891>", line 1, in <module>
    0 / 0

ZeroDivisionError: division by zero
>>> # Is there a catchall? Yes.
>>> # Should you use it, generally no.
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
The index was bad
This always runs
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
The index was bad
This always runs
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
ERROR:root:Something bad happened but not an KeyError or IndexError
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 60, in <module>
    print(ss[1])
NameError: name 'ss' is not defined
This always runs
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
>>> issubclass(KeyError, LookupError)
True
>>> issubclass(IndexError, LookupError)
True
>>> 
>>> 
>>> 
>>> e = KeyError('charlie')
>>> 
>>> isinstance(e, KeyError)
True
>>> type(e)
<class 'KeyError'>
>>> type(e).__name__
'KeyError'
>>> e.args
('charlie',)
>>> 
>>> raise KeyError('charlie')
Traceback (most recent call last):
  File "<pyshell#906>", line 1, in <module>
    raise KeyError('charlie')
KeyError: 'charlie'
>>> 
>>> 
>>> 
>>> # Exceptions are classes
>>> # You can make new exceptions by subclassing
>>> # Raising an exception creates an instance of the class
>>> # try/except catches the exception
>>> #     if isinstance(e, LookupError)
>>> # generally, we tightly match the exception category
>>> #     to the handler (the solution for the problem)
>>> # generally, if you don't expect a problem
>>> #     or you don't a solution to it
>>> #     then don't write an except clause
>>> # IOW: catch only exceptions that you expect and can fix.
>>> # It is rare to write a catchall because you might
>>> #     catch too much.
>>> 
>>> # "Exception" catches everything but KeyboardInterrupt and SystemExit
>>> # If really want everything, use "BaseException"
>>> s = ['raymond', 'rachel', 'matthew']
>>> s = ['raymond', 'rachel', 'matthew',]
>>> s = [
	'raymond',
	'rachel',
	'matthew',
]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 89, in <module>
    print(brand['mindy'])
KeyError: 'mindy'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 89, in <module>
    print(brand['mindy'])
KeyError: 'mindy'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
done
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 105, in <module>
    print(brands.keys())
NameError: name 'brands' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
>>> s
{40, 10, 50, 20, 30}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/grand_tour.py", line 123, in <module>
    print(s.different(t))
AttributeError: 'set' object has no attribute 'different'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
{10, 20, 30}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
{10, 20, 30}
{60, 70}
>>> 
>>> 
>>> 
>>> even = {2, 4, 6, 8, 10}
>>> prime = {2, 4, 5, 7, 11}
>>> even.union(prime)
{2, 4, 5, 6, 7, 8, 10, 11}
>>> even.intersection(prime)
{2, 4}
>>> prime - even
{11, 5, 7}
>>> even - prime
{8, 10, 6}
>>> 
>>> # Sets are your most powerful tool for data analysis
>>> # Reach for them first
>>> 
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
{10, 20, 30}
{60, 70}
{70, 40, 10, 50, 20, 60, 30}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/grand_tour.py =========
Hello my name is: __main__
What I like to do:
 Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.

Woohoo! I was directly with F5
7.0
49
Help on function square in module __main__:

square(x)
    Return a value times itself

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[-72, -69, -60, -45, -24, 3, 36, 75, 120, 171]
Caught a NameError
This always runs
<class 'dict'>
3
True
False
pc
Mindy does not have a computer
Susan does not have a computer
Sheila does not have a computer
dict_keys(['raymond', 'rachel', 'matthew'])
dict_values(['mac', 'pc', 'vtech'])
dict_items([('raymond', 'mac'), ('rachel', 'pc'), ('matthew', 'vtech')])
<class 'set'>
5
True
False
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
{10, 20, 30}
{60, 70}
{70, 40, 10, 50, 20, 60, 30}
{40, 50}
{10, 20, 30}
>>> 
>>> 
>>> # r:  RICH
>>> # t:  TALL
>>> # Bring over all the RICH people AND bring the TALL ones too
>>> #                                 ^-- more
>>> # Bring over all the people who are RICH AND TALL
>>> #                                         ^-- fewer
>>> 
>>> # Coke and fries -> nothing
>>> 
>>> 
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> for method in dir(list):
	if not method.startswith('__'):
		print(method.upper())

		
APPEND
CLEAR
COPY
COUNT
EXTEND
INDEX
INSERT
POP
REMOVE
REVERSE
SORT
>>> 
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> len(dir(list)) - len(dir(tuple))
13
>>> set(dir(list)) - set(dir(tuple))
{'__delitem__', 'insert', 'copy', 'reverse', '__setitem__', 'sort', 'remove', 'extend', 'clear', '__iadd__', '__reversed__', 'pop', 'append', '__imul__'}
>>> sorted(set(dir(list)) - set(dir(tuple)))
['__delitem__', '__iadd__', '__imul__', '__reversed__', '__setitem__', 'append', 'clear', 'copy', 'extend', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> print('\n'.join(sorted(set(dir(list)) - set(dir(tuple)))))
__delitem__
__iadd__
__imul__
__reversed__
__setitem__
append
clear
copy
extend
insert
pop
remove
reverse
sort
>>> print('\n'.join(sorted(set(dir(list)) - set(dir(tuple)))).upper())
__DELITEM__
__IADD__
__IMUL__
__REVERSED__
__SETITEM__
APPEND
CLEAR
COPY
EXTEND
INSERT
POP
REMOVE
REVERSE
SORT
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> 
>>> 
