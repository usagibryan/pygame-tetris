from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING)) # create score window and define size
        # create rectangle and attach at the bottom right of the window from it's bottom right corner
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING))
        self.display_surface = pygame.display.get_surface() # return main window from main.py

    def run(self):
        self.display_surface.blit(self.surface,self.rect) # place score window on main window at rectangle location