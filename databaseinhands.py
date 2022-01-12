from visualstratament import *


def dt_create_with_name():
    formatText('creating database and name')
    name = read_oneName('Database name: ', n=1)
    join = [name, '.txt']
    name_file = ''.join(join)
    try:
        a = open(name_file, 'wt', encoding='utf-8')
    except:
        errormessage()
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
    c1 = ''
    c2 = ''
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


li = ['KALFA MENU', 1, [1, 3], ['Nome da família', 'Numero favorito'], 'kalfa.txt']
lup = ('1', '2', 'Nome da família', 'Numero favorito')
# [menu_name, option_style, types_of_columns, name_columns, name_dt]
#     0            1                 2            3            4


def storeFile(*lis):
    try:
        print(lis[0][4])
        a = open(lis[0][4], 'a', encoding='utf-8')
        add_this = writeType_dt(lis[0])
        a.write(f'{str(add_this[0])};{str(add_this[1])}\n')
    except Exception as error:
        print(f'{error}')
    else:
        # a = open(lis[0][4], 'wt', encoding='utf-8')
        # a.writelines(conteudo)
        a.close()


storeFile(li)
