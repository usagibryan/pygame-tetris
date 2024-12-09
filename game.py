from settings import *
from random import choice

from timer import Timer

class Game:
    def __init__(self):

        # general
        self.surface = pygame.Surface((GAME_WIDTH,GAME_HEIGHT)) # creating game area to put on left side of screen
        self.display_surface = pygame.display.get_surface() # returns main window from main.py
        # ^ you can use this method to get the display surface anywhere in the code
        
        # create rect for grid border
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        self.sprites = pygame.sprite.Group() # create group for sprites

        # lines
        self.line_surface = self.surface.copy() # create copy of original surface to draw lines on
        self.line_surface.fill((0,255,0)) # fill with pure green color we will never use
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(60) # lower values make lines more transparent
        # ^ to understand the logic here see: https://youtu.be/-vJg_k7XqhE?si=tplxWNfxzA_pvrSi&t=456

        # tetrominos
        self.tetromino = Tetromino(choice(list(TETROMINOS.keys())), self.sprites)

        # timer
        self.timers = {
            'vertical move': Timer(UPDATE_START_SPEED, True, self.move_down),
            'horizontal move': Timer(MOVE_WAIT_TIME)
        }
        self.timers['vertical move'].activate()

    def timer_update(self):
        for timer in self.timers.values():
            timer.update()

    def move_down(self):
        self.tetromino.move_down()

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

    def input(self):
        keys = pygame.key.get_pressed()
        # use timer to prevent moving piece too fast from user input
        if not self.timers['horizontal move'].active: # check if timer is not active, then allow
            if keys[pygame.K_LEFT]:
                self.tetromino.move_horizontal(-1)
                self.timers['horizontal move'].activate() # start timer again
            if keys[pygame.K_RIGHT]:
                self.tetromino.move_horizontal(1)
                self.timers['horizontal move'].activate()

    def run(self):

        # update
        self.input()
        self.timer_update()
        self.sprites.update()

        # drawing
        self.surface.fill(GRAY)
        self.sprites.draw(self.surface) # draw the sprites on the surface

        self.draw_grid()

        # We want to place the game area "surface" onto the main window "display surface"
        # blit = "block image transfer", put one surface on another surface
        # arguments are surface you want to place, and position
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        
        # 5 arguments; surface, color, rect, width, corner radius
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2) # draw border around grid

class Tetromino:
    def __init__(self, shape, group):
        
        # setup using shapes dictionary from settings.py
        self.block_positions = TETROMINOS[shape]['shape']
        self.color =TETROMINOS[shape]['color']

        # create blocks
        # use "list comprehension" to store in a list in an attribute (Video 4, 13 minutes in)
        # create one instance of the block class for every position in the list
        self.blocks = [Block(group, pos, self.color) for pos in self.block_positions]
        
    def move_horizontal(self, amount):
        for block in self.blocks:
            block.pos.x += amount

    def move_down(self):
        for block in self.blocks:
            block.pos.y += 1

class Block(pygame.sprite.Sprite): # create sprite
    def __init__(self, group, pos, color): # place sprite into group
       
       # general
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE)) # create surface we want to display and make it one cell size
        self.image.fill(color)

        # position
        self.pos = pygame.Vector2(pos) + BLOCK_OFFSET
        self.rect = self.image.get_rect(topleft = self.pos * CELL_SIZE) # create rect to determine where to place it

    def update(self):
        self.rect.topleft = self.pos * CELL_SIZE