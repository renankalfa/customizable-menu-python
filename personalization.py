from visualstratament import *
from databaseinhands import *


def name_menu():
    formatText('MENU PERSONALIZATION')
    name = read_oneName('Name of your menu: ', 2)
    return name


def styleOptions_show():
    styleShow_options()
    option = readInt_number('Type your option style: ')
    return option


def coluns_ofDf():
    # what do your prefer for the first colun?
    colunShow_options()
    colun1 = readInt_inOptions('Enter your choice for column 1')
    return colun1
    # what do your prefer for the second colun?
