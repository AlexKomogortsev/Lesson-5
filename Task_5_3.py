# Task 3

with open('Wages.txt') as search:
    l = []
    cnt = 0
    sum = 0
    for line in search:
        l = line.split(':')
        sum += int(l[1])
        cnt += 1
        if int(l[1]) < 20000:
            print(f'Не доплачиваем: {l[0]}')
    print(f'Средний оклад по всем сотрудникам: {sum / cnt}')
