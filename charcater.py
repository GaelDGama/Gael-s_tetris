import pygame
import random

class block1():
    def __init__(self, playing_area, position):
        self.area = playing_area
        self.color = (0,230,0)
        self.position = position
        self.size = [self.position[0], self.position[1], 100,50]
        self.down =False

    def draw(self):
        return pygame.draw.rect(self.area, self.color, self.size)
    
    def x_position(self):
        return self.position[0]
    
    def y_position(self):
        return self.position[1]
    
    def width(self):
        return self.size[2]
    
    def height(self):
        return self.size[3]

class block2():
    def __init__(self, playing_area, position):
        self.area = playing_area
        self.color = (0,230,0)
        self.position = position
        self.size = [self.position[0], self.position[1], 50, 50]
    
    def draw(self):
        return pygame.draw.rect(self.area, self.color, self.size)
    
    

    
        
        
