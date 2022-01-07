# Functions for visual "effects"


def errormessage(n=0):
    """
    Create a error message
    :param n: 0 -> generic, 1 -> name, 2 -> integer and 3 -> real/float
    :return: error message
    """
    if n == 0:
        print('\033[31mError! Try again! \033[m')
    if n == 1:
        print('\033[31mError! Try to enter a valid name!\033[m')
    if n == 2:
        print('\033[31mError! Try to enter a valid integer!\033[m')
    if n == 3:
        print('\033[31mError! Try to enter a valid real number!\033[m')


def formatText(phrase='frase formatada', n=0, show=True):
    if n == 0:
        if show is True:
            print('=' * 40)
            print(f'{phrase.center(40).upper()}')
            print('=' * 40)
        return n
    if n == 1:
        if show is True:
            print('~' * 40)
            print(f'{phrase.center(40).upper()}')
            print('~' * 40)
        return n
    if n == 2:
        if show is True:
            print('-' * 40)
            print(f'{phrase.center(40).upper()}')
            print('-' * 40)
        return n


def dynamicFormat(phrase='no phrase', n=0):
    size = len(phrase) + 2
    if n == 0:
        print('=' * size)
        print(f'{phrase.center(size).upper()}')
        print('=' * size, end='')
    if n == 1:
        print('~' * size)
        print(f'{phrase.center(size).upper()}')
        print('~' * size)
    if n == 2:
        print('-' * size)
        print(f'{phrase.center(size).upper()}')
        print('-' * size)


def dividerLine(n):
    if n == 0:
        print('=' * 40)
    if n == 1:
        print('~' * 40)
    if n == 2:
        print('-' * 40)


# Functions to verify something


def read_oneName(phrase='Name: ', n=0):
    """
    Checker that the user correctly typed a name
    :param phrase: phrase you want to use in the input
    :param n: n=0 -> normal phrase, n=1 -> lower phrase and n=2 -> upper phrase
    :return: just the correct name
    """
    name = input(phrase)
    while not name.isalpha():
        errormessage(1)
        name = input(phrase)
    if n == 0:
        return name
    elif n == 1:
        return name.lower()
    elif n == 2:
        return name.upper()


# Functions to customize menu

def welcome():
    formatText('Welcome to creating your menu')



def styleChoice(n=0):
    print(f'{dynamicFormat("Style 1", n=0)}', end='')
    print(f'{dynamicFormat("Style 2", n=1)}', end='')
    print(f'{dynamicFormat("Style 3", n=1)}', end='')


#styleChoice()