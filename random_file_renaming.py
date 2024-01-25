'''
    Author:  Andrii S
    Created: 25 Jan 2023
    Description: This script renames all files in current folder to random names
'''

import os


FOLDER_PATH = ''


def create_file_name(old_name) -> str:
    from random import randint

    extension = old_name.split('.')[-1]

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '1234567890'

    name_length = randint(5, 12)   
    file_name = '' 
    for i in range(0, name_length):
        file_name += ALPHABET[randint(0, len(ALPHABET) - 1)] 

    return file_name + '.' + extension


if __name__ == '__main__':
    files = [
        f for f in os.listdir('.') 
        if os.path.isfile(f)
    ]

    script_name = __file__.split('\\')[-1]
    
    for old_file_name in files:
        if old_file_name == script_name:
            continue

        new_name = create_file_name(old_file_name)
        
        os.rename(
            os.path.join(FOLDER_PATH, old_file_name),
            new_name 
        )



