from visualstratament import *


def name_menu():
    formatText('MENU PERSONALIZATION')
    name = read_oneName('Name of your menu: ', 2)
    return name


def style_menu():
    formatText('STYLE PERSONALIZATION')
    style_option = int(input('Style: '))
