from visualstratament import *
from databaseinhands import *


def name_menu():
    formatText('MENU PERSONALIZATION')
    name = readName_withNumber('Name of your menu: ', 2)
    return name


def styleOptions():
    styleShow_options()
    option = readInt_number('Type your option style: ')
    return option


def colunsName_ofDf():
    colunShow_options()
    column1 = readInt_inOptions('Enter your choice for column 1: ', 3)
    colunShow_options()
    column2 = readInt_inOptions('Enter your choice for column 2: ', 3)
    return [column1, column2]


name_menu()
styleOptions()
colunsName_ofDf()
