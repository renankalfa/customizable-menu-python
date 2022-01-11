from visualstratament import *
from databaseinhands import *


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
    column1 = readInt_inOptions('Enter your choice for column 1: ', 3)
    columnShow_options()
    column2 = readInt_inOptions('Enter your choice for column 2: ', 3)
    return [column1, column2]


def personalization():
    welcomemessage()
    menu_name = name_menu()
    option_style = styleOptions()
    types_of_columns = columnsName_ofDf()
    name_dt = dt_create_with_name()
    return [menu_name, option_style, types_of_columns, name_dt]


# [menu_name, option_style, types_of_columns]
