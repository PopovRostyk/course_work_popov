from pyslideshare import pyslideshare
from functions import *
functions_list = {
    'get_by_tag':get_by_tag(),
    'count_by_tag':count_by_tag(),
    'get_by_user': get_by_user(),
    'count_by_user': count_by_user(),
    'download': download_slideshow(),
    'upload': upload_slideshow(),
    'delete':delete_slideshow()
}

def main():
    pass

def make_call(commands_list):
    string_of_commands = ', '.join([keys for keys in commands_list])
    command = input('Choose operation: ' + string_of_commands)
    try:
        commands_list[command]
    except KeyError:
        print('Operation not in list')

make_call(functions_list)



