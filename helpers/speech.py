#from os import system

from helpers.sub import sub
from helpers.tts import transform


def speak(text):
    f = transform(text)
    sub(['mpg321', f])
    sub(['rm', '-f', f])
