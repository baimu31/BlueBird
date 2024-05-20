import pygame

class Timer:
    def __init__(self,duration):
        self.duration =duration
        self.active = False
        self.strat_time = 0

    def activate(self):
        self.active = True
        self.strat_time=pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.strat_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time -self.strat_time >=self.duration:
            self.deactivate()