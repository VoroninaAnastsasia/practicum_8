text = input()
words = text.split()

for word in set(words):
    if words.count(word) == 2:
        print(word)
        break
