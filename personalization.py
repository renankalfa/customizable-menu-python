from databaseinhands import *
clearConsole = lambda: print('\n' * 150)


def name_menu():
    print('=' * 50)
    print('                  \033[46mYOUR NAME MENU\033[m')
    print('=' * 50)
    print('1 - building... \n2 - building... \n3 - building...')
    dividerLine()
    name = readName_withNumber('\033[36mName of your menu > \033[m', 2)
    return str(name)


def styleOptions():
    styleShow_options()
    option = readInt_inOptions('Type your option style \033[36m>\033[m ', 3)
    return option


def columnsName_ofDf():
    dividerLine()
    name1 = '\033[46mfirst column\033[m'
    name2 = '\033[43msecond columnn\033[m'
    print(f'{name1:<30}{name2}')
    dividerLine()
    template = {'\033[36mRenan Barbosa\033[m': '\033[33m20\033[m', '\033[36m20\033[m': '\033[33m4\033[m',
                '\033[36mBanana\033[m': '\033[33m2.99\033[m'}
    for keys, values in template.items():
        print(f'{keys:<30}{values}')
    columnShow_options()
    column1 = readInt_inOptions('What is the data type of the first column?'
                                '\n\033[33m>\033[m ', 3)
    columnShow_options()
    column2 = readInt_inOptions('What is the data type of the second column?'
                                '\n\033[33m>\033[m ', 3)
    return [column1, column2]


def personalization():
    sleep(0.3)
    welcomemessage()
    sleep(1.5)
    clearConsole()
    menu_name = name_menu()
    clearConsole()
    option_style = styleOptions()
    clearConsole()
    name_columns = nameOf_columns()
    clearConsole()
    types_of_columns = columnsName_ofDf()
    clearConsole()
    name_dt = dt_create_with_name()
    return [menu_name, option_style, types_of_columns, name_columns, name_dt]
