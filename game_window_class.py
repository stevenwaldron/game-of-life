import pygame
import copy
import time
from cell_class import *
vec = pygame.math.Vector2


class Game_window:
    def __init__(self,screen, x, y):
        self.screen = screen
        self.pos = vec(x,y)
        self.width, self.height = 600,600
        self.image = pygame.Surface((self.width,self.height))
        self.rect = self.image.get_rect()
        self.rows = 30
        self.cols = 30
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]
        for row in self.grid:
            for cell in row:
                cell.get_neighbors(self.grid)
    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.image.fill((102,102,102))
        for row in self.grid:
                for cell in row:
                     cell.drawing()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def reset_grid(self):
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)] for y in range(self.rows)]

   
    
    def evaluate(self):
        class Que:
            def __init__(self,storage = []):
                self.storage = storage 

            def eque(self,value):
                self.storage.append(value)

            def deque(self):
                return self.storage.pop(0)

        Q = Que()
        last_grid = self.grid
        time.sleep(0.1)
        new_grid = copy.copy(self.grid)
        

        for row in self.grid:
            for cell in row:
                cell.live_neighbors()
        for yidx, row in enumerate(self.grid):
            for xidx, cell in enumerate(row):
                if cell.alive:
                    if cell.alive_neighbors == 2 or cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True 
                    if cell.alive_neighbors < 2:
                            new_grid[yidx][xidx].alive = False
                    if cell.alive_neighbors > 3:
                            new_grid[yidx][xidx].alive = False
                elif cell.alive_neighbors == 3:
                        new_grid[yidx][xidx].alive = True 
                
        
        
        Q.eque(new_grid)
        

        # if last_grid == Q.deque():
        #         return 'stop'
        self.grid = Q.deque()   
            
                 

    
        #         for neighbor in cell.neighbors:
        #             if neighbor.alive:
        #                 cell.alive_neighbors += 1
        # new_grid = [[Cell(self.image,x,y) for x in range(self.cols)] for y in range(self.rows)]
        # for yidx, row in enumerate(self.grid):
        #     for xidx, cell in enumerate(row):
        #         if cell.alive_neighbors < 2 and cell.alive:
        #             new_grid[yidx][xidx].alive = False
        #         if cell.alive_neighbors > 3 and cell.alive:
        #             new_grid[yidx][xidx].alive = False
        #         if cell.alive_neighbors == 2 or cell.alive_neighbors == 3 and cell.alive:
        #             new_grid[yidx][xidx].alive = True
        #         if cell.alive_neighbors == 3 and not cell.alive:
        #             new_grid[yidx][xidx].alive = True
        # self.grid = new_grid



