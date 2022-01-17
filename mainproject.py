from menushow_options import *
from personalization import *

user_options = personalization()
while True:
    showMenu_head(name_menu=user_options[0], n=user_options[1])
    showMenu_options(user_options)
    option = readInt_inOptions('Your option > ', n=3)
    if option == 1:
        storeFile(user_options)
    if option == 2:
        showDt(user_options)
        nothing = input('Press enter to continue > ')
    if option == 3:
        goodbye_message(user_options[1])
        break
