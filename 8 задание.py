text = input()

words = text.split()
res = ' '.join(sorted(words, key=len))

print(res)
