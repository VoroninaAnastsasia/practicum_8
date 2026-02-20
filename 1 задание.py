text = input()

maxspace = 0
space = 0

for ch in text:
    if ch.isspace():
        space += 1
        maxspace = max(maxspace,space)
    else:
        space = 0

print(maxspace)
