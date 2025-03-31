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

# with open('file.txt', 'w+') as file:
#     file.truncate()

# import os
# print(os.path.curdir)
# os.remove('file.txt')

           #FIRST
# sentence = "KhazarUniversity"
# # Ожидаемый вывод: "Kha zar Uni ver sit y"

# a = []
# for i in range(0,len(sentence),3):
#     a.append(sentence[i:i+3])
             
            
# print(a)
# print(' '.join(a))

# a * * * *
# b * * * *
# c * * * *
# d * * * *
# e * * * *

# list = []
# start = ord('a')

# for i in range(5):
#     a = []
#     for j in range(5):
#             if(j == 0):
#                 j = chr(start)
#             else:
#                 j = "*"
#             a.append(str(j))
#     list.append(a)
#     start +=1

# for i in list:
#     print(' '.join(i))


# list = []
# start = ord('a')

# for i in range(5):
#     a = []
#     for j in range(5):
#             if(j == 0):
#                 j = chr(start)
#             else:
#                j = "*"
#             a.append(str(j))
#     list.append(a)
#     start+=1

# for i in list:
#     print(' '.join(i))

# numbers = [10, 20, 30, 40, 50, 60, 70]
# # Четные индексы: [10, 30, 50, 70]
# # Нечетные индексы: [20, 40, 60]

# a = []
# b = []
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         a.append(numbers[i])
#     else:
#         b.append(numbers[i])

# print('Even index',a)
# print('Odd index',b)

# sentence = "hello"
# letter_count = {}
# Ожидаемый вывод: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# for i in range(len(sentence)):
#     if i in letter_count:
#         letter_count[sentence[i]] += 1
#     else:
#         letter_count[sentence[i]] = 1

# print(letter_count)


# sentence = "hello"
# letter_count = {}

# for char in sentence:
#     if char in letter_count:
#         letter_count[char] += 1
#     else:
#         letter_count[char] = 1

# print(letter_count)

# for i in sentence:
#     if i in letter_count:
#         letter_count[i] += 1

#     else:
#         letter_count[i] = 1
# print(letter_count)


# sentence = "I study at Khazar University"
# words = sentence.split()  # Разбиваем строку на список слов
# reversed_sentence = ' '.join(reversed(words))  # Разворачиваем список и объединяем обратно в строку

# print(reversed_sentence)
# bl = True
# fl = 12.5
# print(name)
# print("John")
# num = 12
# print(type(num))

# print(name.index('h'))
# number = '994552918195'
# print(number.index('55'))
# print(number.startswith('99'))
# print(number.endswith('9'))
# print(number[0:3])
# print(number[3:])
# print(number[0:6:2])

# num = '    994773710281  '
# print(num)
# print(num.strip())

# print(num.replace('7','9',1))

# print(number[-12:4])

# print(number.removeprefix('9'))

# print('Hello','World')

# nameis = 'narmin balakishi'
# print(nameis.title())

age = '1867'
number = 12.5
name ='narmin'
# print(name*2)
# print(age//10)
# print(age%10)
# print(pow(age,2))
# txt = f'My name is {name}'
# print(txt)
# print('My name is {}.Age is {}'.format(name,age))

# print(format(age, 'b'))

# print(format(age, 'x'))
# print(' '.join(format(int(i), 'x') for i in age))

# print(ord('A'))
# print(chr(23))

# print(format(name,'*^10'))
# print(format(name[2:], '*>10'))
# print(format(name, '*>10'))
# print(format(name[2:], '*>5'))
# print(format(name[2:5], '*^5'))
# print(name[2:5])
# print(format(name[1:len(name)-1], '*^' + str(len(name))))

# a = []
# a = list()
# a = [23,23,14,True, 'Narmin']
# b = None
# a.append('Narmin')
# print(a)
# a.insert(1,'Nar')
# print(a)
# a.remove('Narmin')
# print(a)
# del a[0]

# # print(a)
# a = [23,'BMW','Mercedes',None,'New Avtomobile']
# print(a[1:3])

# r = range(0,12,2)
# for i in r:
#     print(i)

# for i in range(len(a)):
#     print(a[i])


# sentence = 'I study at Khazar University'
# #output: Is tu dy at Kh az ar Un iv er si ty

# sentence.strip()
# ' '.join(sentence)
# # print(''.join(sentence))
# # print(format(sentence))
# # print(sentence.replace(' ', ''))
# sent = sentence.replace(' ', '')
# # print(sentence.split())

