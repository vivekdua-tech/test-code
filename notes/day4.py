Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
>>> print(vcard)
BEGIN:VCARD
VERSION:2.1
N:Gump;Forrest;;Mr.
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;GIF:http://www.example.com/dir_photos/my_photo.gif
TEL;WORK;VOICE:(111) 555-1212
TEL;HOME;VOICE:(404) 555-1212
ADR;WORK;PREF:;;100 Waters Edge;Baytown;LA;30314;United States of America
LABEL;WORK;PREF;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:100 Waters Edge=0D=
 =0ABaytown\, LA 30314=0D=0AUnited States of America
ADR;HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;HOME;ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8:42 Plantation St.=0D=0A=
 Baytown, LA 30314=0D=0AUnited States of America
EMAIL:forrestgump@example.com
REV:20080424T195243Z
END:VCARD

>>> # Raymond Dean | Hettinger
>>> # Guido | van Rossum
>>> fname = input('Enter your first name: ')
Enter your first name: David
>>> lname = input('Enter your last name: ')
Enter your last name: I
>>> 
>>> 
>>> fname
'David'
>>> lname
'I'
>>> len(lname) == 1
True
>>> if len(lname) == 1:
	print('We need a real name, not an initial')
	lname = input('Enter your last name: ')

	
We need a real name, not an initial
Enter your last name: I
>>> # David Yi
>>> # Ramon Luna Hettinger
>>> # Raymond Dean Hettinger
>>> # Raymond Matthew Hettinger
>>> # The Artist Formerly Known as Prince
>>> # c@c.
>>> 
>>> 
>>> # Happy Valentines Day!
>>> # Happy Matthew's 7th Birthday.
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> x = 10
>>> print(f'The answer is {x}')
The answer is 10
>>> 
>>> template = 'The answer is {x}'
>>> 
>>> x = 10
>>> template.format(x=x)
'The answer is 10'
>>> with open('sample_template.txt', 'w') as f:
	f.write(template)

	
17
>>> 
=============================== RESTART: Shell ===============================
>>> x = 12
>>> with open('sample_template.txt') as f:
	template = f.read()
	print(template.format(x=x))

	
The answer is 12
>>> with open('sample_template.txt') as f:
	template = f.read()
	print(template.format(x=x))

	
The answer is approximately 12

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Raymond Hettinger
Mary Thomas
Harold Davis
Martin Masterson
David Jones
Luis Zapata
Fritz Gunter
Esmerela Pichon
Marilyn Blain
Blair Marks
David Jones
Harold Davis
Gertrude Schmidt
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> # one: name it generically           lock
>>> # many: name specifically       reader_lock writer_lock
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/vcard.py", line 30, in <module>
    vcard.write(vcard)
AttributeError: 'str' object has no attribute 'write'
>>> type(vcard)
<class 'str'>
>>> print(vcard)
BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> import os
>>> os.getcwd()
'/Users/raymond/Dropbox/Public/sj195'
>>> os.chdir('notes')
>>> os.getcwd()
'/Users/raymond/Dropbox/Public/sj195/notes'
>>> os.chdir('..')
>>> os.getcwd()
'/Users/raymond/Dropbox/Public/sj195'
>>> os.listdir('notes')
['gm_vs_toyata.py', 'rss.xml', 're.txt', 'etag_db.dir', 'Raymond_Hettinger.vcf', 'kap.svg', 'day2.py', 'tdemo_peace.py', 'member_template.txt', 'english_composition.txt', 'corpus.dat', 'kap.dot', 'oop_story.txt', 'gender.json', 'iris_data.csv', 'dns_servers.json', 'ping_output.txt', 'norvig_corrector.py', 'email.txt', 'books.xml', 'pexpect.py', 'tdemo_yinyang.py', '__init__.py', 'stocks.txt', 'picirc.py', 'queue_stats.txt', 'links.txt', 'overview.py', 'islands.pdf', 'raisin_team.csv', 'BeautifulSoup.py', 'magicmethods.pdf', 'team_history.txt', 'books.json', 'raisin_team_update.csv', 'crossword_challenge.py', 'team_history.json', 'ipv4_int_bri.txt', 'family_template.txt', 'highlight.py', 'vcard.css', 'words.txt', 'fruit.xml', 'how_python_works.py', 'CSRRESTAPI.pdf', 'telnet_demo.py', 'mpl_demo.py', 'interfaces.xml', 'show_controllers.txt', 'PythonAwesome.pdf', 'parse_demo2.txt', 'Raymond_Hettinger.png', 'IntroPython.pdf', 'fsm.py', 'grand_tour.py', 'nasa_19950801.log', 'banner.py', 'hamlet.txt', 'parse_demo1.txt', 'etag_db.dat', 'day1.py', 'looping_idioms.py', 'publish.py']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
BEGIN:VCARD
VERSION:2.1
N:Hettinger;Raymond
FN:Raymond Hettinger
ORG:Raisins R Us, Inc.
TITLE:VP Raisin Smushing
TEL;WORK;VOICE:559-555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:raymond@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Thomas;Mary
FN:Mary Thomas
ORG:Raisins R Us, Inc.
TITLE:Sr. Associate Raisin Design
TEL;WORK;VOICE:559-555-2300
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:mary@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Chief Raisin Picker
TEL;WORK;VOICE:559-555-2318
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:harold@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Masterson;Martin
FN:Martin Masterson
ORG:Raisins R Us, Inc.
TITLE:Asst Raisin Smusher
TEL;WORK;VOICE:559-555-2348
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:martin@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Grape Ager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:david@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Zapata;Luis
FN:Luis Zapata
ORG:Raisins R Us, Inc.
TITLE:VP Grape Sales
TEL;WORK;VOICE:559-555-2301
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:luis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Gunter;Fritz
FN:Fritz Gunter
ORG:Raisins R Us, Inc.
TITLE:Grape Smusher
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:fritz@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Pichon;Esmerela
FN:Esmerela Pichon
ORG:Raisins R Us, Inc.
TITLE:Head Raisin Counter
TEL;WORK;VOICE:559-555-2397
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:esmerelda@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Blain;Marilyn
FN:Marilyn Blain
ORG:Raisins R Us, Inc.
TITLE:Raisin Packager
TEL;WORK;VOICE:559-555-2379
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:marilyn@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Marks;Blair
FN:Blair Marks
ORG:Raisins R Us, Inc.
TITLE:VP Investor Relations
TEL;WORK;VOICE:559-555-6513
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:blair@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Jones;David
FN:David Jones
ORG:Raisins R Us, Inc.
TITLE:Transport Specialist
TEL;WORK;VOICE:559-555-1892
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:djones@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Davis;Harold
FN:Harold Davis
ORG:Raisins R Us, Inc.
TITLE:Quality Assurance Tech
TEL;WORK;VOICE:559-555-1478
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:hdavis@example.com
REV:20190214T195243Z
END:VCARD

