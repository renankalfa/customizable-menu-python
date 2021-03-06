from visualstratament import *
from time import sleep


def dt_create_with_name():
    formatText('creating database and name')
    name = read_oneName('Database name \033[36m>\033[m ', n=1)
    join = [name.lower(), '.txt']
    name_file = ''.join(join)
    try:
        a = open(name_file, 'w', encoding='utf-8')
        sleep(1)
    except Exception as error:
        print(error)
    else:
        a.close()
        return name_file


def nameOf_columns():
    dividerLine()
    name1 = '\033[46mfirst column name\033[m'
    name2 = '\033[43msecond columnn name\033[m'
    print(f'{name1:<30}{name2}')
    dividerLine()
    template = {'undefined': 0, 'undefined2': 0}
    for keys, values in template.items():
        print(f'{keys:<22}{values}')
    dividerLine()
    name1 = readMultiples_Names('\033[36mFirst column name\033[m > ')
    name2 = readMultiples_Names('\033[33mSecond column name\033[m > ')
    dividerLine()
    return [name1, name2]


def writeType_dt(*lis):
    c1 = 'undefined'
    c2 = 0
    sleep(0.3)
    formatText(f'ADDING {lis[0][3][0].upper()} and {lis[0][3][1].upper()}', n=lis[0][1])
    sleep(0.5)
    if lis[0][2][0] == 1:
        c1 = readMultiples_Names(f'\033[36m{lis[0][3][0]}\033[m > ')
    elif lis[0][2][0] == 2:
        c1 = readInt_number(f'\033[36m{lis[0][3][0]}\033[m > ')
    elif lis[0][2][0] == 3:
        c1 = readFloat_number(f'\033[36m{lis[0][3][0]}\033[m > ')
    if lis[0][2][1] == 1:
        c2 = readMultiples_Names(f'\033[33m{lis[0][3][1]}\033[m > ')
    elif lis[0][2][1] == 2:
        c2 = readInt_number(f'\033[33m{lis[0][3][1]}\033[m > ')
    elif lis[0][2][1] == 3:
        c2 = readFloat_number(f'\033[33m{lis[0][3][1]}\033[m > ')
    dividerLine(n=lis[0][1])
    return [c1, c2]


def storeFile(*lis):
    try:
        a = open(lis[0][4], 'a', encoding='utf-8')
        sleep(0.3)
        add_this = writeType_dt(lis[0])
        a.write(f'{str(add_this[0])};{str(add_this[1])}\n')
    except Exception as error:
        print(f'{error}')
    else:
        a.close()


def showDt(*lis):
    try:
        a = open(lis[0][4], 'rt', encoding='utf-8')
    except Exception as error:
        print(error)
        print('\033[31mError reading file!\033[m')
    else:
        sleep(0.3)
        dividerLine(lis[0][1], 50)
        sleep(0.3)
        print(f'\033[36m{lis[0][3][0]:<30}\033[33m{lis[0][3][1]}\033[m')
        sleep(0.3)
        dividerLine(lis[0][1], 50)
        for linha in a:
            sleep(0.5)
            dado = linha.replace('\n', '').split(';')
            print(f'\033[36m{dado[0]:<30}\033[m', end='')
            print(f'\033[33m{dado[1]}\033[m')
        sleep(0.5)
        dividerLine(lis[0][1], 50)
