from settings import *

class Preview:
    def __init__(self):
        # look at these next two lines again, compare to score.py, and understand why the math works
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING, PADDING))
        self.display_surface = pygame.display.get_surface() # return main window from main.py

    def run(self):
        self.display_surface.blit(self.surface,self.rect)