while True:
    print('retornou')
    name = input('Nome: ')
    list_words = name.split()
    c = 0
    for word in list_words:
        if word.isalpha() is False:
            print('erro')
            c += 1
    if c == 0:
        break

print(name)