BEGIN:VCARD
VERSION:2.1
N:Schmidt;Gertrude
FN:Gertrude Schmidt
ORG:Raisins R Us, Inc.
TITLE:VP Business Development
TEL;WORK;VOICE:559-555-6700
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:gertrude@example.com
REV:20190214T195243Z
END:VCARD

>>> # Keep filename the same
>>> # And give every person their own direct
>>> 
>>> # Give every person a different filename
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'Raymond_Hettinger.vcf'
Wrote: 'Mary_Thomas.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Martin_Masterson.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Luis_Zapata.vcf'
Wrote: 'Fritz_Gunter.vcf'
Wrote: 'Esmerela_Pichon.vcf'
Wrote: 'Marilyn_Blain.vcf'
Wrote: 'Blair_Marks.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Gertrude_Schmidt.vcf'
>>> # str and repr
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'Raymond_Hettinger.vcf'
Wrote: 'Mary_Thomas.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Martin_Masterson.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Luis_Zapata.vcf'
Wrote: 'Fritz_Gunter.vcf'
Wrote: 'Esmerela_Pichon.vcf'
Wrote: 'Marilyn_Blain.vcf'
Wrote: 'Blair_Marks.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Gertrude_Schmidt.vcf'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: Raymond_Hettinger.vcf
Wrote: Mary_Thomas.vcf
Wrote: Harold_Davis.vcf
Wrote: Martin_Masterson.vcf
Wrote: David_Jones.vcf
Wrote: Luis_Zapata.vcf
Wrote: Fritz_Gunter.vcf
Wrote: Esmerela_Pichon.vcf
Wrote: Marilyn_Blain.vcf
Wrote: Blair_Marks.vcf
Wrote: David_Jones.vcf
Wrote: Harold_Davis.vcf
Wrote: Gertrude_Schmidt.vcf
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'Raymond_Hettinger.vcf'
Wrote: 'Mary_Thomas.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Martin_Masterson.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Luis_Zapata.vcf'
Wrote: 'Fritz_Gunter.vcf'
Wrote: 'Esmerela_Pichon.vcf'
Wrote: 'Marilyn_Blain.vcf'
Wrote: 'Blair_Marks.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Gertrude_Schmidt.vcf'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'Raymond_Hettinger.vcf'
Wrote: 'Mary_Thomas.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Martin_Masterson.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Luis_Zapata.vcf'
Wrote: 'Fritz_Gunter.vcf'
Wrote: 'Esmerela_Pichon.vcf'
Wrote: 'Marilyn_Blain.vcf'
Wrote: 'Blair_Marks.vcf'
Wrote: 'David_Jones.vcf'
Wrote: 'Harold_Davis.vcf'
Wrote: 'Gertrude_Schmidt.vcf'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: '559-555-1212.vcf'
Wrote: '559-555-2300.vcf'
Wrote: '559-555-2318.vcf'
Wrote: '559-555-2348.vcf'
Wrote: '559-555-2379.vcf'
Wrote: '559-555-2301.vcf'
Wrote: '559-555-2379.vcf'
Wrote: '559-555-2397.vcf'
Wrote: '559-555-2379.vcf'
Wrote: '559-555-6513.vcf'
Wrote: '559-555-1892.vcf'
Wrote: '559-555-1478.vcf'
Wrote: '559-555-6700.vcf'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond@example.com.vcf'
Wrote: 'mary@example.com.vcf'
Wrote: 'harold@example.com.vcf'
Wrote: 'martin@example.com.vcf'
Wrote: 'david@example.com.vcf'
Wrote: 'luis@example.com.vcf'
Wrote: 'fritz@example.com.vcf'
Wrote: 'esmerelda@example.com.vcf'
Wrote: 'marilyn@example.com.vcf'
Wrote: 'blair@example.com.vcf'
Wrote: 'djones@example.com.vcf'
Wrote: 'hdavis@example.com.vcf'
Wrote: 'gertrude@example.com.vcf'
>>> # .tar  .gz  .tar.gz
>>> # RDH Business -- 2012 -- Summary & Receipts.xlsw
>>> # rdh_business_2012_summmary_and_receipts.xlsw
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.vcf'
>>> # And Trump said, <~I demand a wall`%@ at today's conference.
>>> 
>>> 
>>> names = ['raymond', 'rachel', 'matthew']
>>> # list -> od ul           ordered list or unordered list
>>> # 1. raymodn
>>> # 2. rachel
>>> 
>>> # * raymond
>>> # * rachel
>>> 
>>> # list of tuples -> [('raymond', 'hettinger', 54, 'python@rcn.com'),
>>> #                    ('matthew', 'hettinger', 7, 'mattinator@aol.com']
>>> # list of tuples ->      table
>>> #
>>> # <table>
>>> # <tr> <th> First </th> <th> Last </th> </tr>
>>> # <tr> <td> Raymond </td> <td> Hettinger </td> </tr>
>>> # </table>
>>> 
>>> color = {'raymond': 'red', 'rachel': 'blue', 'matthew': 'yellow'}
>>> # dict -> definition list
>>> 
>>> # <dl>
>>> #     <dt> raymond </dt> <dd> red </red>
>>> #     <dt> rachel> </dt> <dd> blue </dd> </dt>
>>> # </dl>
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.vcf'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Raymond Hettinger </title>
</head>
<body>
<h1> Contact info for <em> Raymond Hettinger </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Raymond Hettinger  </dd>
    <dt> Job title  </dt>  <dd> VP Raisin Smushing </dd>
    <dt> Work phone  </dt>  <dd> 559-555-1212  </dd>
</dl>
</body>
</html>

Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Mary Thomas </title>
</head>
<body>
<h1> Contact info for <em> Mary Thomas </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Mary Thomas  </dd>
    <dt> Job title  </dt>  <dd> Sr. Associate Raisin Design </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2300  </dd>
