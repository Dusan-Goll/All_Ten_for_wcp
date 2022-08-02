# heavily under construction

import os
from random import choice

separ = '-' * 40
bm_list = ['ROWS MENU:',
           'homerow (beginners starts here)',
           'querty-row',
           'zxcv-row',
           'words',
           'exit']


def menu_list_print(menu_list):
    """Prints enumerated menu from list, first item must be menu name.
    Enumerating starts on index 1."""
    for inx, item in enumerate(menu_list):
        if inx == 0:
            print(item)
        else:
            print(f'{inx} - {item}')


# This function will be imported to program body 'All_Ten_in_wcp.py'
# and through several sub-functions (sub-menus) will return final text to typing practise
def base_menu():
    menu_list_print(bm_list)
    print(separ, 'Please, select one option:', sep='\n')
    return input('>')


while True:
    os.system('cls')
    selection = base_menu()
    if not selection.isdecimal():
        continue
    else:
        selected = int(selection)
        if selected not in range(1, len(bm_list)):
            continue
        elif selected == 1:
            homerow_menu()
        elif selected == 2:
            qwerty_row_menu()
        elif selected == 3:
            zxcv_row_menu()
        elif selected == 4:
            words_menu()
        elif selected == 5:  # exit loop
            break


def homerow_menu():
    hr_menu = ['HOMEROW MENU:',
               'letters "fj"',
               'letters "dk"',
               'letters "sl"',
               'letter "a" & symbol ";"',
               'letters "gh"',
               'symbol "'" & enter",
               'exit']

    while True:
        os.system('cls')
        menu_list_print(hr_menu)
        print(separ, 'Please, select one option:', sep='\n')
        sect = input('>')
        if not sect.isdecimal() and int(sect) not in range(1, len(hr_menu)):
            continue
        else:
            selected_letters = int(sect)
            break
    if sect == 1:
        fj_lessons()
    elif sect == 2:
        dk_lessons()
    elif sect == 3:
        sl_lessons()
    elif sect == 4:
        a_lessons()
    elif sect == 5:
        gh_lessons()
    elif sect == 6:
        enter_lessons()
    elif sect == 7:
        # exit .... how to return to first while loop?)


# other rows menu functions
def qwerty_row_menu():
    pass


def zxcv_row_menu():
    pass


def words_menu():
    pass


lessons_fj = ['lessons with "f" & "j":',
              "fj - doubles",  # like: 'fj jf fj jj ff jf ff ...'
              "fj - triples",  # like: 'fjf jfj ffj jjf jfj ....'
              "fj - quartet",  # like: 'fjfj fjjf jffj jfjf ....'
              "exit"]

lessons_dk = ['lessons with "d" & "k":',
              "dk - doubles",  # like: 'dk kd kk dk dd kd dk ...'
              "dk - triples",  # like: 'dkd kdd kdk kkk dkk ....'
              "dkfj - doubles",  # like: 'jd kf fj dj kk fd ....'
              "dkfj - triples",  # like: 'dkj fdk fdj kjk dkd ..'
              "dkfj - quartet",  # like: 'dkjf fjfk djkd kkjd ..'
              "exit"]

# example of common double_lesson:

def doubles_lesson(letters):
    text = ''
    for i in range(15):
        text = text + choice(letters) + choice(letters) + ' '
    return text
