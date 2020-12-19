# Task 5

digit = open('Digits.txt', 'w')
digit.write(input('Введите набор чисел через пробел: '))
digit.close()

with open('Digits.txt') as digit:
    s = digit.readline()
    l = s.split()
    sum = 0
    for el in l:
        sum += float(el)
    print(f'Сумма равна: {sum}')
