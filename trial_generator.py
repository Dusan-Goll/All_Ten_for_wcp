from random import choice


def generate():
    text = ''
    for i in range(15):
        text = text + choice('fjdksl') + choice('fjghsl') + choice("dk';gh") \
               + choice('dk":gh') + ' '
    return text