# a = []
# for i in range(0,len(sent),2):
#     a.append(sent[i:i+2])

# print(a)
# print(' '.join(a))

# t = tuple()
# print(type(t))
# p = (1,2,3)
# print(p[1])

# a = (12,34,1)
# print(a[1])

# def listCount(list):
#        return len(set(list))

# numbers = [1,2,2,3,4,5,6,7,8,9,10,11,12]

# print(listCount(numbers))

# def mergeAndSort(lista, listb):
#        return sorted(lista + listb)

# a = [1, 4, 3]

# b = [5, 2, 8, 1, 9]
# list = mergeAndSort(a,b)

# print(list)
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # Output: [1, 1, 3, 4, 5]
# print(numbers)  # Original list remains unchanged: [3, 1, 4, 1, 5]

# numbers.sort()

# print(numbers)  # Output: [1, 1, 3, 4, 5]

# def multiplication(number):
#        for i in range(11):
#               if(number > 0):
#                      print(str(number) + '*' + str(i) + "=" + str(number*i))
#               else:
#                      print('The number entered should be positiove')

# multiplication(5)

# def multiplication(number):
#        if(number == 0):
#               print('Multiplication by zero is always 0')
#               return
#        if(number < 0):
#               print(f'Multiplication table for {number}')
#        for i in range(1,11):
#               print(f'{number} * {i} = {number*i}')


# multiplication(5)

# multiplication(-5)

# multiplication(0)

# sentence = 'I study at Khazar University'
# print(sentence.split())

# def palindrome(sentence):
#        words = sentence.split()
#        reversed_words = words[::-1]
#        reversed_sentence = ' '.join(reversed_words)
#        return reversed_sentence.lower() == sentence.lower()

# sentence = 'Ranar'

# print(palindrome(sentence))

# def is_palindrome(s):
#     # Remove spaces and convert to lowercase
#     cleaned = s.replace(" ", "").lower()
#     # Check if the string is equal to its reverse
#     return cleaned == cleaned[::-1]

# # Example usage:
# print(is_palindrome("Racecar"))        # True
# print(is_palindrome("A man a plan a canal Panama"))  # True
# print(is_palindrome("Hello"))          # False

# def isPalindrome(sentence):
#        cleaned = sentence.replace(' ','').lower()
#        return cleaned == cleaned[::-1]

# sentence = 'Ranar'

# print(isPalindrome(sentence))

# def vowels(sentence):
#        vowels = 'aeouiAEOUI'
#        count = 0

#        for char in sentence:
#               if char in vowels:
#                      count += 1
#        return count

# sentence = 'I study at Khazar University'

# print(vowels(sentence))  

# def average(list):
#        if(len(list) == 0):
#               return 0
#        sum = 0
#        for i in range(0,len(list)):
#               sum += list[i]
              
#        avg = sum/len(list)
#        return avg

# numbers = []

# print(average(numbers))

# def fibonacci(n):
#     if n < 2:
#         print("Please enter a number greater than or equal to 2")
#         return []

#     fib_sequence = [0, 1]  # First two Fibonacci numbers
    
#     for i in range(2, n):
#         next_fib = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two numbers
#         fib_sequence.append(next_fib)
    
#     return fib_sequence

# # Example usage:
# n = int(input("Enter the number of Fibonacci numbers you want: "))
# result = fibonacci(n)
# print(result)

# def fibonacci(n):
#        if( n < 2):
#               print("Please enter a number greater than or equal to 2")
#               return []
#        fib_sequence = [0,1]
#        for i in range(2, n):
#               fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
#        return fib_sequence

# n = int(input("Enter the number of Fibonacci numbers you want: "))

# result = fibonacci(n)

# print(result)





# def fibonacci(n):
#        if(n < 2):
#               print('Please enter more that 2 numbers')
#               return []
#        fib_sequence = [0,1]

#        for i in range(2,n):
#               fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
#        return fib_sequence

# n = int(input('Please enter a number of Fibonacci numbers you want'))
# result = fibonacci(n)

# print(result)

# tup = (('a',34),('b',67))
# dictinonary = dict(tup)
# print(dictinonary)
# print(type(dictinonary))

# def evenNums(number):
#        even_numbers = []
#        for i in range(0,len(number)):
#               if(number[i] % 2 == 0):
#                      even_numbers.append(number[i])
#        return even_numbers

# number = [1,2,3,4,5,6,7,8,9,10]

# print(evenNums(number))


