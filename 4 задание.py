text = input()
text = text.lower()

for ch in text:
    if text.count(ch) == 3:
        print(ch)
        break
