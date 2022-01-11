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
    name1 = read_oneName('First column name: ')
    name2 = read_oneName('Second column name: ')
    return [name1, name2]


def writeType_dt(c1=1, c2=2):
    if c1 == 1:
        name = readMultiples_Names('Name of element: ')
    if c1 == 2:
        number_int = readInt_number('Integer Number: ')
    if c1 == 3:
        number_float = readFloat_number('Float Number: ')


# Name_dt, int and int
# Name_dt, int and float
# Name_dt, int and name

# Name_dt, float and int
# Name_dt, float and float
# Name_dt, float and name
# [menu_name, option_style, types_of_columns, name_dt]

def storeFile(menu_name='', c1=1, c2=2):
    try:
        a = open(menu_name, 'r', encoding='utf-8')
        conteudo = a.readline()
        conteudo.append(f'{c1};{c2}\n')
    except Exception as error:
        print(f'{error}')


li = ['KALFA MENU', 1, [1, 2], 'kalfa.txt']
storeFile(menu_name=li[0], c1=li[2][0], c2=li[2][1])