# def maxAndMin(numList):
#        max_num = numList[0]
#        min_num = numList[0]
#        for i in range(0,len(numList)):
#               if numList[i] > max_num:
#                      max_num = numList[i]
#               if numList[i] < min_num:
#                      min_num = numList[i]
#        return max_num, min_num

# numbers = [-1,1, 4, 3, 8, 2, 100, 5]

# max_num, min_num = maxAndMin(numbers)

# print('Maximum number:', max_num)

# print('Minimum number:', min_num)

# def factorial(number):
#        if number == 0 or number == 1:
#               return 1
#        else:
#               return number * factorial(number-1)
       
# number = int(input('Enter a number: '))

# result = factorial(number)

# print('Factorial of', number, 'is', result)


# def fact(number):
#        if(number < 0):
#               print('Please enter the positive number')
#               return 
#        elif(number == 0 or number ==1):
#               return 1
#        else:
#               return number*fact(number - 1)
# number = int(input('Enter a number'))
# result = fact(number)

# print('Factorial of', number, 'is', result)


# def divison(num1, num2):
#        if(num2 == 0):
#               print('Cannot divide by zero')
#               return None, None
#        else:
#               return num1 // num2,num1 % num2

       

# num1 = int(input('Enter first number: '))

# num2 = int(input('Enter second number: '))

# quotient, remainder = divison(num1, num2)

# print('Quotient is:', quotient)

# print('Remainder is:', remainder)
# Sample string
# text = "Hello, World!"

# # Convert string to byte format using encode()
# byte_format = text.encode('utf-8')

# # Print the byte format
# print(byte_format)


# def something(number):
#        return format(number,'')

# def format_float(number):
#     # Format the number to 2 decimal places, aligned to the right within a 10-character width
#     formatted_number = "{:>10.2f}".format(number)
#     print(formatted_number)

# format_float(12345.6789)

# format_float(-12345.6789)


# def format_float(number):
#        formatted_value = "{:>10.2f}".format(number)
#        return (formatted_value)

# n = float(input("Enter a number"))
# result = format_float(n)

# print("Formatted number:", result)

# def funct(number):
#        formatted_value = "{:>10.2f}".format(number)
#        return formatted_value

# n = float(input("Enter a number"))

# result = funct(n)

# print("Formatted number:", result)

# def round(number):
#        format(number,'.2f')
#        return number.round()

# number = float(input("Enter a number"))

# result = round(number)

# print("Rounded number:", result)


# def rounds(number):
#        return round(number,2)

# num1 = 23.456
# print(rounds(num1))

# def multiplication(x,y):
#        print(x*y)


# x = int(input('Please enter the first number'))
# y = int(input('Please enter the second number'))

# multiplication(x,y)

# def multiply():
#        x = int(input('Enter the first number'))
#        y = int(input('Enter the second number'))
#        return x * y

# result = multiply()
# print(result)
# def absolute_value(number):
#        abs_number = abs(number)
#        return f'This is absolute value:{abs_number}'

# num = int(input('Number'))

# print(absolute_value(num))

# def remove_html(filename):
#        if(filename.endswith('.html')):
#               return filename[:-5]

#        else:
#               return filename

# filename = 'index.html'


# print(remove_html(filename))

# def remove_prefix(string,prefix):
#        if(string.startswith(prefix)):
#               return string[len(prefix):]
#        else:
#               return string

# string1 = "HelloWorld"
# prefix1 = "Hello"
# string2 = "GoodbyeWorld"
# prefix2 = "Hello"


# def split_into_words(sentence):
#        words = sentence.split()
#        for word in words:
#                print(word)

# sentence = "This is a sample sentence."

# words = split_into_words(sentence)


# def endwithsmth(filename):
#        return filename.endswith('.txt')


# print(endwithsmth('salam.jpg'))

# sentence = 'This is a sample sentence'

# print(sentence.split())
# print(sentence.strip())

# def cleared_string():
#        sentence = input("Enter a sentence: ")
#        return sentence.strip()


# def checking(string,prefix):
#     string = string.lower()
#     prefix = prefix.lower()
#     return string.startswith(prefix)


# print(checking("Hello World", "hello"))  # Output: True
# print(checking("Hello World", "WORLD"))  # Output: False
 

# def chechkingStr():
#     string = str(input('Please enter a sentence'))
#     if(string):
#         return len(string)
#     else:
#         return "String is empty"
    
# print(chechkingStr())

# def count_word_frequency(filename):
#     with open(filename, 'r') as file:
#         content = file.read().lower()

