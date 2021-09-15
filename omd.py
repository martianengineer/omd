#!/usr/bin/env python3

import textwrap


def step1():
    print('Утка-маляр 🦆 решила выпить зайти в бар. ' 'Взять ей зонтик? ☂️')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """ This function describes the case with umbrella. """

    print('Взяла и ушла. Когда она шла мимо дома - ее сбил грузовик.')


def step2_no_umbrella():
    """ This function describes the case without umbrella. """

    text = ('Как только она вышла начался дождь. Она увидела, что к ней '
            'двигается огромный грузовик. Водитель грузовика увидел утку и '
            'остановился. Он вышел из машины и пригласил её на кофе. Утка '
            'нарисовала его портрет акварелью. На следующий день утка '
            'получила комплимент от водителя: «Вы нарисовали мой портрет '
            'лучше, чем любой художник в городе!»')
    print(textwrap.fill(text=text, width=30))


if __name__ == '__main__':
    step1()
