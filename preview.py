from settings import *

class Preview:
    def __init__(self):
        self.surface = pygame.Surface((SIDEBAR_WIDTH,GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION)) # create preview window and define size
        # create rectangle and attach at the top right of the window from it's top right corner
        self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING, PADDING))
        self.display_surface = pygame.display.get_surface() # return main window from main.py

    def run(self):
        self.display_surface.blit(self.surface,self.rect)