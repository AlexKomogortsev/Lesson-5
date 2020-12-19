# Task 1

from io import TextIOWrapper

task = open('testfile.txt', 'a')
s = input('Введите строку: ')
while s != '':
    task.write(s)
    task.write('\n')
    s = input('Введите строку: ')

task.close()
