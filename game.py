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
        self.rotation = 2


    def run_game(self):
        score = '0'
        front  = Path(Path.cwd()/'Assets'/'static'/'Inter_18pt-Black.ttf')
              
        while True:
            
            
            self.playing_area.fill((0,0,230))
            self.screen.fill(self.background)
            sys_font = pygame.font.Font(front, size=18)
            
           

            for thing in self.blocks:
                pygame.draw.rect(self.playing_area, (0,230,0), thing)
                
                
            
            
            cur = ch.fourbyfour(self.playing_area, self.spawn)

            if self.rotation % 2 == 1:
                width_c = str(cur.width())
                length_c = str(cur.height())

                cur.size[2] = int(length_c)
                cur.size[3] = int(width_c)
                 
            
            cur.draw()
            
        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                if event.type == pygame.KEYDOWN:
                        
                    if event.key == pygame.K_r:
                        if self.rotation % 2 == 0:
                            self.rotation = 3
                        else:
                            self.rotation = 2

                    
                    if event.key == pygame.K_a and 0 < cur.position[0] - cur.d_x:
                        cur.position[0] -= cur.d_x
                    
                            

                    if event.key == pygame.K_d and cur.position[0] + cur.d_x < 500:
                        cur.position[0] += cur.d_x
                        
                        
                    if event.key == pygame.K_SPACE:
                        for block in cur.onebyone:
                            block[1] += 600
                        
                        print('New iteration')
                        
                        
                        for r in self.blocks:
                            for i in cur.onebyone:
                                if min(max(round((i[0]), 0),0), 400) == round(r.x, 0):
                                    i[1] -= 50
                            
                           
                                
                        for block in cur.onebyone:
                            rectangle = pygame.Rect(block[0], block[1], block[2], block[3])
                            
                            self.y_position_list.append(rectangle.y)
                            self.blocks.append(rectangle)
                        
                       
                        for y in set(self.y_position_list):
                            if self.y_position_list.count(y) > 9:
                                while y in self.y_position_list:
                                    del self.blocks[self.y_position_list.index(y)]
                                    self.y_position_list.remove(y)
                                    
                                c_score = int(score[:])

                                c_score += 10

                                score = str(c_score)
                                
                            # for r in self.blocks:
                            #     if min(self.y_position_list) >= r.y and r.y <= 0:
                            #         R.y += 50
                                
                            # for i in range(len(self.y_position_list)):
                            #     if min(self.y_position_list) >= i and i <= 0:
                            #         self.y_position_list[i] += 50
                                
                        

                                
                        
                        print(self.y_position_list)
                                
                        
                        
                        
                                
                        

                        cur.position[1] = 50
                        
            
            self.playing_area.blit(sys_font.render(score, True, (0,0,0)), (self.playing_area.get_width()/2, 10))
            self.screen.blit(self.playing_area, (400,50))
            pygame.display.flip()
            
            
            
            
        pygame.quit()
            



if __name__ == '__main__':
    ts = tetris()
    ts.run_game()

