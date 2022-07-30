from random import choice


def generate():
    text = ''
    for i in range(15):
        text = text + choice('fjdksl') + choice('fjdksl') + choice('fjdksl') \
               + choice('fjdksl') + ' '
    return text
