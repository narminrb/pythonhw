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