#     words = content.split()
#     word_frequency = {}

#     for word in words:
#         word = word.strip('.,!?":;')
#         if word in word_frequency:
#             word_frequency[word] += 1
#         else:
#             word_frequency[word] = 1

#     sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1]))

#     for word, freq in sorted_word_frequency.items():
#         print(f'{word}: {freq}')

# filename = input('Enter the filename: ')  
# count_word_frequency(filename)


# def checking_sent():
#     string = input('Enter the sentence')
#     word = input('Enter the word: ')
#     string = string.lower()
#     word = word.lower()

#     words = string.split()
#     count = words.count(word)
#     return count

        
# print(checking_sent())

#TICKET 27
# def sumOfDigits():
#     number = int(input('Enter a number'))
#     total = 0
#     while number > 0:
#         total += number % 10
#         number //= 10
#     return total

# print(sumOfDigits())


#CHECKING FOR A PERFEKT NUMBER

# def checkForPrfektNumber():
#     number = int(input('Enter a number'))
#     factors = []
#     for i in range(1, number):
#             if number % i == 0:
#                 factors.append(i)
#     sum_of_factors = sum(factors)

#     return sum_of_factors == number
# print(checkForPrfektNumber())

#TICKET 51

# def checkCharInSentence():
#     string = input('Enter the sentence')
#     char = input('Enter the character')

#     first_index = string.find(char)
#     last_index = string.rfind(char)

#     return first_index, last_index

# print(checkCharInSentence())

#TICKET 48
# def removeDuplicatesFromList(lst):
    
#     return list(set(lst))

# lst = [1, 2, 3, 4, 4, 5, 5, 6]

# print(removeDuplicatesFromList(lst))

#TICKET 47
# def is_armstrong():
#     while True:
#             number = int(input("Enter a positive integer: "))
#             if number <= 0:
#                 print("Please enter a number greater than 0.")
#                 continue

#             num_str = str(number)
#             num_digits = len(num_str) 
#             armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
            
#             if armstrong_sum == number:
#                 print(f"{number} is an Armstrong number")
#             else:
#                 print(f"{number} is not an Armstrong number")
#             break 

# # Run the function
# is_armstrong()


# TICKET 44
# def sortInAlphOrder():
#     string = input('Please neter a string ')
#     splitted = string.split()
#     sorted_words = sorted(splitted)
#     sorted_string = ' '.join(sorted_words)
#     return sorted_string

# print(sortInAlphOrder())

# TICKET 41
# def word_length(words):
#     return [len(word) for word in words]

# words = ['apple', 'banana', 'cherry']

# print(word_length(words))

# def word_length_recur(words):
#     if not words:
#         return []
#     else:
#         return [len(words[0])] + word_length_recur(words[1:])
    

# words = ['apple', 'banana', 'cherry']
# print(word_length_recur(words))

#TICKET 38

# def largElInList():
#     lists = list(map(int,input('Enter a list of numbers ').split()))
#     return max(lists)

# print(largElInList())

# TICKET 43
# def replace_substring():
#     s = input('Enter a string: ')
#     old = input('Enter the substring to replace: ')
#     new = input('Enter the replacement substring: ')
#     return s.replace(old, new)

# print(replace_substring())

# TICKET 40

# def checkIfPalindrome():
#     s = input('Enter a string: ')
#     s = s.lower()
#     s = ''.join(e for e in s if e.isalnum())
#     return s == s[::-1]

# print(checkIfPalindrome())

#Ticket 37

# def chechForVowels():
#     vowels = 'aeoui'
#     s = input('Enter a string ')
#     count = 0
#     s = s.lower()
#     for i in s:
#         if i in vowels:
#             count += 1
#     return count

# print(chechForVowels())


#Ticket 45
# def secondLargNumberInList():
#     lists = list(map(int,input('Enter the list ').split()))
#     if len(lists) < 2:
#         return 'The list should contain at least two numbers.'
    
#     return sorted(lists)[-2]

# print(secondLargNumberInList())


#Ticket Counting words in a sentence

# def numOfWordsInSentence():
#     sentence = input("Enter a sentence: ")
#     words = sentence.split()
#     return len(words)

# print(numOfWordsInSentence())

#Finding the sum of Digits in a Number

# def sumOfDigitsInNumber():
#     number = int(input("Enter a number: "))
#     sum = 0
#     while number > 0:
#         sum += number % 10
#         number //= 10
#     return sum

# print(sumOfDigitsInNumber())

