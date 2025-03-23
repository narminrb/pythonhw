
sentence = 'I study at Khazar University'
#output Is tu dy at Kh az ar Un iv er si ty

print(sentence)
sentence = sentence.replace(' ', '')
print(sentence)
a =[]
for i in range(0,len(sentence),2):
   a.append(sentence[i:i+2])

print(a)
print(' '.join(a))