from visualstratament import *


def showMenu_head(name_menu='no name', n=0):
    formatText(name_menu.upper(), n)


def showMenu_options(*li):
    for pos, value in enumerate(li):
        print(f'\033[33m{pos}\033[m - \033[36m{value}\033[m')