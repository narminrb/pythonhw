#TICKET 27

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

# TICKET 55
# def checkStrinEnd(filename):
#     return filename.endswith('.txt')

# print(checkStrinEnd('test.txt'))

# TICKET 56

# def removeWhiteSpace():
#     sentence = input('Enter the sentence: ')
#     clean_sentence = sentence.strip()
#     return clean_sentence

# print(removeWhiteSpace())

# TICKET 54

# def checkStringStart(sentence,prefix):
#     sentence = sentence.lower()
#     prefix = prefix.lower()
#     return sentence.startswith(prefix)

# print(checkStringStart('This is a sample sentence', 'this'))


# TICKET 53
# def clacStringLength():
#     sentence = input("Enter a sentence: ")
#     if sentence == '':
#         return 'Empty string'
#     return len(sentence)

# print(clacStringLength())

#Word Frequency Counter

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

#Checking for perfekt numbers

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

# TICKET 51
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

# TICKET 48

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

