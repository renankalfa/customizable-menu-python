from visualstratament import *
import os
from time import sleep


def dt_create_with_name():
    formatText('creating database and name')
    name = read_oneName('Database name: ', n=1)
    join = [name, '.txt']
    name_file = ''.join(join)
    try:
        a = open(name_file, 'w+', encoding='utf-8')
        sleep(1)
        a.flush()
        os.fsync(a.fileno())
    except Exception as error:
        print(error)
    else:
        a.close()
        return name_file


# Name_dt, name and int
# Name_dt, name and float
# Name_dt, name and name


def nameOf_columns():
    name1 = readMultiples_Names('First column name: ')
    name2 = readMultiples_Names('Second column name: ')
    return [name1, name2]


def writeType_dt(*lis):
    c1 = 1
    c2 = 2
    if lis[0][2][0] == 1:
        c1 = readMultiples_Names(f'{lis[0][3][0]}: ')
    if lis[0][2][0] == 2:
        c1 = readInt_number(f'{lis[0][3][0]}: ')
    if lis[0][2][0] == 3:
        c1 = readFloat_number(f'{lis[0][3][0]}: ')
    if lis[0][2][1] == 1:
        c2 = readMultiples_Names(f'{lis[0][3][1]}: ')
    if lis[0][2][1] == 2:
        c2 = readInt_number(f'{lis[0][3][1]}: ')
    if lis[0][2][1] == 3:
        c2 = readFloat_number(f'{lis[0][3][1]}: ')
    return [c1, c2]


# li = ['KALFA MENU', 1, [2, 2], ['Nome', 'Numero favorito'], 'kalfa.txt']
# [menu_name, option_style, types_of_columns, name_columns, name_dt]
#     0            1                 2            3            4


def storeFile(*lis):
    try:
        a = open(lis[0][4], 'a', encoding='utf-8')
        sleep(1)
        add_this = writeType_dt(lis[0])
        a.flush()
        os.fsync(a.fileno())
        a.write(f'{str(add_this[0])};{str(add_this[1])}\n')
    except Exception as error:
        print(f'{error}')
    else:
        a.close()


#                                 0                                      1
#            0        1     2                   3                      4
# lis = (['KALFA MENU', 2, [1, 2], ['Names', 'Favorite Numbers'], 'catálogo.txt'],)
# print(f'{lis[0][3][0]:<30}{lis[0][3][1]}')


def showDt(*lis):
    try:
        a = open(lis[0][0][4], 'rt', encoding='utf-8')
    except Exception as error:
        print(error)
        print('\033[31mError reading file!\033[m')
    else:
        dividerLine(lis[0][0][1], 50)
        print(f'{lis[0][0][3][0]:<30}{lis[0][0][3][1]}')
        dividerLine(lis[0][0][1], 50)
        for linha in a:
            dado = linha.replace('\n', '').split(';')
            print(f'{dado[0]:<30}',end='')
            print(f'{dado[1]}')
        dividerLine(lis[0][0][1], 50)
