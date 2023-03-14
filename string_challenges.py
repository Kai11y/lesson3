# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'.lower()
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
print(len([word for word in word if word in 'ауоыиэяюёе']))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence) - sentence.count(' '))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for sent in list_sentence:
    print(sent[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
word=sentence.split()
length=len(word)
average_length = sum(len(count) for count in word)
print(average_length/length)
