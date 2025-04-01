#TICKET 27

# def sumOfDigits():
#     number = int(input("Enter a number:"))
#     if number < 0:
#         return 'The number must be positive'
#     sum = 0
#     while number > 0:
#         digit = number % 10
#         number //=10
#         sum+=digit
#     return sum

# print(sumOfDigits())

#---------------------

#TICKET 64

# def intDivision():
#     number = float(input("Enter a number: "))
#     divider = float(input("Enter the divider: "))
#     quotient = number // divider
#     remainder = number % divider
#     return f"The quotient is {quotient} and the remainder is {remainder}"

# print(intDivision())

#---------------------

# # TICKET 65
# def formatNumbers(number):
#     formatted_number = '{:10.2f}'.format(number)
#     return formatted_number

# print(formatNumbers(15.6789))
# question:
# string = 'Khazar uni'
# formatted = string.encode('utf-8')

# print(formatted)

#---------------------

#TICKET 63

# def roundNums():
#     number = float(input("Enter a number: "))
#     formatted_num = round(number,2)
#     return formatted_num

# print(roundNums())


#---------------------

# TICKET 62
# def calcPowers():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     return num1 * num2

# print(calcPowers())

#---------------------

# TICKET 61

# def calcAbsValue():
#     number = int(input("Enter a number: "))
#     abs_value = abs(number)
#     return "This is absolute value {}".format(abs_value)

# print(calcAbsValue())


#---------------------

# TICKET 60
# def removeSuffix(filename):
#     return filename.removesuffix('.html')
    

# print(removeSuffix('myfile.html'))

#---------------------

# TICKET 58
# def replaceSubstr():
#     sentence = input("Please enter a sentence: ")
#     words = sentence.split()
#     word = 'Python'
#     if word in words:
#         index = words.index(word)
#         words[index] = 'Javascript'

#     new_sentence = ' '.join(words)
#     return new_sentence
# print(replaceSubstr())

# def replaceSubstr():
#     sentence = input("Please enter a sentence: ")
#     if "Python" in sentence:
#         sentence = sentence.replace('Python', 'Javascript')
#     return sentence

# print(replaceSubstr())
# Question 

# def replace_first_occurrence():
#     sentence = input("Please enter a sentence: ")
#     if 'Python' in sentence:  
#         sentence = sentence.replace('Python', 'JavaScript', 1)  # Only replace first occurrence
#     return sentence

# print(replace_first_occurrence())

#TICKET 53
# def calcStrLength():
#     string = input("Enter the string: ")
#     return len(string)

# print(calcStrLength())

#---------------------

# WORD FREQUENCY COUNTER

def wordFreqCounter(filename):
    word_frequency = {}
    try :
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().lower()
            words = content.split()
            for words in words:
                word = word.strip(':;?",.')
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
        
        sorted_word_frequency = dict(sorted_word_frequency.items(), key = lambda item: item[1] , reversed=True)

        for word,freq in sorted_word_frequency.items():
            print(f"{word} frequency {freq}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

filename = 'example.txt'

wordFreqCounter(filename)


