Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 9
>>> print(x)
9
>>> x + 4
13
>>> _ * 2
26
>>> s = 'Aman'
>>> x = 'Pradhan'
>>> s + x
'AmanPradhan'
>>> 'Hello' + s
'HelloAman'
>>> print(s)
Aman
>>> s[0]
'A'
>>> s[5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> s[-1]
'n'
>>> s[-2]
'a'
>>> s[-3]
'm'
>>> s[-4]
'A'
>>> s[-7]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[-7]
IndexError: string index out of range
>>> name = 'AmanPradhan'
>>> name[0:2]
'Am'
>>> name[3:6]
'nPr'
>>> name[3:]
'nPradhan'
>>> name[:]
'AmanPradhan'
>>> name[:5]
'AmanP'
>>> name[2:14]
'anPradhan'
>>> name
'AmanPradhan'
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> name[0:3] = 'my'	# in pyhton String are immutable
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    name[0:3] = 'my'	# in pyhton String are immutable
TypeError: 'str' object does not support item assignment
>>> 'hello' + name[0:3]
'helloAma'
>>> len(name)
11
>>> 
