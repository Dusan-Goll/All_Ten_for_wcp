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
import time
from msvcrt import getch
from colorama import Fore, Back, Style, init, deinit

line_length = 71
SEP = '-' * line_length
lessons_folder = "lessons_database"
txt_files = os.listdir(lessons_folder)


def main():
    """Welcome the user, activate colors, display menu and let the user choose
    (run lesson or quit), deactivate colors and quit."""
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
    """return lesson text with actual position to display"""
    return 'For exit press "esc" button.\n' + SEP + '\n' \
           + _text_[:index] + yellowed(character) + _text_[index + 1:]\
           + '\n' + SEP + '\n' + _text_[:index] + reded(_typo_)


def message():
    """return final message and mistakes count"""
    return Back.GREEN + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Got it!' \
        + Style.RESET_ALL


def reded(wrong_typo):
    """color wrong typo to red"""
    return Back.RED + Style.BRIGHT + wrong_typo + Style.RESET_ALL


def yellowed(_char_):
    """color actual letter background to yellow"""
    return Back.YELLOW + Style.BRIGHT + _char_ + Style.RESET_ALL


def run_lesson(text_list):
    """display text for typing, wait for user's typo and handle it"""
    first_hit = True
    typos_count, speed, speed_sum, missed, missed_total = 0, 0, 0, 0, 0
    for line in text_list:
        line = line.replace('\n', '')
        for ix, char in enumerate(line):
            typo = ''
            while typo != char:  # print text and wait for correct typo
                os.system('cls')
                print('actual speed:', speed, '   missed:', missed + missed_total)
                print(screen(ix, char, line, typo))
                typo_raw = getch()
                typos_count += 1
                #
                if first_hit:
                    start_time = begin = time.time()  # start counting
                    first_hit = False
                elif time.time() - start_time >= 60:  # stop after 1 minute
                    speed = typos_count - missed  # actual speed in secs
                    missed_total += missed
                    speed_sum += speed
                    typos_count, missed = 0, 0  # reset typos_count and mistakes
                    start_time = time.time()  # reset time counting
                #
                typo = typo_raw.decode("utf-8")
                if typo == '\x1b':  # ESC button immediately quits the lesson
                    return
                if typo != char:
                    missed += 1
    speed_sum += typos_count - missed  # add part of last minute
    missed_total += missed
    total_time = round(((time.time() - begin) / 60), 1)
    total_speed = round(speed_sum / total_time, 0)
    os.system('cls')
    print(SEP)
    print(message())
    print(f'You have missed {missed_total}-times.')
    print(f'your typing speed: {total_speed} hits per minute')
    print(f'total time: {total_time} min\n')
    input('Press Enter to continue...\n> ')


def options_dict(lessons_list):
    """return dictionary of menu options"""
    first_parts = [file[:9] for file in lessons_list]
    second_parts = [file[9:].split('.')[0].lstrip('_') for file in lessons_list]
    lesson_names = [f'{a} ({b})' for a, b in zip(first_parts, second_parts)]
    lessons_dict = {str(i + 1): name for i, name in zip(range(len(lesson_names)), lesson_names)}
    menu_dict = {'0': 'QUIT program'}
    menu_dict.update(lessons_dict)
    return menu_dict


def display_menu(lessons):
    """display menu options from dictionary"""
    os.system('cls')
    print('MENU:')
    for key in options_dict(lessons):
        print(key.rjust(2), ' -> ', options_dict(lessons)[key])


def user_option(lessons_list):
    """return user's correct choice from menu options"""
    choice = ''
    choices = [str(x) for x in range(len(lessons_list) + 1)]
    while choice not in choices:
        display_menu(lessons_list)
        choice = input('\nPlease select option (write number)'
                       ' and press Enter:\n> ')
    return choice


if __name__ == '__main__':
    main()