</dl>
</body>
</html>

Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Harold Davis </title>
</head>
<body>
<h1> Contact info for <em> Harold Davis </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Harold Davis  </dd>
    <dt> Job title  </dt>  <dd> Chief Raisin Picker </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2318  </dd>
</dl>
</body>
</html>

Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Martin Masterson </title>
</head>
<body>
<h1> Contact info for <em> Martin Masterson </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Martin Masterson  </dd>
    <dt> Job title  </dt>  <dd> Asst Raisin Smusher </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2348  </dd>
</dl>
</body>
</html>

Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> David Jones </title>
</head>
<body>
<h1> Contact info for <em> David Jones </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> David Jones  </dd>
    <dt> Job title  </dt>  <dd> Grape Ager </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2379  </dd>
</dl>
</body>
</html>

Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Luis Zapata </title>
</head>
<body>
<h1> Contact info for <em> Luis Zapata </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Luis Zapata  </dd>
    <dt> Job title  </dt>  <dd> VP Grape Sales </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2301  </dd>
</dl>
</body>
</html>

Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Fritz Gunter </title>
</head>
<body>
<h1> Contact info for <em> Fritz Gunter </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Fritz Gunter  </dd>
    <dt> Job title  </dt>  <dd> Grape Smusher </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2379  </dd>
</dl>
</body>
</html>

Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Esmerela Pichon </title>
</head>
<body>
<h1> Contact info for <em> Esmerela Pichon </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Esmerela Pichon  </dd>
    <dt> Job title  </dt>  <dd> Head Raisin Counter </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2397  </dd>
</dl>
</body>
</html>

Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Marilyn Blain </title>
</head>
<body>
<h1> Contact info for <em> Marilyn Blain </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Marilyn Blain  </dd>
    <dt> Job title  </dt>  <dd> Raisin Packager </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2379  </dd>
</dl>
</body>
</html>

Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Blair Marks </title>
</head>
<body>
<h1> Contact info for <em> Blair Marks </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Blair Marks  </dd>
    <dt> Job title  </dt>  <dd> VP Investor Relations </dd>
    <dt> Work phone  </dt>  <dd> 559-555-6513  </dd>
</dl>
</body>
</html>

Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> David Jones </title>
</head>
<body>
<h1> Contact info for <em> David Jones </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> David Jones  </dd>
    <dt> Job title  </dt>  <dd> Transport Specialist </dd>
    <dt> Work phone  </dt>  <dd> 559-555-1892  </dd>
</dl>
</body>
</html>

Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Harold Davis </title>
</head>
<body>
<h1> Contact info for <em> Harold Davis </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Harold Davis  </dd>
    <dt> Job title  </dt>  <dd> Quality Assurance Tech </dd>
    <dt> Work phone  </dt>  <dd> 559-555-1478  </dd>
</dl>
</body>
</html>

Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Gertrude Schmidt </title>
</head>
<body>
<h1> Contact info for <em> Gertrude Schmidt </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Gertrude Schmidt  </dd>
    <dt> Job title  </dt>  <dd> VP Business Development </dd>
    <dt> Work phone  </dt>  <dd> 559-555-6700  </dd>
</dl>
</body>
</html>

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Raymond Hettinger </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Raymond Hettinger </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Raymond Hettinger  </dd>
    <dt> Job title  </dt>  <dd> VP Raisin Smushing </dd>
    <dt> Work phone  </dt>  <dd> 559-555-1212  </dd>
</dl>
</body>
</html>

Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Mary Thomas </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Mary Thomas </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Mary Thomas  </dd>
    <dt> Job title  </dt>  <dd> Sr. Associate Raisin Design </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2300  </dd>
</dl>
</body>
</html>

Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Harold Davis </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Harold Davis </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Harold Davis  </dd>
    <dt> Job title  </dt>  <dd> Chief Raisin Picker </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2318  </dd>
</dl>
</body>
</html>

Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Martin Masterson </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Martin Masterson </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Martin Masterson  </dd>
    <dt> Job title  </dt>  <dd> Asst Raisin Smusher </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2348  </dd>
</dl>
</body>
</html>

Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> David Jones </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> David Jones </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> David Jones  </dd>
    <dt> Job title  </dt>  <dd> Grape Ager </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2379  </dd>
</dl>
</body>
</html>

Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Luis Zapata </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Luis Zapata </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Luis Zapata  </dd>
    <dt> Job title  </dt>  <dd> VP Grape Sales </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2301  </dd>
</dl>
</body>
</html>

Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Fritz Gunter </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Fritz Gunter </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Fritz Gunter  </dd>
    <dt> Job title  </dt>  <dd> Grape Smusher </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2379  </dd>
</dl>
</body>
</html>

Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Esmerela Pichon </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Esmerela Pichon </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Esmerela Pichon  </dd>
    <dt> Job title  </dt>  <dd> Head Raisin Counter </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2397  </dd>
</dl>
</body>
</html>

Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Marilyn Blain </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Marilyn Blain </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Marilyn Blain  </dd>
    <dt> Job title  </dt>  <dd> Raisin Packager </dd>
    <dt> Work phone  </dt>  <dd> 559-555-2379  </dd>
</dl>
</body>
</html>

Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Blair Marks </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Blair Marks </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Blair Marks  </dd>
    <dt> Job title  </dt>  <dd> VP Investor Relations </dd>
    <dt> Work phone  </dt>  <dd> 559-555-6513  </dd>
</dl>
</body>
</html>

Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> David Jones </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> David Jones </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> David Jones  </dd>
    <dt> Job title  </dt>  <dd> Transport Specialist </dd>
    <dt> Work phone  </dt>  <dd> 559-555-1892  </dd>
</dl>
</body>
</html>

Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Harold Davis </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Harold Davis </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Harold Davis  </dd>
    <dt> Job title  </dt>  <dd> Quality Assurance Tech </dd>
    <dt> Work phone  </dt>  <dd> 559-555-1478  </dd>
</dl>
</body>
</html>

Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> Gertrude Schmidt </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> Gertrude Schmidt </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> Gertrude Schmidt  </dd>
    <dt> Job title  </dt>  <dd> VP Business Development </dd>
    <dt> Work phone  </dt>  <dd> 559-555-6700  </dd>
</dl>
</body>
</html>

