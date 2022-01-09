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


def dividerLine(n=0, t=40):
    if n == 0:
        print('=' * t)
    if n == 1:
        print('~' * t)
    if n == 2:
        print('-' * t)


def styleShow_options():
    dividerLine(0, 38)
    allindict = {'Style1': '=', 'Style2': '~', 'Style3': '-'}
    for values in allindict.values():
        print(f'{values * 6:>10}', end='  ')
    print()
    for keys in allindict.keys():
        print(f'{keys:>10}', end='  ')
    print()
    for values in allindict.values():
        print(f'{values * 6:>10}', end='  ')
    print()
    dividerLine(0, 38)





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


def readName_withNumber(phrase='Name: ', n=0):
    while True:
        name = input(phrase)
        list_words = name.split()
        c = 0
        for word in list_words:
            if word.isalnum() is False:
                errormessage(1)
                c += 1
        if c == 0:
            break
    if n == 0:
        return ' '.join(list_words)
    if n == 1:
        return ' '.join(list_words).lower()
    if n == 2:
        return ' '.join(list_words).upper()


def readInt_number(pharse='Number: '):
    number = input(pharse)
    while not number.isdigit():
        errormessage(2)
        number = input(pharse)
    return number
