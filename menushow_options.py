from visualstratament import *


def showMenu_head(name_menu='no name', n=0):
    formatText(name_menu.upper(), n)


def showMenu_options(*li):
    lis = [f'New registry ({li[0][3][0]}, {li[0][3][1]})', f'See "{li[0][4]}" database', 'Close Menu']
    for pos, value in enumerate(lis):
        print(f'\033[33m{pos + 1}\033[m - \033[36m{value}\033[m')
    dividerLine(n=li[0][1])
