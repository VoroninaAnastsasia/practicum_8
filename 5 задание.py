str1 = input()
str2 = input()
str3 = input()

all_str = str1 + str2 + str3

for ch in all_str:
    count = 0
    if ch in str1:
        count += 1
    if ch in str2:
        count += 1
    if ch in str3:
        count += 1

    if count == 1:
        print(ch, end='')
