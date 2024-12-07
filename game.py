from settings import *

class Game:
    def __init__(self):

        # general
        self.surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT)) # creating game area to put on left side of screen
        self.display_surface = pygame.display.get_surface() # returns main window from main.py
        # ^ you can use this method to get the display surface anywhere in the code

    # We want to place the game area "surface" onto the main window "display surface"

    def run(self):
        # blit = "block image transfer", put one surface on another surface
        # arguments are surface you want to place, and position
        self.display_surface.blit(self.surface, (PADDING,PADDING))