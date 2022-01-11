from visualstratament import *


def dt_create_with_name():
    formatText('creating database and name')
    name = read_oneName('Database name: ', n=1)
    join = [name, '.txt']
    name_file = ''.join(join)
    try:
        a = open(name_file, 'wt', encoding='utf-8')
    except:
        errormessage()
    else:
        a.close()
        return name_file


# Name_dt, name and int
# Name_dt, name and float
# Name_dt, name and name

# Name_dt, int and int
# Name_dt, int and float
# Name_dt, int and name

# Name_dt, float and int
# Name_dt, float and float
# Name_dt, float and name

def storeFile(*settings):
    print('k')