#Ticket 36
# def logestWordInSentence():
#     s = input("Enter a sentence ")
#     words = s.split()
#     for i in range(len(words)):
#         if len(words[i]) > len(words[0]):
#             words[0] = words[i]
        
#     return len(words[0])

# print(logestWordInSentence())

#Ticket 35
# def removeDuplicatesFromList():
#     lists = list(map(int,input('Enter a list ').split()))
#     convert =list(set(lists))
#     return convert

# print(removeDuplicatesFromList())

#Ticket 32
# def reverseTheString():
#     s = input("Enter a string: ")
#     return s[::-1]

# print(reverseTheString())

# s = "Hello, World!"
# result = s[::-1]
# print(result) 

#TICKET 29

# def sortedAndMergedTwoListsOfNumbers():
#     list1 = list(map(int,input('Enter a list of numbers ').split()))
#     list2 = list(map(int,input('Enter another list of numbers ').split()))
#     list1.extend(list2)
#     sorted_list = sorted(list1)
#     return sorted_list


# print(sortedAndMergedTwoListsOfNumbers())

#TICKET 26

# def eachWordFrequencyInString():
#     s = input("Enter a string: ")
#     words = s.split()
#     frequency = {}
#     for word in words:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency

# print(eachWordFrequencyInString())


#Converting Celsius to Fahrenheit

# def celsiusToFahrenheit():
#     celsius = float(input("Enter the temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# print(celsiusToFahrenheit())


#TICKET 31

# def commonElInTwoists():
#     list1 = list(map(int,input('Enter list 1 ').split()))
#     list2 = list(map(int,input('Enter list 2 ').split()))
#     set1 = set(list1)
#     set2 = set(list2)
#     same = set1.intersection(set2)
#     return list(same)

# print(commonElInTwoists())

# TICKET 25

# multipTableForGivenNumber()

# def multipTableForGivenNumber():
#     number = int(input('Enter a number: '))
#     for i in range(1,11):
#         print(f'{number} x {i} = {number * i}')

# multipTableForGivenNumber()


# Calculating Factorial of a number

# def factorialOfAGivenNumber():
#     number = int(input('Enter a number: '))
#     if number < 0:
#         return 'Factorial is not defined for negative numbers.'
#     factorial = 1
#     for i in range(1,number + 1):
#              factorial *= i
#     return factorial
    
# print(factorialOfAGivenNumber())

#Calculating Area of a Circle

# import math
# def areaOfACircle():
#     radius = float(input('Enter the radius of the circle: '))
#     area = math.pi * radius * radius
#     return area

# print(areaOfACircle())

# TICKET 24

# def isPalindrome():
#     s = input('Enter the ')
#     s = s.lower()
#     return s[:: -1] == s

# print(isPalindrome())

#Finding even numbers in a list

# def findEvenNumsInList():
#     lists = list(map(int,input('Enter the list of numbers ').split()))
#     even_list = []
#     for i in range(0,len(lists)):
#         if lists[i] % 2 == 0:
#             even_list.append(lists[i])
#     return even_list


# print(findEvenNumsInList())

# import re
# def findEvenNumsInList():
#     smth = input('Enter the list of numbers ')
#     lists = list(map(int, re.findall(r'\d+', smth)))
#     even_list = []
#     for i in range(0,len(lists)):
#         if lists[i] % 2 == 0:
#             even_list.append(lists[i])
#     return even_list


# print(findEvenNumsInList())

# def sortList():
#     lists = list(map(int,input('Enter a list of numbers ').split()))
#     lists.sort()
#     return lists

# print(sortList())

#TICKET 20

# def maximInList():
#     lists = list(map(int,input('Enter the list of numbers ').split()))
    
#     return max(lists)

# print(maximInList())
    
# def absoluteValue():
#     number = int(input('Enter a number: '))
#     return abs(number)

# print(absoluteValue())

# str = ''
# print(str.split())

# def splittingStringIntoAList():
#     string = input('Enter a string: ')
#     words = string.split()
#     return words

# print(splittingStringIntoAList())

# def checkStringEnd(string, suffix):
#     return string.endswith(suffix)
# str = 'slm'
# print(str.startswith(' '))
# print(checkStringEnd('Hello, World!', 's'))

# #COUNTING CHARACTER OCCURENCES IN A STRING
# def checkString(string,charCount):
#     count = 0
#     for i in string:
#         if i == charCount:
#             count += 1
#     return count

# string = 'Hello, World!'

# print(checkString(string, 'l'))