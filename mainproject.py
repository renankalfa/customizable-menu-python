from menushow_options import *
from personalization import *

clearConsole = lambda: print('\n' * 150)
user_options = personalization()
clearConsole()
while True:
    showMenu_head(name_menu=user_options[0], n=user_options[1])
    showMenu_options(user_options)
    option = readInt_inOptions('\033[33mYour option\033[m \033[36m>\033[m ', n=3)
    clearConsole()
    if option == 1:
        storeFile(user_options)
    elif option == 2:
        showDt(user_options)
        nothing = input('Press \033[31menter\033[m to continue > ')
    elif option == 3:
        goodbye_message()
        break
    clearConsole()
