from databaseinhands import *
clearConsole = lambda: print('\n' * 150)


def name_menu():
    formatText('MENU PERSONALIZATION')
    name = readName_withNumber('Name of your menu: ', 2)
    return str(name)


def styleOptions():
    styleShow_options()
    option = readInt_number('Type your option style: ')
    return option


def columnsName_ofDf():
    columnShow_options()
    column1 = readInt_inOptions('What is the data type of the first column?'
                                '\n> ', 3)
    columnShow_options()
    column2 = readInt_inOptions('What is the data type of the second column?'
                                '\n> ', 3)
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
    types_of_columns = columnsName_ofDf()
    clearConsole()
    name_columns = nameOf_columns()
    clearConsole()
    name_dt = dt_create_with_name()
    return [menu_name, option_style, types_of_columns, name_columns, name_dt]
