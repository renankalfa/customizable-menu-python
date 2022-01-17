from time import sleep


def errormessage(n=0):
    """
    Create a error message
    :param n: 0 -> generic, 1 -> name, 2 -> integer and 3 -> real/float
    :return: error message
    """
    if n == 0:
        print('\033[31mError! Try again! \033[m')
    elif n == 1:
        print('\033[31mError! Try to enter a valid name!\033[m')
    elif n == 2:
        print('\033[31mError! Try to enter a valid integer!\033[m')
    elif n == 3:
        print('\033[31mError! Try to enter a valid real number!\033[m')
    elif n == 4:
        print('\033[31mError! Try entering a valid integer between options!\033[m')


def formatText(phrase='frase formatada', n=0, show=True):
    if n == 0:
        if show is True:
            print('=' * 50)
            print(f'{phrase.center(50).upper()}')
            print('=' * 50)
        return n
    elif n == 1:
        if show is True:
            print('~' * 50)
            print(f'{phrase.center(50).upper()}')
            print('~' * 50)
        return n
    elif n == 2:
        if show is True:
            print('-' * 50)
            print(f'{phrase.center(50).upper()}')
            print('-' * 50)
        return n


def dynamicFormat(phrase='no phrase', n=0):
    size = len(phrase) + 2
    if n == 0:
        print('=' * size)
        print(f'{phrase.center(size).upper()}')
        print('=' * size, end='')
    elif n == 1:
        print('~' * size)
        print(f'{phrase.center(size).upper()}')
        print('~' * size)
    elif n == 2:
        print('-' * size)
        print(f'{phrase.center(size).upper()}')
        print('-' * size)


def dividerLine(n=0, t=50):
    if n == 0:
        print('=' * t)
    elif n == 1:
        print('~' * t)
    elif n == 2:
        print('-' * t)


def styleShow_options():
    dividerLine(0, 50)
    to_format = {'Style1': '=', 'Style2': '~', 'Style3': '-'}
    for values in to_format.values():
        print(f'{values * 6:>13}', end='  ')
    print()
    for keys in to_format.keys():
        print(f'{keys:>13}', end='  ')
    print()
    for values in to_format.values():
        print(f'{values * 6:>13}', end='  ')
    print()
    dividerLine(0, 50)


def columnShow_options(n=50):
    dividerLine(t=n)
    options_list = ['Names in general', 'Integer Numbers', 'Float Numbers']
    cont = 1
    for option_name in options_list:
        print(f'\033[33m{cont}\033[m - \033[36m{option_name}\033[m')
        cont += 1
    dividerLine(t=n)


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
    elif n == 1:
        return ' '.join(list_words).lower()
    elif n == 2:
        return ' '.join(list_words).upper()


def readMultiples_Names(phrase='Name: ', n=0):
    while True:
        name = input(phrase)
        list_words = name.split()
        c = 0
        for word in list_words:
            if word.isalpha() is False:
                errormessage(1)
                c += 1
        if name.strip() == '':
            errormessage(1)
            c += 1
        if c == 0:
            break
    if n == 0:
        return ' '.join(list_words)
    elif n == 1:
        return ' '.join(list_words).lower()
    elif n == 2:
        return ' '.join(list_words).upper()


def readInt_number(phrase='Number: '):
    number = input(phrase)
    while not number.isdigit():
        errormessage(2)
        number = input(phrase)
    return int(number)


def readFloat_number(phrase='Number float: '):
    number = input(phrase)
    while not number.replace('.', '').replace(',', '').isnumeric():
        errormessage(3)
        number = input(phrase)
    return float(number)


def readInt_inOptions(phrase='Number in options: ', n=2):
    number = input(phrase)
    while not number.isdigit():
        errormessage(2)
        number = input(phrase)
    number = int(number)
    while number < 1 or number > n:
        errormessage(4)
        number = readInt_number(phrase)
    return number


def welcomemessage():
    print('\033[36m', end='')
    formatText('WELCOME TO MENU PERSONALIZATION')
    print('\033[m')


def goodbye_message(n=0):
    sleep(0.5)
    print('\033[33m')
    dividerLine()
    sleep(0.5)
    print('\033[36m')
    print('it\'s never goodbye'.center(50))
    print('\033[33m')
    sleep(0.5)
    dividerLine()
