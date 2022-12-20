# Imports go at the top
from microbit import *
import music

# Code in a 'while True:' loop repeats forever
music.set_tempo(bpm=80*8)
f20es = [
    'E4:4','E4','E4','E4',
    'E4','E4','E4','E4',
    'E4','E4','E4','E4',
    'E4','E4','E4','E4'
    'E4','E4','E4','E4'
]
ddE = [
    'E4','F4','E4','D#4','E4','','A5','','C6:16'
]
goingDown = [
    'D6:4','D6','D6','D6','D6','C6','B5','D6'
]
goingDownC = [
    'C6','C6','C6','C6','C6','B5','A5','C6'
]
goingDownB = [
    'B5','B5','B5','B5','F#5','','B5','','G#5','','','','E4:16'
]
while True:
    music.play(f20es + ddE + goingDown + goingDownC + goingDownB)
