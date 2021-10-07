# TOCANDO UMA MÚSICA

from pygame import mixer, init, time, event
from os import path

init()
if path.exists('vmz.mp3'):
    mixer.music.load('vmz.mp3')
    mixer.music.play()
    mixer.music.set_volume(1)

    clock = time.Clock()
    clock.tick(10)

    while mixer.music.get_busy():
        event.poll()
        clock.tick(10)
    else:
        print('Arquivo não encontrado! Por favor, coloque-o na mesma pasta dos exercícios e tente novamente.')