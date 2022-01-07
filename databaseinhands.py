from visualstratament import *


def databasename():
    name = readoneName('Database name: ', n=1)
    join = [name, '.txt']
    name_file = ''.join(join)
    try:
        a = open(name_file, 'wt')
    except:
        errormessage()
    else:
        a.close()


databasename()
