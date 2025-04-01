#TICKET 27  #one

# def sumOfDigits():
#     number = int(input('Enter a number:'))
#     sum = 0
#     while number > 0:
#         digit = number % 10
#         number //=10
#         sum+=digit
#     return sum
# print(sumOfDigits())

#TICKET 64 
# def integDivision():
#     number = int(input('Enter a number: '))
#     divider = int(input('Enter a divider: '))
#     quotient = number // divider
#     remainder = number % divider
#     return quotient, remainder

# print(integDivision())

#TICKET 65 
# def formatNum(number):
#     formatted = "{:>10.2f}".format(number)
#     return formatted

# print(formatNum(23))
#TICKET 63
# def roundedNum():
#     number = float(input('Enter a number: '))
#     rounded_num = round(number,2)
#     return rounded_num

# age = 23
# print(f"I am {age} years    old")

#TICKET 62 
# def multiplyNums():
#     num1 = float(input('Enter the first number: '))
#     num2 = float(input('Enter the second number: '))

#     return num1 * num2

# result = multiplyNums()

# print(f'The product is: {result}')

#TICKET 61 

# def calcAbsValue():
#     number = int(input("Enter a number: "))
#     abs_value = abs(number)
#     return 'This is absolute value {}'.format(abs_value)

# print(calcAbsValue())

# TICKET 60 
# def removeSuffix(filename):
#     return filename.removesuffix('.html')

# print(removeSuffix('index.jpg'))

# TICKET 59 
# def removePrefix(filename,prefix):
#     return filename.removeprefix(prefix)

# print(removePrefix('index.html', 'index'))

 
# TICKET 58 
# def replaceSubstr():
#     sentence = input('Enter a sentence: ')
#     if sentence.find('Python'):
#         sentence = sentence.replace('Python', 'JavaScript')
#     return sentence

# print(replaceSubstr())

# TICKET 57 

# def splittingSent():
#     sentence = input('Enter the sentence: ')
#     words = sentence.split()
#     for word in words:
#         print(word)
    
# splittingSent()

# TICKET 55 #ten
# def checkStrinEnd(filename):
#     return filename.endswith('.txt')

# print(checkStrinEnd('test.txt'))

# TICKET 56

# def removeWhiteSpace():
#     sentence = input('Enter the sentence: ')
#     clean_sentence = sentence.strip()
#     return clean_sentence

# print(removeWhiteSpace())

# TICKET 54 #twelve

# def checkStringStart(sentence,prefix):
#     sentence = sentence.lower()
#     prefix = prefix.lower()
#     return sentence.startswith(prefix)

# print(checkStringStart('This is a sample sentence', 'this'))


# TICKET 53 #thirteen
# def clacStringLength():
#     sentence = input("Enter a sentence: ")
#     if sentence == '':
#         return 'Empty string'
#     return len(sentence)

# print(clacStringLength())

#TICKET 50

# def count_word_frequency(filename):
#     word_frequency = {} 
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             content = file.read().lower()
        
#         words = content.split() 
#         for word in words:
#             word = word.strip('.,!?":;()') 
#             if word in word_frequency:
#                 word_frequency[word] += 1
#             else:
#                 word_frequency[word] = 1

#         sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda item: item[1], reverse=True))

#         for word, freq in sorted_word_frequency.items():
#             print(f"{word}: {freq}")

#     except FileNotFoundError:
#         print("Error: The file was not found!")


# filename = "hometask1.py"
# count_word_frequency(filename)
         
    
# TICKET 52 

# def countOccurancesOfWord():
#     sentence = input('Enter a sentence: ')
#     word_to_find = input("Enter the word to find: ")
#     sentence = sentence.lower()
#     word_to_find = word_to_find.lower()
#     words = sentence.split()
#     count = 0
#     for word in words:
#         if word == word_to_find:
#             count += 1
#     return count

# print(countOccurancesOfWord())

#QUESTION
# def countOccurancesOfWord():
#     sentence = input('Enter a sentence: ')
#     word_to_find = input("Enter the word to find: ")
#     sentence = sentence.lower()
#     word_to_find = word_to_find.lower()
#     words = sentence.split()
#     count = 0
#     for word in words:
#         if word_to_find in word:
#             count += 1
#     return count

# print(countOccurancesOfWord())

#TICKET 49

# def checkForPerfectNum():
#     number = int(input('Enter the number '))
#     sum = 0

#     for i in range(1,number):
#         if number % i == 0:
#             sum += i
    
#     if sum == number:
#         return True
#     else:
#         return False

# print(checkForPerfectNum())

# TICKET 51  #seventeen
# def workWithStr():
#     sentence = input('Enter the sentence: ')
#     character = input('Enter the character: ')

