from visualstratament import *
from menushow_options import *
from databaseinhands import *
from personalization import *

# Parte de personalização
user_options = personalization()
# [menu_name, option_style, types_of_columns, name_columns, name_dt]
# showMenu_head(name_menu=user_options[0], n=user_options[1])
# Mostrar o menu (while True)
while True:
    showMenu_head(name_menu=user_options[0], n=user_options[1])
    showMenu_options(user_options)
    option = readInt_inOptions('Your option > ', n=3)
    if option == 1:
        storeFile(user_options)
    # if option == 2:
        # Criar função para mostrar com vários tipos de formatações
    if option == 3:
        # função para despedida
        break
