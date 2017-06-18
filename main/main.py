from pyslideshare import pyslideshare
from functions import *
from localsettings import username, password, api_key, secret_key
requires_for_uploading =['username', 'password',
                         'slideshow_title', 'slideshow_srcfile', 'slideshow_description',
                         'slideshow_tags', 'make_src_public', 'make_slideshow_private',
                         'generate_secret_url', 'allow_embeds', 'share_with_contacts']
dict_of_params = {'api_key': api_key, 'secret_key':secret_key, 'username':username, 'password':password}
obj = pyslideshare(params_dict=dict_of_params)
functions_list = {
    'get_by_tag':get_by_tag,
    'count_by_tag':count_by_tag,
    'get_by_user': get_by_user,
    'count_by_user': count_by_user,
    'download': download_slideshow,
    'upload': upload_slideshow,
    'delete':delete_slideshow
}

def make_call(commands_list):
    string_of_commands = ', '.join([keys for keys in commands_list])
    print("'smth' and 'smth' is correct")
    command_input = input('Choose operation: ' + string_of_commands + '\n')
    command_input = command_input.replace(' ', '').split('and')
    for commands in command_input:
        try:
            commands_list[commands](obj)
        except KeyError:
            print('Incorrect command.')
            continue




def main():
    while True:
        start = str(input('Start or break?\n'))
        if start.lower() == 'start':
            make_call(functions_list)
        else:
            break

main(