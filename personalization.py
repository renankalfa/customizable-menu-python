from visualstratament import *


def name_menu():
    formatText('MENU PERSONALIZATION')
    name = read_oneName('Name of your menu: ', 2)
    return name


def styleOptions_show():
    dividerLine(0)
    dict = {'Style1': '=', 'Style2': '~', 'Style3': '-'}
    for values in dict.values():
        print(f'{values * 6}', end='  ')
    print()
    for keys in dict.keys():
        print(f'{keys}', end='  ')
    print()
    for values in dict.values():
        print(f'{values * 6}', end='  ')
    print()
    dividerLine(0)
