text = input()
words = text.split()

for word in words:
    if words.count(word) == 2:
        print(word)
        break
