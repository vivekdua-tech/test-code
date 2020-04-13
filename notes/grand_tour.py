''' Fast, whirlwind tour of most of Pyton.
    No time to stop and linger.
    We can come back later and go into more detail.
'''

print('Hello my name is:', __name__)
print('What I like to do:')
print(__doc__)

if __name__ == '__main__':
    print('Woohoo! I was directly with F5')
else:
    print('Oh no! I was imported')

## Functions ############################################

from textwrap import dedent
import math

print(math.sqrt(49))

def square(x):
    'Return a value times itself'
    return x * x

def myhelp(obj):
    ''' Home built help utility

        Runs something like help
        to instropsect an object
        to learn more about it
    '''
    print(f'Help on {type(obj).__name__} {obj.__name__} in module {obj.__module__}:')
    print()
    try:
        print(f'{obj.__name__}({", ".join(obj.__code__.co_varnames)})')
    except AttributeError:
        print(f'{obj.__name__}()')
    for line in dedent(obj.__doc__).splitlines():
        print('    ', line, sep='')
    print()

print(square(7))
myhelp(square)

print([square(0), square(1), square(2), square(3), square(4), square(5), square(6), square(7), square(8), square(9)])
print([square(x) for x in range(10)])               # List comprehension
print(list(map(square, range(10))))                 # map()
print(list(map(lambda x: 3*x**2 - 72, range(10))))  # lambda means "make function"

## Exceptions ####################################

import logging

class ClassOverError(Exception):                    # Exceptions are classes. Make new exceptions by subclassing
    'Signals the end of the Python course'

s = ['baby one more time', 'toxic', 'piece of me']
try:
    print(ss[1])
except KeyError:                            # Run this handler when there is a KeyError from dictionaries
    print("Doh! I can't find the key")
except (IndexError, RuntimeError):                          # Run this handler when there is an IndexError from lists, tuples, or strings 
    print("Oops, I did it again. I indexed too far. I'm not that innocent.")
except Exception as e:                      # This catches ALL exceptions, but it usually catches too much.
    if isinstance(e, NameError):
        print('Caught a NameError')
    else:
        logging.exception('Something bad happened but not an KeyError or IndexError')
else:                                       # Run this, when there is no error at all
    print('Hey, it ran perfectly')
finally:                                    # Run this always (if there is an error or if there isn't)
    print('This always runs')

## Dictionaries #####################################

brand = {                                   # dict literals have curly braces AND colons    
    'raymond': 'mac',
    'rachel': 'pc',
    'matthew': 'vtech',
}

print(type(brand))                  # brand.__class__
print(len(brand))                   # brand.__len__()
print('rachel' in brand)            # brand.__contains__('rachel')
print('mindy' in brand)
print(brand['rachel'])              # brand.__getitem__('rachel')

# EAFP -- Easier to ask forgiveness, than permission
try:
    print(brand['mindy'])
except KeyError:
    print('Mindy does not have a computer')

# LBYL -- Look before you leap
if 'susan' in brand:
    print(brand['susan'])
else:
    print('Susan does not have a computer')

# Unconditional lookup -- unlike [], it never fails
print(brand.get('sheila', 'Sheila does not have a computer'))

# Inspection tools
print(brand.keys())
print(brand.values())
print(brand.items())


## Sets ##############################
#         Literal notation: Curly braces without colons

s = {10, 20, 30, 40, 20, 30, 50}
print(type(s))
print(len(s))      # Sets are unordered and eliminate duplicates
print(20 in s)     # Fast membership testing
print(90 in s)

t = {40, 50, 60, 70}

print(s.union(t))   # Set to set analysis operations
print(s.intersection(t))
print(s.difference(t))
print(t.difference(s))

print(s | t)        # Pipe operator, "or", union
print(s & t)        # Ampersand operator, "and", intersection
print(s - t)        # Minus operotor, difference

# Recommendation: spell-out union() and intersection()
# but use the minus-sign for difference.

# Sets should be your number one tool for data analysis
print(sorted(set(dir(list)) - set(dir(tuple))))