>>> # Katniss Everdeen
>>> # Think of words that might appear on the page you're looking for and type them in.
>>> #        I will always love you
>>> # Describe the KIND of thing your looking and use that to qualify search
>>> #        I will always love you lyrics
>>> 
>>> # Think of words that might appear on the page you're looking for and type them in.
>>> #        Twitter
>>> # Describe the KIND of thing your looking and use that to qualify search
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
https://chart.googleapis.com/chart?cht=qr&chs=300x300&chl=BEGIN%3AVCARD%0AVERSION%3A2.1%0AN%3ASchmidt%3BGertrude%0AFN%3AGertrude+Schmidt%0AORG%3ARaisins+R+Us%2C+Inc.%0ATITLE%3AVP+Business+Development%0ATEL%3BWORK%3BVOICE%3A559-555-6700%0AADR%3BWORK%3BPREF%3A%3B%3B100+Flat+Grape+Dr.%3BFresno%3BCA%3B95551%3BUnited+States+of+America%0AEMAIL%3Agertrude%40example.com%0AREV%3A20190214T195243Z%0AEND%3AVCARD%0A
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
>>> qr[:5]
b'\x89PNG\r'
>>> type(qr)
<class 'bytes'>
>>> len(qr)
2865
>>> qr[:5]
b'\x89PNG\r'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'raymond_at_example_dot_com.png'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.png'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.png'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.png'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.png'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.png'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.png'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.png'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.png'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.png'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.png'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.png'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
>>> # ILT 432855
>>> 

>>> 
>>> n = 23
>>> 
>>> 
>>> n % 2 == 0
False
>>> 
>>> # That is why they call it "work"
>>> 
>>> def is_even(n):
	return n % 2 == 0

>>> 
>>> 
>>> is_even(23)
False
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'raymond_at_example_dot_com.png'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.png'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.png'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.png'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.png'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.png'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.png'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.png'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.png'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.png'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.png'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.png'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'raymond_at_example_dot_com.png'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.png'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.png'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.png'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.png'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.png'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.png'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.png'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.png'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.png'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.png'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.png'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
=============================== RESTART: Shell ===============================
>>> import vcard
>>> dir(vcard)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'html_template', 'make_html', 'make_qr_code', 'make_vcard', 'urlencode', 'urlopen', 'vcard_template']
>>> help(vcard)
Help on module vcard:

NAME
    vcard

DESCRIPTION
    Old, true, and sordid tale of Python
    featuring raisins, pushy relatives,
    business cards, web pages, checkboards and
    getting must needed rest api.

FUNCTIONS
    make_html(fname, lname, title, phone, email)
        Create human readable contact information in an HTML 5 format
    
    make_qr_code(text)
        Create a computer readable QR matrix barcode in a PNG file format
    
    make_vcard(fname, lname, title, phone, email)
        Create an electronic business card in a VCard 2.1 format

DATA
    html_template = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <met.....
    vcard_template = 'BEGIN:VCARD\nVERSION:2.1\nN:{lname};{fname}\nFN:{fn....

FILE
    /Users/raymond/Dropbox/Public/sj195/vcard.py


>>> 
>>> print(vcard.make_vcard('Lakshmi', 'Ramesh', 'VP of Programmers', '555-1212', 'lramesh_superprogrammer@cisco.com'))
BEGIN:VCARD
VERSION:2.1
N:Ramesh;Lakshmi
FN:Lakshmi Ramesh
ORG:Raisins R Us, Inc.
TITLE:VP of Programmers
TEL;WORK;VOICE:555-1212
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:lramesh_superprogrammer@cisco.com
REV:20190214T195243Z
END:VCARD

>>> print(vcard.vcard_template)
BEGIN:VCARD
VERSION:2.1
N:{lname};{fname}
FN:{fname} {lname}
ORG:Raisins R Us, Inc.
TITLE:{title}
TEL;WORK;VOICE:{phone}
ADR;WORK;PREF:;;100 Flat Grape Dr.;Fresno;CA;95551;United States of America
EMAIL:{email}
REV:20190214T195243Z
END:VCARD

