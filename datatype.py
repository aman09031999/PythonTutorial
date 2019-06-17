Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = None		#	DataType : 'None'
>>> type(num1)
<class 'NoneType'>
>>> num2 = 12		#	DataType : 'Numberic : int'
>>> type(num2)
<class 'int'>
>>> num3 = 1.2		#	DataType : 'Numberic : float'
>>> type(num3)
<class 'float'>
>>> num4 = True		#	DataType : 'Numberic : bool(boolean)'
>>> type(num4)
<class 'bool'>
>>> num5 = 4+8j		#	DataType : 'Numberic : complex'
>>> type(num5)
<class 'complex'>
>>> a = 5.7
>>> b = int(a)		#	Type casting : float -> int
>>> type(a)
<class 'float'>
>>> type(b)
<class 'int'>
>>> x = 6+9j
>>> y = complex(x)
>>> type(y)
<class 'complex'>
>>> x = 6+9j
>>> x = 6
>>> y = 7
>>> z = complex(x,y)	#	Type casting : int -> complex
>>> type(z)
<class 'complex'>
>>> z
(6+7j)
>>> x>y
False
>>> x>z
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x>z
TypeError: '>' not supported between instances of 'int' and 'complex'
>>> int(True)
1
>>> int(False)
0
>>> range(0,10)
range(0, 10)
>>> type(range)
<class 'type'>
>>> type(type())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    type(type())
TypeError: type() takes 1 or 3 arguments
>>> type(type)
<class 'type'>
>>> lis(range)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    lis(range)
NameError: name 'lis' is not defined
>>> lis(range(10))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lis(range(10))
NameError: name 'lis' is not defined
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(type(10))
<class 'type'>
>>> d = {'name': 'Aman','phone' : 'iPhone'}
>>> d = {'name': 'Aman','phone' : 'iPhone'}		#	Dictionary
>>> d.keys()
dict_keys(['name', 'phone'])
>>> d.values()
dict_values(['Aman', 'iPhone'])
>>> d.['name']
SyntaxError: invalid syntax
>>> d.get['name']
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    d.get['name']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d.get('name')
'Aman'
>>> 
