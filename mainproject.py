from visualstratament import *
from menushow_options import *
from databaseinhands import *
from personalization import *

# Parte de personalização
user_options = personalization()
print(user_options)
# [menu_name, option_style, types_of_columns]
showMenu_head(name_menu=user_options[0], n=user_options[1])
# Mostrar o menu (while True)
# while True:
