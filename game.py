from settings import *

class Game:
    def __init__(self):

        # general
        self.surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT)) # creating game area to put on left side of screen
        self.display_surface = pygame.display.get_surface() # returns main window from main.py
        # ^ you can use this method to get the display surface anywhere in the code
        
        # create rect for grid border
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        # lines
        self.line_surface = self.surface.copy() # create copy of original surface to draw lines on
        self.line_surface.fill((0,255,0)) # fill with pure green color we will never use
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(120) # make lines transparent
        # ^ to understand the logic here see: https://youtu.be/-vJg_k7XqhE?si=tplxWNfxzA_pvrSi&t=456

    def draw_grid(self):

        # draw vertical lines in a grid
        for col in range(1, COLUMNS): # start at 1 instead of zero to get rid of the leading line
            x = col * CELL_SIZE # increase start_pos by cell size each time
            # 5 arguments; surface, color, start_pos, end_pos, width
            pygame.draw.line(self.line_surface, LINE_COLOR, (x,0), (x, self.surface.get_height()), 1) 

        # draw horizontal lines in a grid
        for row in range (1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (0,y), (self.surface.get_width(), y))

        # draw the new line surface onto the original game surface
        self.surface.blit(self.line_surface, (0,0))

    def run(self):

        # drawing
        self.surface.fill(GRAY)

        self.draw_grid()

        # We want to place the game area "surface" onto the main window "display surface"
        # blit = "block image transfer", put one surface on another surface
        # arguments are surface you want to place, and position
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        
        # 5 arguments; surface, color, rect, width, corner radius
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2) # draw border around grid