#     if character in sentence:
#         first_index = sentence.index(character)
#         last_index = sentence.rindex(character)
#         return first_index, last_index
#     else:
#         return -1
    
# print(workWithStr())

# TICKET 48 #eighteen

# def removeDuplicates():
#     entered_list = list(map(int,input("Enter a list of numbers: ").split()))
#     unique_list = list(set(entered_list))
#     return unique_list

# print(removeDuplicates())

# TICKET 47 

# def checkForArmstrongNum():
#     num = int(input('Enter a number: '))
#     num_str = str(num)
#     num_length = len(num_str)
#     sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
#     return num == sum_of_powers

# print(checkForArmstrongNum())
 
# TICKET 44  

# def sortWordsInAlphabeticOrder():
#     sentence = input('Enter the sentence: ')
#     words = sentence.split()
#     words.sort()
#     return words

# print(sortWordsInAlphabeticOrder())

# TICKET 41 

# def newListFromWords():
#     items_list = input('Enter the list of words').split()
#     length_list = [len(item) for item in items_list]
#     return length_list

# print(newListFromWords())

# TICKET 38 
 
# def findTheLargestNum():
#     num_list = list(map(int,input('Enter the list of numbers: ').split()))
#     max_item = num_list[0]
#     for i in range(1,len(num_list)):
#         if num_list[i] > max_item:
#             max_item = num_list[i]

#         return max_item
    
# print(findTheLargestNum())

# TICKET 46 

# def averageOfListNums():
#     list_nums = list(map(int,input('Enter the list of numbers: ').split()))
#     return sum(list_nums) / len(list_nums)

# print(averageOfListNums())


# TICKET 43 

# def replacingOccurancesOfSubstring():
#     sentence = input('Enter the sentence: ')
#     substring_to_find = input('Enter the substring to find: ')
#     substring_to_replace = input('Enter the substring to replace: ')
#     sentence = sentence.replace(substring_to_find, substring_to_replace)
#     return sentence

# print(replacingOccurancesOfSubstring())

# TICKET 40

# def checkIfPlaindrome():
#     string = input('Enter the string: ')
#     string = string.lower()
#     return string[::-1] == string

# print(checkIfPlaindrome())


# TICKET 37
# def numOfVowels():
#     vowels = 'aeoiu'
#     string = input('Enter the string: ')
#     string = string.lower()
#     count = 0
#     for char in string:
#         if char in vowels:
#             count +=1
#     return count

# print(numOfVowels())

# TICKET 45
# def secondMaxNUmInList():
#     nums_list = list(map(int,input("Enter the list of number: ").split()))
#     max_num = max(nums_list)
#     nums_list.remove(max_num)
#     second_max = max(nums_list)
#     return second_max

# print(secondMaxNUmInList())


# def countOfWords():
#     string = input('Enter the string: ')
#     words = string.split()
#     num_of_words = len(words)
#     return num_of_words

#TICKET 39

# def sumOfDigits():
#     number = int(input('Enter a number: '))
#     sum_of_digits = 0
#     while number > 0:
#         digits = number % 10
#         number //= 10
#         sum_of_digits += digits

#     return sum_of_digits

# print(sumOfDigits())

# TICKET 36

# def findLengthOfLongestWord():
#     sentence = input('Enter a sentence: ')
#     words = sentence.split()

#     longest_word = max(words, key=len)
#     return len(longest_word)

# print(findLengthOfLongestWord())
#question 
# The ASCII (American Standard Code for Information Interchange) table is a character encoding standard that assigns a unique numerical value (0–127) to different characters, including:

#  Standardized Encoding – Ensures text is universally readable across devices.
# 2️⃣ Lightweight & Simple – Uses only 7 bits (values 0-127), making it memory efficient.
# 3️⃣ Fast Processing – Simple integer mapping makes it quick to convert characters.
# 4️⃣ Compatible with Most Systems – ASCII is the foundation for Unicode (UTF-8, UTF-16, etc.).

# TICKET 35
# Mode	Read/Write	File Existence	Truncation (Clears File?)	Cursor Position
# r+	Read & Write	File must exist (raises error if not)	❌ No (keeps existing content)	At the beginning of the file
# w	Write only	Creates a new file if it doesn’t exist	✅ Yes (deletes existing content)	At the beginning of the file



# TICKET 32

# def reverseString():
#     string = input("Enter the string: ")
#     reversed_str = string[::-1]
#     return reversed_str

# print(reverseString())

# TICKET 29
# def mergeAndSortTwoLists():
#     first_list = list(map(int,input('Enter the list of numbers: ').split()))
#     second_list = list(map(int,input('Enter the second list of numbers: ').split()))
#     first_list.extend(second_list)
#     first_list.sort()
#     return first_list

