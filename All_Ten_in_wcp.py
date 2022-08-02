"""All_Ten_in_wcp
- simple program to learn and practise to write with all ten fingers
  in command-prompt (for Windows)
- by Dušan Goll"""

# TODO: / create while loop for main menu
#       / generator.py: create a database of lessons (automatically generated texts)
#       / add speed of typing
#       / add final stats after completing the lesson
#       / text wrapping
#       / add display with actual speed and count of miss-typos
#       / possibility of backspace requirement

import os
from msvcrt import getch
from colorama import Fore, Back, Style, init, deinit
import trial_generator


text = trial_generator.generate()  # here will be generator.base_menu() instead
line_length = 49
separ = '-' * line_length


def main():
    print("""
--------------- All_Ten_in_wcp -----------------
Welcome, this is simple program to learn
and practice typing by All-ten fingers.
------------------------------------------------
Press Enter to start.
""")
    input(">")
    init()
    missed = 0
    for ix, char in enumerate(text):
        typo = ''
        while typo != char:
            os.system('cls')
            print(screen(ix, char, text, typo))
            typo_raw = getch()
            typo = typo_raw.decode("utf-8")
            if typo == '\x1b':  # ESC button
                print('You have quited the program.')
                quit()
            if typo != char:
                missed += 1
    os.system('cls')
    print(separ, text, separ, text, separ, sep='\n')
    print(message(missed))
    deinit()


def screen(index, character, _text_, _typo_):
    return 'For exit press "esc" button.\n' + separ + '\n' \
           + _text_[:index] + yellowed(character) + _text_[index + 1:]\
           + '\n' + separ + '\n' + _text_[:index] + reded(_typo_)


def message(mistakes):
    return Back.GREEN + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Got it!' \
           + Style.RESET_ALL + f'\nYou have missed {mistakes}-times.'


def reded(wrong_typo):
    return Back.RED + Style.BRIGHT + wrong_typo + Style.RESET_ALL


def yellowed(_char_):
    return Back.YELLOW + Style.BRIGHT + _char_ + Style.RESET_ALL


if __name__ == '__main__':
    main()
