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


# Functions for visual "effects"


def formatar(phrase='frase formatada', n=0, show=True):
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


# Functions to verify something


def readoneName(phrase='Name: ', n=0):
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
