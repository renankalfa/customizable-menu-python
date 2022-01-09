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


def coluns_ofDf(n):
    return n
    # what do your prefer for the first colun?

    # what do your prefer for the second colun?
