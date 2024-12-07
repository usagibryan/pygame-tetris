from settings import * # import pygame from settings.py
from sys import exit # import module to close game

# components
from game import Game # import Game class from game.py
from score import Score # import Score class from score.py

class Main: # define main class
    def __init__(self):

        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # create display surface
        self.clock = pygame.time.Clock() # create clock to work with time in Pygame
        pygame.display.set_caption('Tetris') # create window title

        # components
        self.game = Game() # create instance of game class
        self.score = Score() # create instance of Score class
    
    def run(self): # method that runs perpetually
        while True: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if X button on window is clicked
                    pygame.quit() # closes pygame
                    exit() # terminates any running script

            # display
            self.display_surface.fill(GRAY) # background color

            # components
            self.game.run() # run the instance of the game class
            self.score.run() # run the instance of the score class
            
            # updating the game
            pygame.display.update() # "updates whatever we are doing in the game so we can see things"
            self.clock.tick() # object that helps control framerate. Pass values to define framerate or leave blank to run as fast as possible

if __name__ == '__main__': # make sure only main.py is run when code is executed
    main = Main() # create instance of main class
    main.run() # run main class