# Task 2

task = open('UFC256.txt', 'a')
task.write('\nВ данном карде вы видите бой за Титул Чемпиона в наименьшей весовой категории\n')
task.write('А в Соглавном бою вы также можете наблюдать схватку за Претендентский статус в Легкой категории')
task.close()

task = open('UFC256.txt', 'r')
line_count = 0
for x in task:
    line_count += 1
print(f'Получилось {line_count} строк')

task.close()

task = open('UFC256.txt', 'r')
word_count = 0
for x in task:
    word_count += len(x.split())
print(f'Получилось {word_count} слов')

task.close()