# Uniquifiction or deduping
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
print(sorted(set(colors)))

# Fast membership testing
supported_extensions = {'html', 'txt', 'css', 'xml', 'php'}
url = 'http://cisco.com/games/funstuff/monopoly.php'
head, ext = url.rsplit('.', 1)
if ext in supported_extensions:
    print('Yes, we can!')
else:
    print("No, we can't. #MPGA")

## List ###################################################
#         Literal notation: Square brackets   
#         Ordered collection that allow duplicates
#         Mutable, dynamic, variant array

starks = ['eddard', 'catelyn', 'robb', 'jon snow',
          'sansa', 'arya', 'brandon', 'rickon']

print(type(starks))
print(len(starks))
print(starks[0])
print(starks[-1])
print(starks[:2])
print(starks[-2:])

starks.append('danyres')
print(starks)
print(starks.pop())    # append/pop implement a LIFO starks
print(starks)

try:
    print(starks[50])
except IndexError:
    print('There is no 50th stark')

print(starks.sort())   # In Python, returning None is a hint the object mutated
print(starks)
print(starks.reverse())
print(starks)

## String Formatting #####################################

import sys

new = 10
old = 20
word = 'Howdy!'

print(new, old, word, file=sys.stderr)                     # fprintf(stderr, "%d %d %s\n", new, old, word);
print(50 ** 2)                                             #                           ^-- end is a newline
                                                           #                    ^--------- separator is a space
print(new, old, word, sep='~')
print(new, old, word, sep='', end='_')
print(75 ** 2)

# Old-style formattng is like C-style
print('The answer is %d today but was %d yesterday' % (new, old))
#                                                     ^^^^^^^^^^---- The input is a tuple
#                                                   ^--------------- String formatting operator (string interpolation operator)
#                    ^-----------------^---------------------------- Placeholders
print('There are two ways to display as string: %s and %r' % (word, word))
print('The answer is %(new)d today but was %(old)d yesterday' % {'old': 20, 'new': 10})

# New-style formatting is like C#-style

spanish = {
    'The answer is {0} today but was {1} yesterday': 'Ayer, la repuesta estaba {1}, pero hoy la repuesta esta {0}',
}

german = {
    'The answer is {0} today but was {1} yesterday': 'Die Antwort ist {0} heute, aber gestern {1}',
}

eng = {}

lang = german

def _(phrase):
    return lang.get(phrase, phrase)

print(_('The answer is {0} today but was {1} yesterday').format(new, old))
#                                         o---------------------------^
#                       o-----------------------------------------^
print('The answer is {new} today but was {old} yesterday'.format(old=20, new=10))
#                                          o------------------------^
#                      o----------------------------------------------------^
print('The answer is {new} today but was {old} yesterday'.format(old=old, new=new))
print(f'The answer is {new} today but was {old} yesterday')

## How do I get data out of a file?

f = open('notes/hamlet.txt')
try:
    play = f.read()
    print(len(play)) 
finally:
    f.close()

with open('notes/hamlet.txt') as f:
    play = f.read()
    print(len(play))     
    
## How do I get data from a url

from urllib.request import urlopen

u = urlopen('http://www.perl.org')
try:
    website = u.read().decode()
    print(len(website))
finally:    
    u.close()

with urlopen('http://www.perl.org') as u:
    website = u.read().decode()
    print(len(website))    

## More codecs #########################################

color = dict(raymond='red', rachel='blue', matthew='yellow')
print(color)
print(color['matthew'])
print(type(color))

import json, pickle, marshal, urllib.parse

s1 = json.dumps(color)
s2 = pickle.dumps(color)
s3 = marshal.dumps(color)
s4 = urllib.parse.urlencode(color)

print([type(s) for s in [s1, s2, s3, s4]])
print([len(s) for s in [s1, s2, s3, s4]])

d1 = json.loads(s1)
d2 = pickle.loads(s2)
d3 = marshal.loads(s3)
d4 = urllib.parse.parse_qs(s4)


