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
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for word in list_sentence:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
length_words = len(words)
average_length_words = sum(len(count) for count in words)
print(average_length_words / length_words)
