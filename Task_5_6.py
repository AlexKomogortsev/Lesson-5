# Task 6

def dsum(a):
    s = str('')
    l = []
    sum = 0
    for el in a:
        if el.isdigit() == True:
            s += el
        elif el == '(':
            l.append(s)
            s = ''
        if el == a[-1]:
            for x in l:
                sum += int(x)
    return sum


with open('Study.txt') as study:
    finaldic = {}
    for line in study:
        l = line.split(':')
        d = {l[0]: dsum(l[1])}
        finaldic.update(d)
    print(finaldic)
