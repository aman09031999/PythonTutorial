Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 	#	Variables
	
>>> num = 5
>>> id(num)
140715525956368
>>> name = 'Aman'
>>> id(name)
1937585204896
>>> a = 10
>>> id(a)
140715525956528
>>> b = a
>>> id(b)
140715525956528
>>> id(a)
140715525956528
>>> is a = b
SyntaxError: invalid syntax
>>> a = b
>>> print(a=b)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(a=b)
TypeError: 'a' is an invalid keyword argument for print()
>>> id(10)
140715525956528
>>> id(a)
140715525956528
>>> id(b)
140715525956528
>>> is a,b
SyntaxError: invalid syntax
>>> a is b is 10
True
>>> a = 12
>>> b = a
>>> id(10)
140715525956528
>>> id(a)
140715525956592
>>> id(b)
140715525956592
>>> PI = 3.14		#	constant values notation
>>> type(PI)
<class 'float'>
>>> type(a)
<class 'int'>
>>> type(name)
<class 'str'>
>>> type(num)
<class 'int'>
>>> lis = [1,'Aman',3.5]
>>> type(lis)
<class 'list'>
>>> 
