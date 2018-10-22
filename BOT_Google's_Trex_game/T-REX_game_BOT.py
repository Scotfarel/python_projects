from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    replay_button = (480, 410)
    dino = (222, 413)


def restart_game():
    pyautogui.click(Cordinates.replay_button)


def jump():
    pyautogui.keyDown('space', 0.1)
    pyautogui.keyUp('space')


def image_grab():
    box = (Cordinates.dino[0] + 78, Cordinates.dino[1],
           Cordinates.dino[0] + 128, Cordinates.dino[1] + 25)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = array(gray_image.getcolors())
    return a.sum()



restart_game()
while True:
    if image_grab() != 1497:
        jump()
time.sleep(0.01)