# print(mergeAndSortTwoLists())

# TICKET 26
# def countWordFrequencyInAString():
#     string = input('Enter the sentence: ')
#     words = string.split()
#     word_frequency = {}
#     for word in words:
#         if word in word_frequency:
#             word_frequency[word] +=1
#         else:
#             word_frequency[word] = 1

#     return word_frequency

# print(countWordFrequencyInAString())

# TICKET 30
# def celciusToFahrenHeit():
#     celsius = float(input('Enter the temp in celsius: '))
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# TICKET 31

# def findingCommonels():
#     list1 = list(map(int, input('Enter the first list of numbers: ').split()))
#     list2 = list(map(int, input('Enter the second list of numbers: ').split()))

#     set1 = set(list1)
#     set2 = set(list2)
    
#     back = list(set1.intersection(set2))
#     return back

# print(findingCommonels())

# TICKET 25
# def multiplTable():
#     num = int(input('Enter the number: '))

#     for i in range(1,11):
#         print(f'{num} x {i} = {num*i}')

# multiplTable()

# TICKET 33
# def factorialOfNumber():
#     number = int(input('Enter a number: '))
#     factorial = 1
#     for i in range(1,number+1):
#         factorial *= i
#     print(f'factorial of {number} is {factorial}')

# factorialOfNumber()
#Question
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Please enter a valid integer.")


#TICKET 23

# def evenNumsInList():
#     numbers = list(map(int, input('Enter the list of numbers: ').split()))
#     even_list = []
#     for i in range(0,len(numbers)):
#         if numbers[i] % 2 == 0:
#             even_list.append(numbers[i])
#     return even_list

# print(evenNumsInList())

# TICKET 22
# def sortListInAscendOrd():
#     nums_list = list(map(int, input('Enter the list of numbers').split()))
#     nums_list.sort()
#     return nums_list

# print(sortListInAscendOrd())

# TICKET 20

# def maxElInList():
#     nums_list = list(map(int, input('Enter the list of numbers: ').split()))
#     max_num = max(nums_list)
#     return max_num
#Question
# def get_max(lst):
#     try:
#         return max(lst)
#     except ValueError:
#         return "List is empty, no maximum value."

# nums = []
# print(get_max(nums))  # Output: List is empty, no maximum value.


#TICKET 19

# def fiBonacci():
#     num = int(input('Enter the number of terms: '))
#     fib_sequence = [0, 1]
#     for i in range(2, num):
#         fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
#     return fib_sequence

# print(fiBonacci())
# Question:
# A module in Python is simply a file containing Python definitions and statements, typically a .py file. It can include functions, classes, and variables that you can reuse in your Python code. Modules help organize code into separate files, making it easier to maintain and use.

# Python has many built-in modules (like math, sys, os, etc.), and you can also create your own modules.


# TICKET 18
# Question 
# In Python, positional arguments are arguments that are passed to a function based on their position. The order in which you pass the arguments when calling a function matters, and Python will assign the values to the corresponding parameters in the function based on their position.

# How Do Positional Arguments Work?
# When you define a function, you specify the parameters. The values passed to those parameters when the function is called are considered positional arguments. The first argument passed corresponds to the first parameter in the function definition, the second argument corresponds to the second parameter, and so on.

# def countVowels():
#     string = input('Enter the string: ')
#     vowels = 'aeoiu'
#     string = string.lower()

#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1

#     return count

# print(countVowels())


# TICKET 17

# def reverseStr():
#     string = input("Enter the string: ")
#     reversed_str = string[::-1]
#     return reversed_str

# print(reverseStr())


#CALCULATING FACTORIAL USING RECURSION
# def calcFactorial():
#     number = int(input('Enter a number: '))
#     factorial = 1

#     for i in range(1, number + 1):
#         factorial *= i
#     return factorial

# print(calcFactorial())


# TICKET 16
#CHECKING PRIME NUMBERS

# def is_prime():
#     number = int(input('Enter a number: '))
#     if number <= 1:
#         print('Please enter a number higher that 1')
#         return 0
#     if number > 100:
#         print('The number is too large. Please enter a number between 1 and 100')
    
#     for i in range(2,number):
#         if number % i == 0:
#             return False

#     return True

# print(is_prime())

# TICKET 13

# Question:
# The range(5) function in Python returns an iterable (a sequence of numbers) starting from 0 up to but not including 5. Essentially, it generates the numbers 0, 1, 2, 3, 4. The default behavior of range() is to start from 0 and have a step size of 1.

# So, if you do something like:
# print(list(range(5)))
# How can you include a step value in range()?
# To include a step value, you can provide a third argument to the range() function. The syntax for range() is:
#     range(start, stop, step)

