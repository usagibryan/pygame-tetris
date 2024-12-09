# see "Build Tetris with Pygame #5 - Moving the Shapes Down" @ https://youtu.be/VjvH8CwBjFA?si=ObVeyCdULD359PoA
# this class can be used as a timer in other Pygame games?

import pygame
from pygame.time import get_ticks

class Timer:
    def __init__(self, duration, repeated = False, func = None):
        self.repeated = repeated
        self.func = func
        self.duration = duration

        self.start_time = 0
        self.active = False

    # only called once
    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks() # gets time that has elapsed since pygame.init() was called

    def deactivate(self):
        self.active = False
        self.start_time = 0

    # call on every frame of the game
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration and self.active:
            
            # call a function
            if self.func and self.start_time != 0:
                self.func() # will only run if there is a function once timer runs out

            # reset timer
            self.deactivate()

            # repeat the timer
            if self.repeated:
                self.activate()