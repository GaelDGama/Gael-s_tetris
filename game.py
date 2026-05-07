# Example file showing a basic pygame "game loop"
from pathlib import Path
import pygame
import sys
import charcater as ch
import random

pygame.font.init()
class tetris:
    def __init__(self):
        pygame.init()
        self.start = True
        self.screen =pygame.display.set_mode((1200, 800))
        self.background = (230, 0, 0)
        self.playing_area = pygame.Surface((501, 700))
        self.clock = pygame.time.Clock()
        self.blocks = []
        self.spawn = [self.playing_area.get_width()/2 - 50, 50]
        self.y_position_list = []


    def run_game(self):
        score = '0'
        front  = Path(Path.cwd()/'Assets'/'static'/'Inter_18pt-Black.ttf')
        d_x = self.playing_area.get_width()//5
        
        while True:
            
            
            self.playing_area.fill((0,0,230))
            self.screen.fill(self.background)
            sys_font = pygame.font.Font(front, size=18)
            
           

            for thing in self.blocks:
                pygame.draw.rect(self.playing_area, (0,230,0), thing)
                
                
            
            
            cur = ch.block1(self.playing_area, self.spawn)
            
            cur.draw()
            
        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                        
                    if event.key == pygame.K_r:
                        cur.position[0] *= -1
                        cur.position[1] *= -1
                    
                    if event.key == pygame.K_a and 0 < cur.position[0] - d_x:
                        cur.position[0] -= d_x
                    
                            

                    if event.key == pygame.K_d and cur.position[0] + d_x < 499:
                        cur.position[0] += d_x
                        
                        
                    if event.key == pygame.K_SPACE:            
                        cur.position[1] = self.playing_area.get_height() - 50
                        rectangles = pygame.Rect(cur.x_position(), cur.y_position(), cur.width(), cur.height())
                        print('New iteration')
                    
                        for R in self.blocks:
                            
                            if min(max(round((cur.x_position()), 0),0), 400) == round(R.x, 0):
                                cur.position[1] -= 50
                                
                        
                        rectangles = pygame.Rect(cur.x_position(), cur.y_position(), cur.width(), cur.height())
                        print(f"rectangle y = {rectangles.y}")
                        self.y_position_list.append(rectangles.y)
                        print(f"y position list: {self.y_position_list}")
                        self.blocks.append(rectangles)
                        print(f'block list: {self.blocks}')

                        for y in set(self.y_position_list):
                            if self.y_position_list.count(y) >= 5:
                                while y in self.y_position_list:
                                    del self.blocks[self.y_position_list.index(y)]
                                    self.y_position_list.remove(y)
                            
                                for R in self.blocks:
                                    R.y += 50
                                
                                for i in range(len(self.y_position_list)):
                                    self.y_position_list[i] += 50
                                
                                c_score = int(score[:])

                                c_score += 10

                                score = str(c_score)
                                
                                
                        
                        
                        
                                
                        print(f'done  {self.blocks}')       

                        cur.position[1] = 50
                        
            
            
            self.playing_area.blit(sys_font.render(score, True, (0,0,0)), (self.playing_area.get_width()/2, 10))
            self.screen.blit(self.playing_area, (400,50))
            pygame.display.flip()
            
            
            
            
        pygame.quit()
            



if __name__ == '__main__':
    ts = tetris()
    ts.run_game()

