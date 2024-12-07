from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING)) # create score window in sidebar
        self.display_surface = pygame.display.get_surface() # returns main window from main.py

    def run(self):
        self.display_surface.blit(self.surface,(0,0)) # place score window on main window