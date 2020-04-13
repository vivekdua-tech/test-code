Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> type(x)
<class 'int'>
>>> y = 'hello'
>>> type(y)
<class 'str'>
>>> z = x
>>> 
>>> x
10
>>> y
'hello'
>>> z
10
>>> id(x)
4344212944
>>> hex(id(x))
'0x102ef6dd0'
>>> hex(id(z))
'0x102ef6dd0'
>>> z += 1
>>> x
10
>>> z
11
>>> hex(id(x))
'0x102ef6dd0'
>>> hex(id(z))
'0x102ef6df0'
>>> x = y
>>> x
'hello'
>>> type(x)
<class 'str'>
>>> # In C, the type is associated with the variable name
>>> # and the data doesn't know its own type.
>>> 
>>> # In Python, the type is associated with a object (the data knows its own type).
>>> # and the variables DON'T HAVE A type.
>>> hex(id(y))
'0x1067fcf10'
>>> hex(id(x))
'0x1067fcf10'
>>> hex(id(z))
'0x102ef6df0'
>>> 
>>> x = 10
>>> type(x)
<class 'int'>
>>> # Foolishly believe, the gives you the type of "x"
>>> 
>>> y = x + 1
>>> y
11
>>> type(10)
<class 'int'>
>>> # What it really does: asks the 10, what is your type.
>>> 
>>> x = 10
>>> x = 12345
>>> import sys
>>> sys.getrefcount(x)
2
>>> y = x            # Assignments NEVER make copies
>>> x
12345
>>> y
12345
>>> id(x) == id(y)
True
>>> sys.getrefcount(x)
3
>>> del y
>>> sys.getrefcount(x)
2
>>> x.__class__
<class 'int'>
>>> x.__class__.__name__
'int'
>>> del x
>>> x = 10
>>> pow(2, x)
1024
>>> 10 + 3 + 5 - 2
16
>>> 10 + 3
13
>>> 10 + 3 + 18
31
>>> x= 10
>>> x += 1
>>> x
11
>>> # qsort(list_of_pointers)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # In big C programs, you usually end-up doing
>>> # what Python is already doing.
>>> 
>>> # The implementation of Python is internally
>>> # much more optimized than what I showed you.
>>> 
>>> # If you write your own sort, it will be 100x slower than C
>>> # But, if you use our sort, it will be faster than what
>>> # most people write in C.
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/sj195/how_for_loops_works.py ====
0
1
2
3
4
5
6
7
8
9
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/sj195/how_for_loops_works.py ====
0
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/sj195/how_for_loops_works.py ====
0
1
2
3
4
5
6
7
8
9
9
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
==== RESTART: /Users/raymond/Dropbox/Public/sj195/how_for_loops_works.py ====
0
1
2
3
4
5
6
7
8
9
5
>>> for name in ['raymond', 'rachel', 'matthew']:
	print(name.capitalize())

	
Raymond
Rachel
Matthew
>>> for name in ['raymond', 'rachel', 'matthew']:
	print(name.capitalize())
	name = 'tom'

	
Raymond
Rachel
Matthew
>>> name
'tom'
>>> 
>>> # Simplified answer
>>> # Roughly:
>>> # local variables in a function
>>> # globals variables within a module
>>> # builtins is pre import module
>>> len('hello')
5
>>> # locals() -> globals() -> builtins -> NameError
>>> x = 10
>>> y = 20
>>> def f(x):
	print(x, x**2, y)

	
>>> f(5)
5 25 20
>>> x
10
>>> def f(x):
	print(x, x**2, y, len('computer'))

	
>>> f(5)
5 25 20 8
>>> def len(obj):
	return 420

>>> __builtins__.len('computer')
8
>>> len('computer')
420
>>> f(5)
5 25 20 420
>>> del len
>>> f(5)
5 25 20 8
>>> def f(x):
	print(x, x**2, y, len('computer'), xyzpdq)

	
>>> f(5)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    f(5)
  File "<pyshell#112>", line 2, in f
    print(x, x**2, y, len('computer'), xyzpdq)
