cities = input().split()

for i in range(1,  len(cities)):
    if (cities[i-1][-1].lower()) != cities[i][0].lower():
        if i % 2 == 0:
            print('Вася')
        else:
            print('Петя')
        break
else:
    if (len(cities) - 1) % 2 == 0:
        print('Петя')
    else:
        print('Вася')