>>> vcard.vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:{lname};{fname}
FN:{fname} {lname}
ORG:Cisco Systems, Inc.
TITLE:{title}
TEL;WORK;VOICE:{phone}
ADR;WORK;PREF:;;150 W Tasman Dr.;San Jose;CA;95051;United States of America
EMAIL:{email}
REV:20190214T195243Z
END:VCARD
'''
>>> print(vcard.make_vcard('Lakshmi', 'Ramesh', 'VP of Programmers', '555-1212', 'lramesh_superprogrammer@cisco.com'))
BEGIN:VCARD
VERSION:2.1
N:Ramesh;Lakshmi
FN:Lakshmi Ramesh
ORG:Cisco Systems, Inc.
TITLE:VP of Programmers
TEL;WORK;VOICE:555-1212
ADR;WORK;PREF:;;150 W Tasman Dr.;San Jose;CA;95051;United States of America
EMAIL:lramesh_superprogrammer@cisco.com
REV:20190214T195243Z
END:VCARD

>>> image = vcard.make_qr_code('He who will not, when he may, when he would, he shall have nay')
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'raymond_at_example_dot_com.png'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.png'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.png'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.png'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.png'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.png'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.png'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.png'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.png'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.png'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.png'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.png'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: '"raymond_at_example_dot_com".vcf'
Wrote: '"raymond_at_example_dot_com".html'
Wrote: '"raymond_at_example_dot_com".png'
Wrote: '"mary_at_example_dot_com".vcf'
Wrote: '"mary_at_example_dot_com".html'
Wrote: '"mary_at_example_dot_com".png'
Wrote: '"harold_at_example_dot_com".vcf'
Wrote: '"harold_at_example_dot_com".html'
Wrote: '"harold_at_example_dot_com".png'
Wrote: '"martin_at_example_dot_com".vcf'
Wrote: '"martin_at_example_dot_com".html'
Wrote: '"martin_at_example_dot_com".png'
Wrote: '"david_at_example_dot_com".vcf'
Wrote: '"david_at_example_dot_com".html'
Wrote: '"david_at_example_dot_com".png'
Wrote: '"luis_at_example_dot_com".vcf'
Wrote: '"luis_at_example_dot_com".html'
Wrote: '"luis_at_example_dot_com".png'
Wrote: '"fritz_at_example_dot_com".vcf'
Wrote: '"fritz_at_example_dot_com".html'
Wrote: '"fritz_at_example_dot_com".png'
Wrote: '"esmerelda_at_example_dot_com".vcf'
Wrote: '"esmerelda_at_example_dot_com".html'
Wrote: '"esmerelda_at_example_dot_com".png'
Wrote: '"marilyn_at_example_dot_com".vcf'
Wrote: '"marilyn_at_example_dot_com".html'
Wrote: '"marilyn_at_example_dot_com".png'
Wrote: '"blair_at_example_dot_com".vcf'
Wrote: '"blair_at_example_dot_com".html'
Wrote: '"blair_at_example_dot_com".png'
Wrote: '"djones_at_example_dot_com".vcf'
Wrote: '"djones_at_example_dot_com".html'
Wrote: '"djones_at_example_dot_com".png'
Wrote: '"hdavis_at_example_dot_com".vcf'
Wrote: '"hdavis_at_example_dot_com".html'
Wrote: '"hdavis_at_example_dot_com".png'
Wrote: '"gertrude_at_example_dot_com".vcf'
Wrote: '"gertrude_at_example_dot_com".html'
Wrote: '"gertrude_at_example_dot_com".png'
>>> print(html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> "Gertrude" "Schmidt" </title>
    <link rel="stylesheet" href="notes/vcard.css">
</head>
<body>
<h1> Contact info for <em> "Gertrude" "Schmidt" </em> </h1>
<hr>
<dl>
    <dt> Full name  </dt>  <dd> "Gertrude" "Schmidt"  </dd>
    <dt> Job title  </dt>  <dd> "VP Business Development" </dd>
    <dt> Work phone  </dt>  <dd> "559-555-6700"  </dd>
</dl>
</body>
</html>

>>> fname
'"Gertrude"'
>>> lname
'"Schmidt"'
>>> phone
'"559-555-6700"'
>>> email
'"gertrude@example.com"'
>>> line
'"Schmidt","Gertrude","VP Business Development","gertrude@example.com","559-555-6700"'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'raymond_at_example_dot_com.png'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.png'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.png'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.png'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.png'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.png'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.png'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.png'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.png'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.png'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.png'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.png'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj195/vcard.py ===========
Wrote: 'raymond_at_example_dot_com.vcf'
Wrote: 'raymond_at_example_dot_com.html'
Wrote: 'raymond_at_example_dot_com.png'
Wrote: 'mary_at_example_dot_com.vcf'
Wrote: 'mary_at_example_dot_com.html'
Wrote: 'mary_at_example_dot_com.png'
Wrote: 'harold_at_example_dot_com.vcf'
Wrote: 'harold_at_example_dot_com.html'
Wrote: 'harold_at_example_dot_com.png'
Wrote: 'martin_at_example_dot_com.vcf'
Wrote: 'martin_at_example_dot_com.html'
Wrote: 'martin_at_example_dot_com.png'
Wrote: 'david_at_example_dot_com.vcf'
Wrote: 'david_at_example_dot_com.html'
Wrote: 'david_at_example_dot_com.png'
Wrote: 'luis_at_example_dot_com.vcf'
Wrote: 'luis_at_example_dot_com.html'
Wrote: 'luis_at_example_dot_com.png'
Wrote: 'fritz_at_example_dot_com.vcf'
Wrote: 'fritz_at_example_dot_com.html'
Wrote: 'fritz_at_example_dot_com.png'
Wrote: 'esmerelda_at_example_dot_com.vcf'
Wrote: 'esmerelda_at_example_dot_com.html'
Wrote: 'esmerelda_at_example_dot_com.png'
Wrote: 'marilyn_at_example_dot_com.vcf'
Wrote: 'marilyn_at_example_dot_com.html'
Wrote: 'marilyn_at_example_dot_com.png'
Wrote: 'blair_at_example_dot_com.vcf'
Wrote: 'blair_at_example_dot_com.html'
Wrote: 'blair_at_example_dot_com.png'
Wrote: 'djones_at_example_dot_com.vcf'
Wrote: 'djones_at_example_dot_com.html'
Wrote: 'djones_at_example_dot_com.png'
Wrote: 'hdavis_at_example_dot_com.vcf'
Wrote: 'hdavis_at_example_dot_com.html'
Wrote: 'hdavis_at_example_dot_com.png'
Wrote: 'gertrude_at_example_dot_com.vcf'
Wrote: 'gertrude_at_example_dot_com.html'
Wrote: 'gertrude_at_example_dot_com.png'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> cm_17_2.location
'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'
>>> cm_17_3.location
'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'
>>> cm_17_2.kind
'junk food'
>>> cm_17_3.kind
'junk food'
>>> 
>>> 
>>> # Classes and Instances in Python
>>> # are implemented in a simple way.
>>> # Classes have a dict
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> cm_17_3.__dict__
{'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> vars(cm_17_3)
{'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> 
>>> 
>>> 'hello'.__len__()
5
>>> len('hello')
5
>>> 
>>> 
>>> pprint(vars(CandyMachine))
mappingproxy({'__dict__': <attribute '__dict__' of 'CandyMachine' objects>,
              '__doc__': 'Food dispenser',
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'CandyMachine' objects>,
              'kind': 'junk food'})
>>> pprint(vars(cm_17_2))
{'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
>>> pprint(vars(cm_17_3))
{'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> # A . B
>>> #   C
>>> 
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> pprint(vars(cm_17_2))
{'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> pprint(vars(cm_17_2))
{'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 18, in <module>
    initialize(cm_17_3.location,'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom')
AttributeError: 'CandyMachine' object has no attribute 'location'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> 
>>> 
>>> # English -- Action Oriented
>>> # Verb DirectObject
>>> # Hit the ball
>>> # Hid the glove
>>> 
>>> # German -- Thing Oriented
>>> # Noun verb
>>> # Das ballens ist aufhitten.
>>> # Die glovenverken is gehidden.
>>> 
>>> # English -- Action Oriented -- Functions
>>> # German -- Objected Oriented
>>> 
>>> 
>>> # hit('ball')
>>> # ball.hit()
>>> 
>>> # hide('glove')
>>> # glove.hide()
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> 
>>> # puts putch printf fprintf sprintf wsprint ...
>>> 
>>> # data.print()
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> vars(cm_17_3)
{}
>>> # A . B
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> vars(cm_17_2)
{'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
>>> pprint(vars(cm_17_2))
{'available': {},
 'cost': {},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {},
 'cost': {},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {},
 'cost': {},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {},
 'cost': {},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> len(cm_17_3.cost)
3
>>> # Law of Demeter
>>> cm_17_3
<__main__.CandyMachine object at 0x10bbc2e10>
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_2.num_kinds_of_candy()
2
>>> 
>>> 
>>> len('hello')
5
>>> 'hello'.__len__()
5
>>> 
>>> # list    dict    CandyMachine
>>> # len()   len()   .num_kinds_of_candy()
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> len('hello')
5
>>> len({})
0
>>> len(cm_17_3)
3
>>> 
>>> 
>>> money = 0.0
>>> len(cm_17_2)
2
>>> cm_17_2.cost['reeses']
0.75
>>> cm_17_2.available['reeses']
5
>>> cm_17_2.cost['reeses'] > money
True
>>> 
>>> money = 0.75
>>> cm_17_2.cost['reeses'] == money
True
>>> cm_17_2.available['reeses']
5
>>> cm_17_2.available['reeses'] > 0
True
>>> cm_17_2.available['reeses'] -= 1
>>> cm_17_2.available['reeses']
4
>>> 
>>> money = 1.00
>>> cm_17_2.cost['reeses'] <= money
True
>>> cm_17_2.available['reeses']
4
>>> cm_17_2.available['reeses'] > 0
True
>>> cm_17_2.available['reeses'] -= 1
>>> cm_17_2.available['reeses']
3
>>> 
>>> money - cm_17_2.cost['reeses']
0.25
>>> 
>>> 
>>> import math
>>> math.sqrt(49)
7.0
>>> math.sqrt('hello')
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    math.sqrt('hello')
TypeError: must be real number, not str
>>> math.sqrt(-49)
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    math.sqrt(-49)
ValueError: math domain error
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_2.vend('reeses')
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    cm_17_2.vend('reeses')
TypeError: vend() missing 1 required positional argument: 'money'
>>> cm_17_2.vend('reeses', 1.00)
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_2.vend('snickers', 1.00)
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    cm_17_2.vend('snickers', 1.00)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 23, in vend
    if self.available[product] == 0:
KeyError: 'snickers'
>>> 
>>> 
>>> colors = dict(raymond='red', rachel='blue')
>>> colors.get('rachel', 'black')
'blue'
>>> colors.get('matthew', 'black')
'black'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_2.vend('snickers', 1.00)
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    cm_17_2.vend('snickers', 1.00)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 24, in vend
    raise ValueError(f'Sorry, I am out of {product}')
ValueError: Sorry, I am out of snickers
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_2.vend('snickers', 1.00)
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    cm_17_2.vend('snickers', 1.00)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 24, in vend
    raise ValueError(f'Sorry, I am out of {product}')
ValueError: Sorry, I am out of snickers
>>> cm_17_2.vend('snickers', 0.25)
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    cm_17_2.vend('snickers', 0.25)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 24, in vend
    raise ValueError(f'Sorry, I am out of {product}')
ValueError: Sorry, I am out of snickers
>>> cm_17_2.vend('reeses', 0.25)
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    cm_17_2.vend('reeses', 0.25)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 27, in vend
    raise ValueError(f'Sorry, the {product} costs {cost}')
ValueError: Sorry, the reeses costs 0.75
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_3.vend('popcorn', 1.00)
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    cm_17_3.vend('popcorn', 1.00)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 27, in vend
    raise ValueError(f'Sorry, the {product} costs ${cost:.2f}')
ValueError: Sorry, the popcorn costs $2.50
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_3.vend('popcorn', 4.00)
Here, have a popcorn and here is your change $1.50
>>> cm_17_3.vend('popcorn', 2.50)
Here, have a popcorn and here is your change $0.00
>>> cm_17_3.vend('popcorn', 2.00)
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    cm_17_3.vend('popcorn', 2.00)
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 27, in vend
    raise ValueError(f'Sorry, the {product} costs ${cost:.2f}')
ValueError: Sorry, the popcorn costs $2.50
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
{'available': {'reeses': 5, 'skittles': 3},
 'cost': {'reeses': 0.75, 'skittles': 1.25},
 'earnings': 0.0,
 'location': 'Cisco Way -- Bldg 17 -- Floor 2 -- Breakroom'}
{'available': {'popcorn': 2, 'reeses': 4, 'snickers': 5},
 'cost': {'popcorn': 2.5, 'reeses': 0.75, 'snickers': 0.6},
 'earnings': 0.0,
 'location': 'Cisco Way -- Bldg 17 -- Floor 3 -- Breakroom'}
>>> cm_17_2.vend('reeses', 1.00)
Here, have a reeses and here is your change $0.25
>>> cm_17_2.vend('skittles', 1.25)
Here, have a skittles and here is your change $0.00
>>> cm_17_2.earnings
2.0
>>> vars[cm_17_2]['earnings']
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    vars[cm_17_2]['earnings']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> vars(cm_17_2)['earnings']
2.0
>>> 
>>> 
>>> # Classes hold SHARED INFO
>>> # Instances hold UNIQUE INFO
>>> # Children can override the parents
>>> cm_17_2.kind = 'beer'
>>> cm_17_2.kind
'beer'
>>> 
>>> # Generalization / Specialization
>>> 
>>> # Living Thing
>>> #   Animals
>>> #   Plants
>>> 
>>> # Living Thing
>>> #   Animals kind of LT with mito
>>> #   Plants kind of LT with choro
>>> 
>>> # Living Thing
>>> #   Animals kind of LT with mito
>>> #     Mammal -- kind of animal live young feed with mamm
>>> #     Fish -- kind of animal that swims
>>> #     Bird -- kind of animal that flies
>>> 
>>> 
>>> #     Mammal -- kind of animal live young feed with mamm
>>> #          Dog kind of mammal that barks
>>> #          Bat kind of mammal that flies
>>> #          Dophin kind of mamman that swims
>>> #     Bird -- kind of animal that flies
>>> #          Eagle kind of bird that is carniv
>>> #          Penguin kind of bird thats swims instead of flied
>>> 
>>> 
>>> # Circle/Ellipse Problems
>>> 
>>> 
>>> # Propensity to subclass varies by language
>>> # In modern C++, best practices is to NEVER subclass
>>> # In typical Java, we subclass many levels
>>> #     starting with an abstract class
>>> # The norm in Python is all concrete classes
>>> #     once is while, we add an ABC after the fact
>>> # The norm in Python is usually one and sometimes two levels deep.
>>> 
>>> # The development varies as well.
>>> # In Java, you tend to write parent classes first.
>>> # In Python, you write two independ classes, THEN
>>> #   move their common feature upward.
>>> 
>>> 
>>> pass
>>> 
>>> 
>>> class ComplexCode:
	pass

>>> class ComplexCode:
	pass

>>> def complex_code(interesting_data):
	'Stubbing out the code'
	pass

>>> # def from_keys(cls, data)    # Alternative constructors
>>> # ^--- classmethod
>>> 
>>> # def convert_inhg_mb(x):
>>> # ^--- staticmethod
>>> 
>>> 
>>> 
>>> # Over 200 dunder things
>>> #  Some of the have patterns
>>> #        + __add__
>>> #        - __sub__
>>> #        * __mul__
>>> #        ** __pow__
>>> #        &  __add__
>>> #        |  __or__
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> # Over 200 dunder things
>>> #  Some of the have patterns
>>> #  Also there are a few in very common use
>>> #  [] __getitem__
>>> #  len __len__
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
None
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 51, in <module>
    print(cm_17_3.vend('skittles', 2.00))
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 25, in vend
    raise ValueError(f'Sorry, I am out of {product}')
ValueError: Sorry, I am out of skittles
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
None
Here, have a skittles and here is your change $0.75
None
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
None
Here, have a skittles and here is your change $0.75
None
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj195/oops.py", line 52, in <module>
    cm_17_2.report()
AttributeError: 'CandyMachine' object has no attribute 'report'
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
None
Here, have a skittles and here is your change $0.75
None
There are 2 products available
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
There are 2 products available
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
There are 2 products available
--------------------
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
There are 2 products available
------------------------------
>>> # keys()    values()    items()
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
There are 2 products available
------------------------------
reeses 4
skittles 2
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 products available
------------------------------
reeses 4
skittles 0
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 products available
------------------------------
reeses 4
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 products available
------------------------------
reeses 4 0.75
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 products available
------------------------------
We have 4 reeses on hand for $0.75
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 4 reeses on hand for $0.75
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 4 reeses on hand for $0.75
----------------------------------------
The total earnings are: $4.50
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 4 reeses on hand for $0.75
----------------------------------------
The total earnings are: $4.50
Here, have a reeses and here is your change $0.65

There are 3 kinds of products possibly in the machine
----------------------------------------
We have 3 reeses on hand for $0.75
We have 5 snickers on hand for $0.60
We have 2 popcorn on hand for $2.50
----------------------------------------
The total earnings are: $0.75
>>> 
>>> 
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 4 reeses on hand for $0.75
----------------------------------------
The total earnings are: $4.50
Here, have a reeses and here is your change $0.65

There are 3 kinds of products possibly in the machine
----------------------------------------
We have 3 reeses on hand for $0.75
We have 5 snickers on hand for $0.60
We have 2 popcorn on hand for $2.50
----------------------------------------
The total earnings are: $0.75
>>> with open('notes/cm_15_1.json') as f:
	shipment = json.load(f)

	
>>> pprint(f)
<_io.TextIOWrapper name='notes/cm_15_1.json' mode='r' encoding='UTF-8'>
>>> pprint(shipment)
{'popcorn': [4, 1.75],
 'reeses': [10, 1.0],
 'skittles': [5, 0.75],
 'snickers': [2, 0.6]}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============
Here, have a reeses and here is your change $0.25
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75
Here, have a skittles and here is your change $0.75

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 4 reeses on hand for $0.75
----------------------------------------
The total earnings are: $4.50
Here, have a reeses and here is your change $0.65

There are 3 kinds of products possibly in the machine
----------------------------------------
We have 3 reeses on hand for $0.75
We have 5 snickers on hand for $0.60
We have 2 popcorn on hand for $2.50
----------------------------------------
The total earnings are: $0.75

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00
{'popcorn': [4, 1.75],
 'reeses': [10, 1.0],
 'skittles': [5, 0.75],
 'snickers': [2, 0.6]}
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00
reeses --> [10, 1.0]
skittles --> [5, 0.75]
snickers --> [2, 0.6]
popcorn --> [4, 1.75]
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00
reeses --> 10 1.0
skittles --> 5 0.75
snickers --> 2 0.6
popcorn --> 4 1.75
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00
{'popcorn': [4, 1.75],
 'reeses': [10, 1.0],
 'skittles': [5, 0.75],
 'snickers': [2, 0.6]}

There are 4 kinds of products possibly in the machine
----------------------------------------
We have 5 snickers on hand for $0.60
We have 17 reeses on hand for $1.00
We have 5 skittles on hand for $0.75
We have 4 popcorn on hand for $1.75
----------------------------------------
The total earnings are: $0.00
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/oops.py ============

There are 2 kinds of products possibly in the machine
----------------------------------------
We have 3 snickers on hand for $0.60
We have 7 reeses on hand for $0.90
----------------------------------------
The total earnings are: $0.00

There are 4 kinds of products possibly in the machine
----------------------------------------
We have 5 snickers on hand for $0.60
We have 17 reeses on hand for $1.00
We have 5 skittles on hand for $0.75
We have 4 popcorn on hand for $1.75
----------------------------------------
The total earnings are: $0.00
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
TestResults(failed=0, attempted=4)
>>> 
>>> True and False
False
>>> True and True
True
>>> False and True
False
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
980 9711
981 9621
982 9531
983 9441
984 9351
985 9261
986 9171
987 9081
988 8991
989 9081
990 9801
991 9711
992 9621
993 9531
994 9441
995 9351
996 9261
997 9171
998 9081
999 8991
1000 999
1001 1089
1002 2088
1003 3087
1004 4086
1005 5085
1006 6084
1007 7083
1008 8082
1009 9081
1010 1089
1011 999
1012 1998
1013 2997
1014 3996
1015 4995
1016 5994
1017 6993
1018 7992
1019 8991
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
0980 -> 9711;
0981 -> 9621;
0982 -> 9531;
0983 -> 9441;
0984 -> 9351;
0985 -> 9261;
0986 -> 9171;
0987 -> 9081;
0988 -> 8991;
0989 -> 9081;
0990 -> 9801;
0991 -> 9711;
0992 -> 9621;
0993 -> 9531;
0994 -> 9441;
0995 -> 9351;
0996 -> 9261;
0997 -> 9171;
0998 -> 9081;
0999 -> 8991;
1000 -> 0999;
1001 -> 1089;
1002 -> 2088;
1003 -> 3087;
1004 -> 4086;
1005 -> 5085;
1006 -> 6084;
1007 -> 7083;
1008 -> 8082;
1009 -> 9081;
1010 -> 1089;
1011 -> 0999;
1012 -> 1998;
1013 -> 2997;
1014 -> 3996;
1015 -> 4995;
1016 -> 5994;
1017 -> 6993;
1018 -> 7992;
1019 -> 8991;
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
>>> type(kapdict)
<class 'dict'>
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
>>> type(kapdict)
<class 'dict'>
>>> len(kapdict)
10000
>>> pprint(list(kapdict.items())[:30])
[('0000', '0000'),
 ('0001', '0999'),
 ('0002', '1998'),
 ('0003', '2997'),
 ('0004', '3996'),
 ('0005', '4995'),
 ('0006', '5994'),
 ('0007', '6993'),
 ('0008', '7992'),
 ('0009', '8991'),
 ('0010', '0999'),
 ('0011', '1089'),
 ('0012', '2088'),
 ('0013', '3087'),
 ('0014', '4086'),
 ('0015', '5085'),
 ('0016', '6084'),
 ('0017', '7083'),
 ('0018', '8082'),
 ('0019', '9081'),
 ('0020', '1998'),
 ('0021', '2088'),
 ('0022', '2178'),
 ('0023', '3177'),
 ('0024', '4176'),
 ('0025', '5175'),
 ('0026', '6174'),
 ('0027', '7173'),
 ('0028', '8172'),
 ('0029', '9171')]
>>> kap(0)
0
>>> kap(1)
999
>>> kap(29)
9171
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
>>> type(firsts)
<class 'set'>
>>> len(firsts)
9945
>>> list(firsts)[:10]
['1609', '1819', '4113', '5079', '3785', '8682', '6445', '5430', '2682', '8163']
>>> 
>>> kap(3468)
5175
>>> '5175' not in firsts
True
>>> 
>>> kap(5623)
4176
>>> '4176' not in firsts
True
>>> '3087' not in firsts
True
>>> '8352' not in firsts
True
>>> '6174' not in firsts
True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
>>> len(kapdict)
10000
>>> len(firsts)
9945
>>> len(rest)
55
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
>>> rest
{'6354', '3177', '5265', '4356', '9711', '9621', '9351', '8442', '8622', '4266', '4995', '6084', '8991', '9261', '8262', '9531', '7992', '1089', '7083', '0999', '6174', '8532', '8172', '5355', '3267', '5085', '8352', '1998', '3996', '7173', '7533', '2178', '7263', '9171', '8712', '5175', '2088', '4176', '6264', '9081', '6993', '6534', '7353', '7443', '9801', '5994', '5445', '4086', '3087', '2997', '9441', '0000', '8082', '7623', '6444'}
>>> sorted(rest)
['0000', '0999', '1089', '1998', '2088', '2178', '2997', '3087', '3177', '3267', '3996', '4086', '4176', '4266', '4356', '4995', '5085', '5175', '5265', '5355', '5445', '5994', '6084', '6174', '6264', '6354', '6444', '6534', '6993', '7083', '7173', '7263', '7353', '7443', '7533', '7623', '7992', '8082', '8172', '8262', '8352', '8442', '8532', '8622', '8712', '8991', '9081', '9171', '9261', '9351', '9441', '9531', '9621', '9711', '9801']
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
0000 -> 0000
0999 -> 8991
1089 -> 9621
1998 -> 8082
2088 -> 8532
2178 -> 7443
2997 -> 7173
3087 -> 8352
3177 -> 6354
3267 -> 5265
3996 -> 6264
4086 -> 8172
4176 -> 6174
4266 -> 4176
4356 -> 3087
4995 -> 5355
5085 -> 7992
5175 -> 5994
5265 -> 3996
5355 -> 1998
5445 -> 1089
5994 -> 5355
6084 -> 8172
6174 -> 6174
6264 -> 4176
6354 -> 3087
6444 -> 1998
6534 -> 3087
6993 -> 6264
7083 -> 8352
7173 -> 6354
7263 -> 5265
7353 -> 4176
7443 -> 3996
7533 -> 4176
7623 -> 5265
7992 -> 7173
8082 -> 8532
8172 -> 7443
8262 -> 6354
8352 -> 6174
8442 -> 5994
8532 -> 6174
8622 -> 6354
8712 -> 7443
8991 -> 8082
9081 -> 9621
9171 -> 8532
9261 -> 8352
9351 -> 8172
9441 -> 7992
9531 -> 8172
9621 -> 8352
9711 -> 8532
9801 -> 9621
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj195/kap.py ============
0000 -> 0000;
0999 -> 8991;
1089 -> 9621;
1998 -> 8082;
2088 -> 8532;
2178 -> 7443;
2997 -> 7173;
3087 -> 8352;
3177 -> 6354;
3267 -> 5265;
3996 -> 6264;
4086 -> 8172;
4176 -> 6174;
4266 -> 4176;
4356 -> 3087;
4995 -> 5355;
5085 -> 7992;
5175 -> 5994;
5265 -> 3996;
5355 -> 1998;
5445 -> 1089;
5994 -> 5355;
6084 -> 8172;
6174 -> 6174;
6264 -> 4176;
6354 -> 3087;
6444 -> 1998;
6534 -> 3087;
6993 -> 6264;
7083 -> 8352;
7173 -> 6354;
7263 -> 5265;
7353 -> 4176;
7443 -> 3996;
7533 -> 4176;
7623 -> 5265;
7992 -> 7173;
8082 -> 8532;
8172 -> 7443;
8262 -> 6354;
8352 -> 6174;
8442 -> 5994;
8532 -> 6174;
8622 -> 6354;
8712 -> 7443;
8991 -> 8082;
9081 -> 9621;
9171 -> 8532;
9261 -> 8352;
9351 -> 8172;
9441 -> 7992;
9531 -> 8172;
9621 -> 8352;
9711 -> 8532;
9801 -> 9621;
>>> 
