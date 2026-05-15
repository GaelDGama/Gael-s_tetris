import pygame
import random

class onebyone():
    def __init__(self, playing_area, position):
        self.area = playing_area
        self.color = (0,230,0)
        self.position = position
        self.size = [self.position[0], self.position[1], 50,50]
        self.down =False
        self.d_x = playing_area.get_width() // 10
        self.onebyone = [self.size]

    def draw(self):
        pygame.draw.rect(self.area, self.color, self.size)
    
    def x_position(self):
        return [self.position[0]]
    
    def y_position(self):
        return [self.position[1]]
    
    def width(self):
        return [self.size[2]]
    
    def height(self):
        return [self.size[3]]
    
    def get_right(self):
        x = []
        for i in self.onebyone:
            x.append(i[0])
        
        return max(x)


class fourbyfour(onebyone):
    def __init__(self, playing_area, position):
        super().__init__(playing_area, position)
        self.size1 = [self.position[0] +50, self.position[1], 50,50]
        self.size2 = [self.position[0], self.position[1] - 50, 50,50]
        self.size3 = [self.position[0] + 50, self.position[1] - 50, 50,50]
        self.onebyone = [self.size, self.size1, self.size2, self.size3]

    def draw(self):
        drawings = [self.size, self.size1, self.size2, self.size3]
        for size in drawings:
            pygame.draw.rect(self.area, self.color, size)
    
    def x_position(self):
        return [self.size[0], self.size1[0], self.size2[0], self.size3[0]]
    
    def y_position(self):
        return [self.size[1], self.size1[1], self.size2[1], self.size3[1]]
    
    def width(self):
        return [self.size[2], self.size1[2], self.size2[2], self.size3[2]]

    def height(self):
        return [self.size[3], self.size1[3], self.size2[3], self.size3[3]]

    
    

    
        
        
