from settings import *

class Score:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * SCORE_HEIGHT_FRACTION - PADDING)) # create score window in sidebar
        self.rect = self.surface.get_rect(bottomright = (WINDOW_WIDTH - PADDING, WINDOW_HEIGHT - PADDING)) # create rectangle and put score window inside it from the bottom right
        # ^ not sure I understand the logic here. See https://youtu.be/YftAXFNc_ZU?si=knBQoEzSAqN3Y9NF&t=777
        self.display_surface = pygame.display.get_surface() # return main window from main.py

    def run(self):
        self.display_surface.blit(self.surface,self.rect) # place score window on main window at rectangle location (bottom right)