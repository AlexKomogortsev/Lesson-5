# Task 4

mapper = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}

with open('Integers.txt') as ints:
    for line in ints:
        l = line.split(' ')
        l[0] = mapper[l[0]]
        s = ' '.join(l)
        with open('IntegersTranslate.txt', 'a') as intr:
            intr.write(f'{s}\n')
