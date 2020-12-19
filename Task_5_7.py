# Task 7

import json

def profit(line):
    l = line.split()
    income = int(l[2]) - int(l[3])
    return income


def firmname(line):
    l = line.split()
    return l[0]


with open('Firms.txt') as company:
    profitdic = {}
    average_profit = {}
    averageprofit = 0
    cnt = 0
    reestr = []
    for line in company:
        d = {firmname(line): profit(line)}
        profitdic.update(d)
    for el in profitdic.values():
        if el < 0:
            pass
        else:
            averageprofit += el
            cnt += 1
    averageprofit = averageprofit / cnt
    average_profit = {'average_profit': averageprofit}
    reestr.append(profitdic)
    reestr.append((average_profit))
    print(reestr)

with open('profit_api.json', 'w') as profit_api:
    json.dump(reestr, profit_api)
