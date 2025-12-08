"""
Author: Prof. Alyssa
Stores values for constant variables.
This is good practice to avoid "magic numbers"

Assignment adapted from HMC CS60

TODO Update this program header
"""

import pygame

class Preferences:
    pygame.init()

    ##########
    # Timing #
    ##########

    # How frequently to move the snake
    REFRESH_RATE = 2
    # How frequently to add food to the board
    FOOD_ADD_RATE = 25    
    # How long to sleep between updates
    SLEEP_TIME = 30

    ##########
    # Sizing #
    ##########

    # Dimensions of the board
    NUM_CELLS_WIDE = 50
    NUM_CELLS_TALL = 30 

    # Size of each cell in pixels
    CELL_SIZE = 30

    # Dimensions of the board in pixels
    GAME_BOARD_WIDTH = NUM_CELLS_WIDE * CELL_SIZE
    GAME_BOARD_HEIGHT = NUM_CELLS_TALL * CELL_SIZE

    ##########
    # Colors #
    ##########

    COLOR_BACKGROUND = pygame.Color('lavender')
    COLOR_WALL = pygame.Color('gray40')
    COLOR_FOOD = pygame.Color('firebrick')
    COLOR_EMPTY = pygame.Color('lavender')
    COLOR_HEAD = pygame.Color('darkorchid4')
    COLOR_BODY = pygame.Color('darkorchid1')

    ##########################
    # Game over text display #
    ##########################
    
    GAME_OVER_X = GAME_BOARD_HEIGHT / 2
    GAME_OVER_Y = GAME_BOARD_WIDTH / 2
    GAME_OVER_COLOR = pygame.Color('navy')
    GAME_OVER_FONT = pygame.font.SysFont("arial", 120)
    GAME_OVER_TEXT = "Game Over"

    ######################
    # Graphics and Audio #
    ######################

    # Image to display as the head
    HEAD_IMAGE = "trainer.png"
    # Sound to play when eating
    EAT_SOUND = "meow.wav"
        ###############################
    # Custom Feature Add-Ons      #
    ###############################

    # Traversal highlight colors
    COLOR_TRAVERSAL = pygame.Color("gold")
    COLOR_TRAVERSAL_SECOND = pygame.Color("yellow")

    # Priority fruit colors (heap-like priorities)
    COLOR_FRUIT_PRIORITY_HIGH = pygame.Color("red3")
    COLOR_FRUIT_PRIORITY_MED = pygame.Color("orange3")
    COLOR_FRUIT_PRIORITY_LOW = pygame.Color("yellow3")

    # Balancing / rotation visual effect
    ROTATION_SHAKE_AMOUNT = 40      # pixels to shift when unbalanced
    ROTATION_EDGE_THRESHOLD = 0.0 # fraction of board away from center

    # Keys for custom modes
    KEY_TRAVERSAL_MODE = pygame.K_t
    KEY_BALANCE_MODE = pygame.K_b
