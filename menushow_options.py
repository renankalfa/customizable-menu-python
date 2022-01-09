from visualstratament import *


def showMenu(name_menu='no name', n=0):
    formatText(name_menu.upper(), n)


def showMenu_options(*list):
    for pos, value in enumerate(list):
        print(f'\033[33m{pos}\033[m - \033[36m{value}\033[m')

