text = input()

words = text.split()
first_word = words[0]

for word in words:
    if word != first_word and len(word) == len(set(word)):
        print(word, end=" ")
