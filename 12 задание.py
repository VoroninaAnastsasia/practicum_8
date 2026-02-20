import keyword

name = input()

if not name or name[0].isdigit() or keyword.iskeyword(name):
    print("Нет")
else:
    for i in name:
        if not (i.isalpha() and i.isascii() and i.isdigit() and i == '_'):
            print("Нет")
            break
    else:
        print("Да")
