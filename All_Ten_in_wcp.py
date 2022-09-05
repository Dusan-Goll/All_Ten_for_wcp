"""All_Ten_in_wcp, by Dušan Goll
- simple program to learn and practise to write with all ten fingers
  in command-prompt (for Windows)
"""

# TODO: / add speed of typing
#       / add final stats after completing the lesson
#       / add display with actual speed and count of miss-typos
#       / possibility of backspace requirement (big task)
#       / add docstrings to functions

import os
from msvcrt import getch
from colorama import Fore, Back, Style, init, deinit

line_length = 71
SEP = '-' * line_length
lessons_folder = "lessons_database"
txt_files = os.listdir(lessons_folder)


def main():
    os.system('cls')
    print("""
Dušan Goll presents:

--------------- All_Ten_in_wcp -----------------
Welcome, this is program to practice 
typing by All-ten fingers.
------------------------------------------------
Press Enter to start.
""")
    input(">")
    init()  # activate colors
    while True:
        option = user_option(txt_files)
        if option == '0':
            deinit()  # deactivate colors
            os.system('cls')
            print('Thanks for using this program, bye.')
            quit()
        else:
            lesson_file = open(f"lessons_database\\"
                               f"{txt_files[int(option) - 1]}", mode="r")
            lesson = lesson_file.readlines()
            lesson_file.close()

            run_lesson(lesson)


def screen(index, character, _text_, _typo_):
    return 'For exit press "esc" button.\n' + SEP + '\n' \
           + _text_[:index] + yellowed(character) + _text_[index + 1:]\
           + '\n' + SEP + '\n' + _text_[:index] + reded(_typo_)


def message(mistakes):
    return Back.GREEN + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Got it!' \
           + Style.RESET_ALL + f'\nYou have missed {mistakes}-times.'


def reded(wrong_typo):
    return Back.RED + Style.BRIGHT + wrong_typo + Style.RESET_ALL


def yellowed(_char_):
    return Back.YELLOW + Style.BRIGHT + _char_ + Style.RESET_ALL


def run_lesson(text_list):
    missed = 0
    for line in text_list:
        line = line.replace('\n', '')
        for ix, char in enumerate(line):
            typo = ''
            while typo != char:  # print text and wait for correct typo
                os.system('cls')
                print(screen(ix, char, line, typo))
                typo_raw = getch()
                typo = typo_raw.decode("utf-8")
                if typo == '\x1b':  # ESC button immediately quits the lesson
                    return
                if typo != char:
                    missed += 1
    os.system('cls')
    print(SEP)
    print(message(missed), '\n')
    input('Press Enter to continue...\n> ')


def options_dict(lessons_list):
    first_parts = [file[:9] for file in lessons_list]
    second_parts = [file[9:].split('.')[0].lstrip('_') for file in lessons_list]
    lesson_names = [f'{a} ({b})' for a, b in zip(first_parts, second_parts)]
    lessons_dict = {str(i + 1): name for i, name in zip(range(len(lesson_names)), lesson_names)}
    menu_dict = {'0': 'QUIT program'}
    menu_dict.update(lessons_dict)
    return menu_dict


def display_menu(lessons):
    os.system('cls')
    print('MENU:')
    for key in options_dict(lessons):
        print(key.rjust(2), ' -> ', options_dict(lessons)[key])


def user_option(lessons_list):
    choice = ''
    choices = [str(x) for x in range(len(lessons_list) + 1)]
    while choice not in choices:
        display_menu(lessons_list)
        choice = input('Please select option (write number)'
                       ' and press Enter:\n> ')
    return choice


if __name__ == '__main__':
    main()