NameError: name 'xyzpdq' is not defined
>>> 
>>> 
>>> # Refrigator magnet programming
>>> # Programming on Purpose
>>> 
>>> import collections
>>> collecktions.Counter()
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    collecktions.Counter()
NameError: name 'collecktions' is not defined
>>> for i in range(10):
	print(i)
	 print(i ** 2)
	 
SyntaxError: unexpected indent
>>> for i in range(10):
	print(i)
	print(i ** 2)

	
0
0
1
1
2
4
3
9
4
16
5
25
6
36
7
49
8
64
9
81
>>> random.choice('abc')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    random.choice('abc')
NameError: name 'random' is not defined
>>> import random
>>> 
>>> # NameError:   Either you didn't assign the variable or you misspelled it
>>> # Python 3.7.2  fresh install from python.org
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> # 1:35
>>> # http://bit.ly/python-sj195
>>> # Red
>>> # Install Python 3.7.2
>>> # http://www.python.org
>>> 
>>> # Quoting characters: ' " ''' """
>>> print('hello')
hello
>>> print("hello")
hello
>>> print('''hello''')
hello
>>> print("""hello""")
hello
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> ''hello''')
hell
SyntaxError: invalid syntax
>>> 


>>> 

>>> # __doc__
>>> print(__doc__)
Scan a log file from a NASA server
>>> # Dunder doc
>>> 
>>> # __head__
>>> __name__
'__main__'
>>> __name__ == '__main__'
True
>>> 
>>> # Docstrings are for users of the code
>>> # Comments are for maintainers of the code
>>> 
>>> # Maintenance manual is comments
>>> # User manual is the docstring
>>> 
=============================== RESTART: Shell ===============================
>>> import overview
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> overview.mo
<re.Match object; span=(25, 72), match='GET\t/shuttle/countdown/video/livevideo.jpeg\t200>
>>> overview.line
'192.94.94.33\t-\t807303121\tGET\t/shuttle/countdown/video/livevideo.jpeg\t200\t40960\t\t\n'
>>> type(overview)
<class 'module'>
>>> type({})
<class 'dict'>
>>> type('hello')
<class 'str'>
>>> def happy():
    print('Woohoo!')

    
>>> happy()
Woohoo!
>>> type(happy)
<class 'function'>
>>> class A:
    x = 10

    
>>> a = A()
>>> b = A()
>>> a.y = 20
>>> b.y = 30
>>> 
>>> type(a)
<class '__main__.A'>
>>> type(b)
<class '__main__.A'>
>>> type(A)
<class 'type'>
>>> type(type)
<class 'type'>
>>> 
>>> a.y
20
>>> b.y
30
>>> a.x
10
>>> b.x
10
>>> # Shared information goes in the class
>>> # Unique information goes in the instance
>>> 
>>> class Employee:
        company = 'Cisco'
        logo = 'Bridge'

        
>>> a = Employee()
>>> a.suchita
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    a.suchita
AttributeError: 'Employee' object has no attribute 'suchita'
>>> a.name = 'suchita'
>>> a.gender = 'female'
>>> b = Employee()
>>> b.name = 'yipu'
>>> b.gender = 'male'
>>> 
>>> 
>>> a.name
'suchita'
>>> b.name
'yipu'
>>> a.logo
'Bridge'
>>> b.logo
'Bridge'
>>> 
>>> a.gender
'female'
>>> b.gender
'male'
>>> 
>>> a.gas = 'full'
>>> b.gas = 'half'
>>> 
>>> a.gas
'full'
>>> b.gas
'half'
>>> b.gas = 'full'
>>> b.gas
'full'
>>> b.gas = 'half'
>>> 
>>> 
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> collections
<module 'collections' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/collections/__init__.py'>
>>> glob
<module 'glob' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/glob.py'>
>>> __doc__
'Scan a log file from a NASA server'
>>> 
>>> type(visited)
<class 'collections.Counter'>
>>> Counter
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    Counter
NameError: name 'Counter' is not defined
>>> collections.Counter
<class 'collections.Counter'>
>>> 
>>> pow(2, 5)
32
>>> Counter
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    Counter

NameError: name 'Counter' is not defined

>>> 
>>> visited = collections.Counter()
>>> visitor = collections.Counter()
>>> 
>>> visited['France']
0
>>> visited['France'] += 1
>>> visited['France']
1
>>> visited['France'] += 1
>>> visited['France']
2
>>> 
>>> 
>>> visited = collections.Counter()
>>> visitor = collections.Counter()
>>> visited['France'] + 1; visitor['Raymond'] += 1
1
>>> visited['France'] + 1; visitor['Rachel'] += 1
1
>>> visited['France']
0
>>> 
>>> 
>>> 
>>> visited = collections.Counter()
>>> visitor = collections.Counter()
>>> visited['France'] += 1; visitor['Raymond'] += 1
>>> visited['France'] += 1; visitor['Rachel'] += 1
>>> visited['France']
2
>>> visitor['Raymond']
1
>>> visitor['Rachel']
1
>>> visited['Germany'] += 1; visitor['Raymond'] += 1
>>> visited['Russia'] += 1; visitor['Raymond'] += 1
>>> visited
Counter({'France': 2, 'Germany': 1, 'Russia': 1})
>>> visitor
Counter({'Raymond': 3, 'Rachel': 1})
>>> import math
>>> math.cos(3.0) + math.sin(2 * math.pi)
-0.9899924966004456
>>> 
>>> import random
>>> random.randrange(1000000)
569641
>>> random.randrange(10)
9
>>> random.randrange(10)
8
>>> # 1990 -- All Python Users were Linux/Unix users
>>> # 1990 -- Almost all Linux programmers knew Bash / C
>>> # 1990 -- Bash called expanding "*.jpg" as "globbing"
>>> 2019 - 1990
29
>>> # 1990 -- #Yolo
>>> # # Covfefe
>>> 
>>> # 1990 -- People had little food and no energy
>>> #  list -> ls
>>> #          fsck
>>> #  san francisco -> cisco
>>> #  show ipv4 int bri
>>> #  show ipv4 int brief
>>> 
>>> # pretty_print   pprint     pp   xz
>>> 
>>> # pip <-- copy
>>> 
>>> # great_name -> worse_name
>>> # regex      -> re
>>> v1 = collections.Counter()
>>> v2 = collections.Counter()
>>> glob.glob('notes/*.log')
['notes/nasa_19950801.log']
>>> type([])
<class 'list'>
>>> type(())
<class 'tuple'>
>>> type('')
<class 'str'>
>>> type("")
<class 'str'>
>>> type('''hello''')
<class 'str'>
>>> # I can loop over a "list".
>>> # A list can be looped over.
>>> # A list can be used with the for-statement
>>> # A list is ITERABLE
>>> 
>>> for c in 'Raymond':
        print(c.upper())

        
R
A
Y
M
O
N
D
>>> pow(2, 5)
32
>>> 
>>> import threading
>>> printer_lock = threading.Lock()
>>> 
>>> printer_lock.acquire()
True
>>> print('Crit section 1')
Crit section 1
>>> print('Crit section 2')
Crit section 2
>>> printer_lock.release()
>>> 
>>> with printer_lock:
       print('C1')
       print('C2')

       
C1
C2
>>> dir(printer_lock)
['__class__', '__delattr__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'acquire', 'acquire_lock', 'locked', 'locked_lock', 'release', 'release_lock']
>>> dir(f)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
>>> dir('hello')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir([])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> s = 'hello'
>>> for c in s:
    print(c.upper())

    
H
E
L
L
O
>>> it = s.__iter__()
>>> type(it)
<class 'str_iterator'>
>>> c = it.__next__()
>>> c
'h'
>>> c = it.__next__()
>>> c
'e'
>>> c = it.__next__()
>>> c
'l'
>>> c = it.__next__()
>>> c
'l'
>>> c = it.__next__()
>>> c
'o'
>>> c = it.__next__()
Traceback (most recent call last):
  File "<pyshell#339>", line 1, in <module>
    c = it.__next__()
StopIteration
>>> # Now hiring a director of iteration:
>>> #   Responsible for a clean iterface to all iterating engineers in the company
>>> #   Skills required:  __iter__ -> it     it.__next__    StopIteration
>>> 
>>> e1 = 'happy'
>>> e2 = ['rachel', 'raymond', 'matthew']
>>> type(e1)
<class 'str'>
>>> type(e2)
<class 'list'>
>>> 
>>> it = e1.__iter__()
>>> while True:
        try:
             c = it.__next__()
        except StopIteration:
             break
        d = c.upper()
        e = d.__str__()
        f = sys.stdout.write(e)
        g = sys.stdout('\n')

        
Traceback (most recent call last):
  File "<pyshell#359>", line 8, in <module>
    f = sys.stdout.write(e)
NameError: name 'sys' is not defined

>>> import sys
>>> it = e1.__iter__()
>>> while True:
        try:
             c = it.__next__()
        except StopIteration:
             break
        d = c.upper()
        e = d.__str__()
        f = sys.stdout.write(e)
        g = sys.stdout('\n')

        
HTraceback (most recent call last):
  File "<pyshell#363>", line 9, in <module>
    g = sys.stdout('\n')
TypeError: 'PseudoOutputFile' object is not callable
>>> 
>>> 
>>> import sys
>>> it = e1.__iter__()
>>> while True:
        try:
             c = it.__next__()
        except StopIteration:
             break
        d = c.upper()
        e = d.__str__()
        f = sys.stdout.write(e)
        g = sys.stdout.write('\n')

        
H
A
P
P
Y
>>> type(e1)
<class 'str'>
>>> it = e2.__iter__()
>>> while True:
        try:
             c = it.__next__()
        except StopIteration:
             break
        d = c.upper()
        e = d.__str__()
        f = sys.stdout.write(e)
        g = sys.stdout.write('\n')

        
RACHEL
RAYMOND
MATTHEW
>>> # Job title: for-statement
>>> for c in e1:
        print(c.upper())

        
H
A
P
P
Y
>>> for c in e2:
        print(c.upper())

        
RACHEL
RAYMOND
MATTHEW
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> x = 10
>>> y = 20
>>> x.__add__(y)
30
>>> x + y
30
>>> 
>>> x = 'hello'
>>> y = ' world'
>>> x + y
'hello world'
>>> search
Traceback (most recent call last):
  File "<pyshell#389>", line 1, in <module>
    search
NameError: name 'search' is not defined
>>> re
<module 're' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/re.py'>
>>> re.search
<function search at 0x107353b70>
>>> re
<module 're' from '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/re.py'>

>>> 
>>> d = {'raymond': 'red', 'rachel': 'blue'}
>>> type(d)
<class 'dict'>
>>> d['raymond']
'red'
>>> s = [10.1, 15.2, 5.2]
>>> s[1]
15.2
>>> type(s)
<class 'list'>
>>> 
>>> d.__getitem__('raymond')
'red'
>>> s.__getitem__(1)
15.2
>>> 
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> type(pprint)
<class 'module'>
>>> type(pprint.pprint)
<class 'function'>
>>> print('Howdy!')
Howdy!
>>> 
>>> # What Editor do I recommend?
>>> # In the is class, I prefer IDLE.
>>> 
>>> # In actual development:
>>> #   At least one fully text based editor:
>>> #           vi   emacs   atom   nano
>>> #   Graphical editors are great:
>>> #      TextMate  Eclipse(pydev)
>>> #      Komodo Wing-IDE PyCharm <--
>>> # Pick one bad ass editor and learn everything it does.
>>> 
>>> 
>>> 
>>> 30 + 40
70
>>> 75 - 5
70
>>> 30 * 40
1200
>>> 38 / 5
7.6
>>> # (int / int) -> float
>>> 
>>> 4 / 3 + 7 / 3 + 1 / 3
4.0
>>> def average(seq):
	'''Compute the arithmetic mean of a sequence

		>>> average([10, 20, 60])
		30

	'''
	# https://en.wikipedia.org/wiki/Arithmetic_mean
	return sum(seq) / len(seq)

	
>>> average([10, 20, 60])
30.0
>>> def average(seq):
	'''Compute the arithmetic mean of a sequence

		>>> average([10, 20, 60])
		30.0

	'''
	# https://en.wikipedia.org/wiki/Arithmetic_mean
	return sum(seq) / len(seq)

	
>>> average([10, 20, 61])
30.333333333333332
>>> def average(seq):
	'''Compute the arithmetic mean of a sequence

		>>> average([10, 20, 60])
		30.0

	'''
	# https://en.wikipedia.org/wiki/Arithmetic_mean
	return sum(seq)/len(seq)

	
>>> average([10, 20, 61])
30.333333333333332
>>> 
>>> # 1) I typed exactly what you did
>>> # 2) My computer did something different.
>>> 
>>> 
>>> 
>>> # Interactive prompt runs in a single-statement mode
>>> # Multiple statements are a SyntaxError
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> visited = collections.Counter()
>>> for filename in glob.glob('notes/*.log'):
    with open(filename) as f:
        for line in f:
            mo = re.search('GET\s+(\S+)\s+200', line)
            if mo is not None:
                url = mo.group(1)
                visited[url] += 1

                
>>> visited = collections.Counter()
for filename in glob.glob('notes/*.log'):
    with open(filename) as f:
        for line in f:
            mo = re.search('GET\s+(\S+)\s+200', line)
            if mo is not None:
                url = mo.group(1)
                visited[url] += 1
                
SyntaxError: multiple statements found while compiling a single statement
>>> def average(seq):
	'''Compute the arithmetic mean of a sequence

		>>> average([10, 20, 60])
		30.0

	'''
	# https://en.wikipedia.org/wiki/Arithmetic_mean
	return sum(seq)/len(seq)

	
>>> 
>>> 
>>> def average(seq):
	'''Compute the arithmetic mean of a sequence

		>>> average([10, 20, 60])
		30.0

	'''
	# https://en.wikipedia.org/wiki/Arithmetic_mean
	return sum(seq) / len(seq)

	
>>> 
>>> 30 + 40
70
>>> 75 - 4
71
>>> 30 * 40
1200
>>> 38 / 5
7.6
>>> 38 // 5
7
>>> 38 % 5
3
>>> 2 ** 5
32
>>> 2 ^ 5
7
>>> divmod(38, 5)
(7, 3)
>>> type(_)
<class 'tuple'>
>>> 2 ** 5
32
>>> _ * 10
320
>>> _ * 10
3200
>>> _ * 10
32000
>>> type(_)
<class 'int'>
>>> type(_)
<class 'type'>
>>> 
>>> quotient, remainder = divmod(38, 5)
>>> quotient
7
>>> remainder
3
>>> # divmod() -> gazinta
>>> 
>>> # 32 bits
>>> # 64 bits
>>> 
>>> 2 ** 3 - 1
7
>>> bin(2 ** 3 - 1)
'0b111'
>>> 2 ** 4 - 1
15
>>> bin(2 ** 4 - 1)
'0b1111'
>>> bin(2 ** 5 - 1)
'0b11111'
>>> bin(2 ** 6 - 1)
'0b111111'
>>> bin(2 ** 100 - 1)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> 3 ** 200 - 2 ** 200
265613988875874769338781322035779625222295408394404220432612869397929888379099189211591863742625
>>> - 3 ** 200 + 2 ** 200
-265613988875874769338781322035779625222295408394404220432612869397929888379099189211591863742625
>>> 
>>> 
>>> 11 ** 3
1331
>>> 11 ** 3 % 1000
331
>>> 2 ** 4 % 5
1
>>> pow(2, 4)
16
>>> pow(2, 4, 5)
1
>>> 2 ** 4
16
>>> 16 % 5
1
>>> 2 * 2
4
>>> 2 * 2 * 2
8
>>> 2 * 2 * 2 % 5
3
>>> 2 * 2 * 2 % 5 * 2
6
>>> 
>>> 
>>> pow(235, 361, 1804)
235
>>> pow(235, 361, 1801)
1107
>>> 235 ** 361

9026061329418915657719745108622460039182291399825542832463916098703230931476079801199584309266053897655049239903352595008294160966071583652030372784567132573588380796940659390049963972847097226497542985109842401155938954928118363355024681310416154726999562729461540948587801637578350846996511530290502512753602978564446365121510553751739560138253061069336353726711617284823606415959272826345805689534385630284714892180071690408917516190402709704544257788346862171622806188752993100386083631648411050292304635504622697904555069006621796452347737812858542673290360641264325350221946074408460318883123372634695487011222845033291309757240703644802824131485279075304108217544101019749305992174313847715857738661763827883547967719726331706690928033324175687668899192805438018125504161583781596326381741815066655510105676600562940592453742283396422863006591796875
>>> 235 ** 361 % 1801
1107
>>> 235 ** 2
55225
>>> 235 ** 2 % 1801
1195
>>> # Twitter: @raymondh
>>> # Jenny's number: 8675309
>>> 
>>> msg = 8675309
>>> code = pow(msg, 65537, 5551201688147)
>>> code
4394401618973
>>> pow(code, 109182490673, 5551201688147)
8675309
>>> 
>>> 
>>> 38 % 5
3
>>> 38 % 6
2
>>> 38 % 4
2
>>> 38 % 3
2
>>> 30 * 41
1230
>>> # Mac:  Controlling
>>> # Win:  Alternative
>>> 
>>> # Cntl-Prev  Cntl-Next
>>> # Alt-P Alt-N
>>> code = pow(323646, 65537, 5551201688147)
>>> code
5098599580024
>>> encode = pow(323646, 65537, 5551201688147)        # Cntl-A beg of line   C-End of line C-Kill
>>> 
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
>>> 
>>> 30 + 40
70
>>> print('hello world')
hello world
>>> for i in range(10):
        print(i**2)

        
0
1
4
9
16
25
36
49
64
81
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
>>> # fn F5
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
>>> n
10
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/overview.py ==========
[('/images/NASA-logosmall.gif', 1861),
 ('/images/MOSAIC-logosmall.gif', 1572),
 ('/images/WORLD-logosmall.gif', 1569),
 ('/images/USA-logosmall.gif', 1568),
 ('/images/ksclogo-medium.gif', 1555),
 ('/ksc.html', 1337),
 ('/images/KSC-logosmall.gif', 1083),
 ('/history/apollo/images/apollo-logo1.gif', 543),
 ('/', 534),
 ('/images/launch-logo.gif', 504),
 ('/images/ksclogosmall.gif', 444),
 ('/shuttle/missions/missions.html', 372),
 ('/images/launchmedium.gif', 298),
 ('/shuttle/countdown/count70.gif', 293),
 ('/shuttle/countdown/', 284),
 ('/shuttle/missions/sts-69/mission-sts-69.html', 275),
 ('/icons/menu.xbm', 216),
 ('/icons/blank.xbm', 211),
 ('/shuttle/missions/sts-69/sts-69-patch-small.gif', 194),
 ('/icons/image.xbm', 180)]
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now 10
>>> pad
'         '
>>> len(pad)
9
>>> 'hello' * 5
'hellohellohellohellohello'
>>> 10 * 5
50
>>> 'hello'.__mul__(5)
'hellohellohellohellohello'
>>> (10).__mul__(5)
50
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now {n}
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now 10
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now 10
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now 10
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj195/welcome.py ==========
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now 10
Let the games begin
 Wow, it moves to the right!
  Wow, it moves to the right!
   Wow, it moves to the right!
    Wow, it moves to the right!
     Wow, it moves to the right!
      Wow, it moves to the right!
       Wow, it moves to the right!
        Wow, it moves to the right!
         Wow, it moves to the right!
          Wow, it moves to the right!
The value of n is now 10
>>> # C-n C-s download.py C-TAB download.py
>>> # C-a C-c C-TAB C-v C-s F5
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj195/download2.py =========
================================== Source: http://10.155.73.99:8080/sj195/links.txt =================================
                                    Starting download at Mon Feb 11 16:40:09 2019                                    
304  Not Modified     http://10.155.73.99:8080/shared/magicmethods.pdf
304  Not Modified     http://10.155.73.99:8080/sj195/how_python_works.py
304  Not Modified     http://10.155.73.99:8080/sj195/links.txt
304  Not Modified     http://10.155.73.99:8080/shared/picirc.py
304  Not Modified     http://10.155.73.99:8080/shared/banner.py
304  Not Modified     http://10.155.73.99:8080/shared/norvig_corrector.py
304  Not Modified     http://10.155.73.99:8080/shared/corpus.dat
304  Not Modified     http://10.155.73.99:8080/shared/highlight.py
304  Not Modified     http://10.155.73.99:8080/shared/publish.py
304  Not Modified     http://10.155.73.99:8080/shared/words.txt
304  Not Modified     http://10.155.73.99:8080/shared/fsm.py
304  Not Modified     http://10.155.73.99:8080/shared/mpl_demo.py
304  Not Modified     http://10.155.73.99:8080/shared/telnet_demo.py
304  Not Modified     http://10.155.73.99:8080/turtle/tdemo_peace.py
304  Not Modified     http://10.155.73.99:8080/turtle/tdemo_yinyang.py
304  Not Modified     http://10.155.73.99:8080/shared/vcard.css
304  Not Modified     http://10.155.73.99:8080/shared/PythonAwesome.pdf
304  Not Modified     http://10.155.73.99:8080/shared/IntroPython.pdf
304  Not Modified     http://10.155.73.99:8080/shared/islands.pdf
304  Not Modified     http://10.155.73.99:8080/shared/__init__.py
304  Not Modified     http://10.155.73.99:8080/shared/BeautifulSoup.py
304  Not Modified     http://10.155.73.99:8080/shared/pexpect.py
304  Not Modified     http://10.155.73.99:8080/shared/oop_story.txt
200* OK               http://10.155.73.99:8080/sj195/overview.py              --> notes/overview.py         (updated) 
304  Not Modified     http://10.155.73.99:8080/shared/kap.svg
304  Not Modified     http://10.155.73.99:8080/shared/kap.dot
304  Not Modified     http://10.155.73.99:8080/shared/english_composition.txt
200* OK               http://10.155.73.99:8080/sj195/day1.py                  --> notes/day1.py             (updated) 
304  Not Modified     http://10.155.73.99:8080/shared/Raymond_Hettinger.png
304  Not Modified     http://10.155.73.99:8080/shared/Raymond_Hettinger.vcf
304  Not Modified     http://10.155.73.99:8080/shared/member_template.txt
304  Not Modified     http://10.155.73.99:8080/shared/family_template.txt
304  Not Modified     http://10.155.73.99:8080/shared/nasa_19950801.log
304  Not Modified     http://10.155.73.99:8080/shared/queue_stats.txt
304  Not Modified     http://10.155.73.99:8080/shared/words.txt
304  Not Modified     http://10.155.73.99:8080/shared/crossword_challenge.py
304  Not Modified     http://10.155.73.99:8080/shared/ipv4_int_bri.txt
304  Not Modified     http://10.155.73.99:8080/shared/show_controllers.txt
304  Not Modified     http://10.155.73.99:8080/shared/raisin_team.csv
304  Not Modified     http://10.155.73.99:8080/shared/raisin_team_update.csv
304  Not Modified     http://10.155.73.99:8080/shared/books.json
304  Not Modified     http://10.155.73.99:8080/shared/books.xml
304  Not Modified     http://10.155.73.99:8080/shared/rss.xml
304  Not Modified     http://10.155.73.99:8080/shared/fruit.xml
304  Not Modified     http://10.155.73.99:8080/shared/stocks.txt
304  Not Modified     http://10.155.73.99:8080/shared/email.txt
304  Not Modified     http://10.155.73.99:8080/shared/dns_servers.json
304  Not Modified     http://10.155.73.99:8080/shared/CSRRESTAPI.pdf
304  Not Modified     http://10.155.73.99:8080/shared/team_history.json
304  Not Modified     http://10.155.73.99:8080/shared/team_history.txt
304  Not Modified     http://10.155.73.99:8080/shared/re.txt
304  Not Modified     http://10.155.73.99:8080/shared/hamlet.txt
304  Not Modified     http://10.155.73.99:8080/shared/interfaces.xml
304  Not Modified     http://10.155.73.99:8080/shared/parse_demo1.txt
304  Not Modified     http://10.155.73.99:8080/shared/parse_demo2.txt
304  Not Modified     http://10.155.73.99:8080/shared/ping_output.txt
304  Not Modified     http://10.155.73.99:8080/shared/gender.json
304  Not Modified     http://10.155.73.99:8080/shared/iris_data.csv
>>> # C-n C-s download.py C-TAB download.py
>>> # C-a C-c C-TAB C-v C-s F5
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
>>> names
['raymond', 'rachel', 'matthew']
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
>>> names
['raymond', 'rachel', 'matthew']
>>> colors
['red', 'blue', 'yellow', 'green']
>>> cities
['austin', 'dallas', 'chicago', 'austin', 'houston', 'austin', 'chicago', 'dallas']
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
>>> 
>>> len(names)
3
>>> for i in range(3):
    print(i)

    
0
1
2
>>> 
>>> names[0]
'raymond'
>>> names[1]
'rachel'
>>> names[2]
'matthew'
>>> 'hello world'.upper()
'HELLO WORLD'
>>> 'hello world'.lower()
'hello world'
>>> 'hello world'.title()
'Hello World'
>>> 'hello world'.capitalize()
'Hello world'
>>> print("don't you forget about me".title())
Don'T You Forget About Me
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj195/looping_idioms.py =======
Task 1: Show all the names in a different case
RAYMOND
RACHEL
MATTHEW
Raymond
Rachel
Matthew
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
0 -> red
1 -> blue
2 -> yellow
3 -> green
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
0 -> red
1 -> blue
2 -> yellow
3 -> green
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
>>> 
>>> list(enumerate(names, start=1000))
[(1000, 'raymond'), (1001, 'rachel'), (1002, 'matthew')]
>>> list(enumerate(colors, start=-50))
[(-50, 'red'), (-49, 'blue'), (-48, 'yellow'), (-47, 'green')]
>>> 
>>> 
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2, 10))
[2, 3, 4, 5, 6, 7, 8, 9]
>>> # Half-open interval
>>> list(range(2, 10, 3))
[2, 5, 8]
>>> # range(start, stop, step)
>>> #                ^-- excluded because it a half-open interval
>>> colors
['red', 'blue', 'yellow', 'green']
>>> len(colors)
4
>>> colors[3]
'green'
>>> colors[2]
'yellow'
>>> colors[1]
'blue'
>>> colors[0]
'red'
>>> # 3 2 1 0
>>> list(range(4))
[0, 1, 2, 3]
>>> # start, stop, step
>>> # 3 2 1 0
>>> list(range(3))
[0, 1, 2]
>>> list(range(3, 0, -1))
[3, 2, 1]
>>> list(range(3, -1, -1))
[3, 2, 1, 0]
>>> list(range(len(colors), -1, -1))
[4, 3, 2, 1, 0]
>>> list(range(len(colors) - 1, -1, -1))
[3, 2, 1, 0]
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
>>> # C-style -> HOW
>>> # P-style -> WHAT
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
>>> 
>>> x = 5
>>> - x
-5
>>> # Unary operator:  Takes 1 argument
>>> x + 7
12
>>> # Binar operator:  Takes 2 arguments
>>> # Ternary operator:  Takes 3 arguments
>>> 
>>> # Ternary operator
>>> # Conditional expression
>>> # In other languages:
>>> #    cond ? posres : negres
>>> 
>>> #    (score >= 70) ? "pass" : "fail";
>>> 
>>> # Python version
>>> 
>>> #     <posres> if <cond> else <negres>
>>> 
>>> score = 55
>>> "pass" if score >= 70 else "fail"
'fail'
>>> score = 85
>>> "pass" if score >= 70 else "fail"
'pass'
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
>>> # HOW -> WHAT
>>> 
>>> 
>>> sum([10, 5, 3])
18
>>> len([10, 5, 3])
3
>>> max([10, 5, 3])
10
>>> min([10, 5, 3])
3
>>> from statistics import mean
>>> mean([10, 5, 3])
6
>>> # Reducers:  sum len max min mean
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
>>> 
>>> # mapcar in LISP
>>> list(zip('abcde', 'uvwxy'))
[('a', 'u'), ('b', 'v'), ('c', 'w'), ('d', 'x'), ('e', 'y')]
>>> list(zip(names, colors))
[('raymond', 'red'), ('rachel', 'blue'), ('matthew', 'yellow')]
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
>>> 
