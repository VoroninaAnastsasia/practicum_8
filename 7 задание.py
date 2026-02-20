text = input()

words = text.split()
min_length = len(words[0])

for word in words:
    word_length = len(word)
    if word_length < min_length:
        min_length = word_length

print(min_length)