# def read_file_line_by_line(filename):
#     try:
#         with open(filename, 'r') as file:
#             for line in file:
#                 print(line.strip())  
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# filename = input("Enter the filename: ")
# read_file_line_by_line(filename)

#TICKET 1
# def power_list(numbers, exponent):
#     return [num ** exponent for num in numbers]

# # Test the function
# nums = [2, 3, 4, 5]
# exp = 3
# print(power_list(nums, exp))  # Output: [8, 27, 64, 125]

#TICKET 15
# Question:
# name = "Alice"
# age = 25

# formatted_string = "Name: {}, Age: {}".format(name, age)
# print(formatted_string)

# def useListComprehensionToSquareNums():
#     number = int(input('Enter the number:'))
#     list_items = []
#     for i in range(1,number+1):
#         list_items.append(i**2)
#     return list_items

# print(useListComprehensionToSquareNums())

#TICKET 12
# read()
# Purpose: Reads the entire content of the file as a single string.

# How it works:

# It reads all the data in the file at once, and returns it as a string.

# It reads everything in the file, including line breaks (\n).

# Useful when you want to process the entire file at once.

# 2. readline()
# Purpose: Reads a single line from the file.

# How it works:

# It reads one line at a time from the file and returns it as a string.

# The cursor moves to the next line after each call to readline().

# Useful for reading a file line by line.

# 3. readlines()
# Purpose: Reads all the lines from the file and returns them as a list of strings.

# How it works:

# It reads the entire file and returns a list, where each element is a line in the file.

# Each line in the file becomes a string in the list, and line breaks (\n) are retained.

# Useful when you want to process each line as an item in a list.

# def rangeAndPrintWithAsteriks():
#     for i in range(1, 11):
       
#         print(' ' * (10 - i) + '*' * (2 * i - 1))


#rangeAndPrintWithAsteriks()

# def asciiValueReturn():
#     character = input('Enter a character: ')
#     return ord(character)

# print(asciiValueReturn())


#TICKET 6
# def lengthOfString():
#     string = input('Enter a string: ')
#     return len(string)

# print(lengthOfString())


#TICKET 4
# When you try to replace a substring that doesn't exist in the string using the replace() method, nothing will happen, and the original string will be returned unchanged.'
# 'original_string = "Hello, world!"
# new_string = original_string.replace("Python", "Java")
# print(new_string)


# TICKET 2

# def countCharInStr():
#     string = input('Enter a string: ')
#     char = input('Enter a character: ')
#     count = string.count(char)
#     return count

# print(countCharInStr())

# TICKET 5
# TICKET 28

#TICKET 71

# def averageListEls(list):
#     total = 0
#     for num in list:
#         total += num
#     return total / len(list)

# # Test the function

# numbers = [1, 2, 3, 4, 5]
# print(averageListEls(numbers))  # Output: 3.0

# TICKET 70

# def numberOfVowels(string):
#     vowels = 'aeoiu'
#     count = 0
#     string = string.lower()
#     for char in string:
#         if char in vowels:
#             count +=1
#     return count

# # Test the function

# string = 'Hello, Wrld!'
# print(numberOfVowels(string))  # Output: 3

#Ticket 69
# def fibonacciSequence():
#     number = int(input("Enter a number: "))
#     fibonacci = [0,1]
#     for i in range(2,number + 1):
#         fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
#     return fibonacci

# # Test the function

# print(fibonacciSequence())  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#TICKET 74

# def mergingTwoLists(list1,list2):
#     merged_list = list1 + list2
#     new_list = sorted(merged_list)
#     return new_list

# # Test the function

# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# print(mergingTwoLists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# TICKET 73

# def multiplTable(number):
#     for i in range(1,11):
#         print(f"{number} x {i} = {number * i}")


# # Test the function

# multiplTable(5)  # Output: 5 x 1 = 5, 5 x 2 = 10, 5 x 3 = 15, 5 x 4 = 20, 5 x 5 = 25, 5 x 6 = 30, 5 x 7 = 35, 5 x 8 = 40, 5 x 9 = 45, 5 x 10 = 50

#TICKET 75


# def count_unique_elements_in_list(input_list):
#     unique_list = list(set(input_list))  # Convert to set to remove duplicates, then back to list
#     return len(unique_list)

# # Test the function
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
# print(count_unique_elements_in_list(numbers))  # Output: 5


#TICKET 42

# def countOfWords():
#     string = input('Enter a string: ')
#     words = string.split()
#     return len(words)

# print(countOfWords())

#TICKET 21

# def sumEls():
#     nums_list = list(map(int,input("ENter the list of numbers: ").split()))
#     return sum(nums_list)

# print(sumEls())