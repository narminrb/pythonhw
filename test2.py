# def test(x, y = 5, *args, **kwargs):
#     print('X value is: ' + str(x))
#     print('Y value is: ' + str(y))
#     for i in args:
#         print('Args values: ' + str(i))
#     for i in kwargs:
#         print('kwargs values: '  + str(kwargs[i]))

# test(8, 5, 67, 6,name='Narmin')
# x = 5
# def loc():
#     print('X value is: ' + str(x))
# loc()
# print(x)
# def test():
#     pass
# def secondTest():
#     pass
# def thirdTest():
#     x = 5
#     print('X value is: ' + str(x))
# thirdTest()
# def test():
#     for i in range(10):
#         for j in range(10):
#             print(j)
#             if j == 2:
#                break
# test()
# def test(x):
#     print(x)
# try:
#     test()
# except NameError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# def test():
#     print('My name is Test')
# test()
# name = 'John Smith'
# number = '994552918195'
# num = 12
# float = 12.5
# boolean = True
# print(type(boolean))
# print(boolean)
# print(float)
# print(num)
# print(name)
# print(name.index('h'))
# print(number.startswith('4'))
# print(number.endswith('4'))
# length = len(number)
# print(number[3:length])
# num = '    994552918195  '
# print(num)
# print(num.strip())
# print(num.replace('5','9',1))
# print(number[-1:])
# if(number[-1:] == '5'):
#     print('Number ends with 5')
# print(number.removesuffix('5'))
# age = '182'
# number = 12.5
# name = 'John'
# print('My name is {}.Age is {}'.format(name,age))
# print(f'My name is {name}.Age is {age}')
# print(name)
# print(type(number))
# print(age)
# print(pow(age,2))
# print(format(age, 'b'))
# print(format(age, 'o'))
# print(' '.join(format(int(i), '03x') for i in age))
# print(ord('a'))
# print(format(name, '*<10'))
# print(format(name, '*^10'))
# print(format(name[2:], '*>5'))
# print(format(name[1:len(name)-1], '*^' + str(len(name))))
# print(format(number, '.2f'))
#LESSON 3
# a = []
# b = list()
# c = [23, 'Value', True]
# print(c)
# a.append('element 1')
# print(a)
# a.pop()
# print(a)
# a.append(1)
# a.insert(1,'New value')
# print(a)
#c = ['Element 1', 1, '2', 3]
# c.insert(1, 'New value')
# print(c)
# c.remove(1)
# print(c)
# del c[2]
# print(c)
# r = range(2,10,2)
# print(type(r))
# # print(*r)
# c = ['Element 1', 1, '2', 3]
# r = range(0, len(c))
# for i in r:
#     print(c[i])
# a = ['Honda', 'BMW', 'Mercedes', 'New Automobile']
# range_element = range(0, len(a), 2)
# sentence = 'I study at Khazar University'
# #output Is tu dy at Kh az ar Un iv er si ty
# print(sentence)
# sentence = sentence.replace(' ', '')
# print(sentence)
# a =[]
# for i in range(0,len(sentence),2):
#    a.append(sentence[i:i+2])
# print(a)
# print(' '.join(a))
#TUPLE
# t = tuple()
# t = (1, 2, 3, 4, 5)
# print(t)
# a = (12, 34, 1)
# x, y, z = a
# print(x)

"""
list - mutable, ordering, duplicate
tuple - immutable, ordering, duplicate
set - mutable, non-duplicte, non-ordering
dictionary - mutable, ordering, non-duplicte
"""
# listExample = [45, 'Okey', True]
# print(setExample)
# print(setExample)
# setExample.add('New Set Element')
# print(setExample)
# print(setExample.difference(set2Example))
# print(setExample.intersection(set2Example))
# print(setExample.union(set2Example))
# setExample = {12, 56, 'Test', None}
# set2Example = {12, 56, True,False, None, 'Bir'}
# setExample.remove(12)
# print(setExample)

#DICTIONARY

# d = {}
# print(type(d))

# d = {'Name':'John', 'Last Name':'Doe','Age':25, 'City':'New York'}

# print(d)
# print(type(d))

# print(d['Name'])

# d['Age'] = 26

# dict1 = {'items' : ['item1', 'item1'], (12, 13):'new Item'}
# print(dict1)
# def test(x, y, *args, **kwargs):
#     print('X value is:' + str(x))
#     print('Y value is:' + str(y))
#     for i in kwargs:
#         print('kwargs values are:' + str(kwargs[i]))
#     for i in args:
#         print('Args value is:' + str(i))

# # test(5,6,34,45,6,56,56,name='Narmin')
# def loc():
#     x = 5
#     print('X value is:' + str(x))

# loc()
# def test():
#     pass

# def secondTest():
#     print('I am the second test')

# secondTest()

# def test():
#     for i in range(10):
#       for j in range(10):
#         if j == 2:
#             return j

# print(test())

# def test(x):
#     print(x)
# try:
#     test(5)
# except NameError as e:
#     print('An error occurred')
# except TypeError as e:
#     print('Another error occurred')


#FILE OPERATIONS 

"""
chmod 755, 777, 644
       read write execute
user   4    2     1
group  4    2     1
others 4    2     1
r, w, a, r+, a+, w+
"""

# file = open('test.txt', 'w+')
# file.write(' text')
# # file.seek(1)
# file.flush()
# # sleep(10)
# # print(file.read())
# # print(file.tell())
# file.close()

with open('file.txt', 'w+') as file:
    file.truncate()

import os
print(os.path.curdir)
os.remove('file.txt')


