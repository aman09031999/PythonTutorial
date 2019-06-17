Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # List in Python
>>> 
>>> nums = [12,45,67,56,67]	# list of number
>>> nums
[12, 45, 67, 56, 67]
>>> name = ['Hello','Aman','Pradhan']	# list of String
>>> name
['Hello', 'Aman', 'Pradhan']
>>> name[2]
'Pradhan'
>>> name[1]
'Aman'
>>> nums[2:]
[67, 56, 67]
>>> nums[-2]
56
>>> nums
[12, 45, 67, 56, 67]
>>> nums[3]
56
>>> nums[-2]
56
>>> value = ['Aman',23,3.6,'hello']	# list of multiple data types
>>> value[1]
23
>>> value[3]
'hello'
>>> value[2]
3.6
>>> value[4]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    value[4]
IndexError: list index out of range
>>> value[0]
'Aman'
>>> mil = [name,nums,value]
>>> mil
[['Hello', 'Aman', 'Pradhan'], [12, 45, 67, 56, 67], ['Aman', 23, 3.6, 'hello']]
>>> nums.append(89)
>>> nums
[12, 45, 67, 56, 67, 89]
>>> nums.insert(2,90)
>>> nums
[12, 45, 90, 67, 56, 67, 89]
>>> len(nums)
7
>>> sum(nums)
426
>>> sum(name)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sum(name)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> min(name)
'Aman'
>>> name
['Hello', 'Aman', 'Pradhan']
>>> name.append('abcs')
>>> min(name)
'Aman'
>>> name
['Hello', 'Aman', 'Pradhan', 'abcs']
>>> sort(name)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sort(name)
NameError: name 'sort' is not defined
>>> name.sort()
>>> name
['Aman', 'Hello', 'Pradhan', 'abcs']
>>> nums.sort()
>>> nums
[12, 45, 56, 67, 67, 89, 90]
>>> 
