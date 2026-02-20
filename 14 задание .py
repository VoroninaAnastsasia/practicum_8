hint = input()
word = input()

i = 0
while i < 25:
    print()
    i += 1

hidden = ''
j = 0
while j < len(word):
    hidden += '*'
    j += 1

attempt = 10

while attempt > 0:
    print(hint)
    print(hidden)

    print('Буква или слово (о - буква, 1 - слово)?')
    choice = input()

    if choice == '0':
        letter = input()

        new_hidden = ''
        k = 0

        while k < len(word):
            if word[k] == letter:
                new_hidden += letter
            else:
                new_hidden += hidden[k]
            k += 1
            
        hidden = new_hidden
        
        if hidden == word:
            print('Победа!')
            break
        attempt -= 1
    elif choice == '1':
        guess = input()

        if guess == word:
            print('Победа!')
            break
        else:
            print('Проигрыш!')
            break
if hidden != word and attempt == 0:
    print('Проигрыш!')
