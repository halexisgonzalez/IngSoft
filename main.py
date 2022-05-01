
# For generating random height of pipes
import random
import sys
import pygame
from pygame.locals import *

# Global Variables for the game
window_width = 600
window_height = 499

# set height and width of window
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}
framepersecond = 32
pipeimage = 'img/pipe.png'
background_image = 'img/background.jpg'
birdplayer_image = '/img/bird.png'
sealevel_image = '/img/base.jfif'
