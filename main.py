import pygame
import sys
import time
from game_window_class import *
from button_class import *


WIDTH, HEIGHT = 800, 800
BACKGROUND = (199,199,199)
FPS = 60


 # ----------------------------setting functions --------------------------->

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    if button.mouse_hovering(mouse_pos):
                        button.click()
                    else:
                        pass

def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)

def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()
    for c in counter:
        c.draw()

    # ----------------------------running functions --------------------------->

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    if button.mouse_hovering(mouse_pos):
                        button.click()
                    else:
                        pass

def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)
    game_window.evaluate()

def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()
    for c in counter:
        c.draw()

 # ----------------------------paused functions --------------------------->

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    if button.mouse_hovering(mouse_pos):
                        button.click()
                    else:
                        pass

def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)

def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()
    for c in counter:
        c.draw()

#-------------------------------------------------------------------------->


def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < WIDTH-100:
        if pos[1] > 100 and pos[1] < HEIGHT-20:
            return True
    return False 

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True

def make_buttons():
    buttons = []
    buttons.append(Button(window,WIDTH//5-50,50,100,30,text='RUN',color=(28,111,51),hover_color=(48,131,81),bg_color=(5,5,5),function=run_game))
    buttons.append(Button(window,WIDTH//2-50,50,100,30,text='PAUSE',color=(18,104,135),hover_color=(51,168,212),bg_color=(5,5,5),function=pause_game))
    buttons.append(Button(window,WIDTH//1.2-50,50,100,30,text='RESET',color=(117,14,14),hover_color=(48,131,81),bg_color=(5,5,5),function=reset_grid))
    return buttons

def make_counter(gen):
    counter = []
    counter.append(Button(window,WIDTH//2-50,100,100,30,text='gen: '+str(gen),color=(18,104,135),hover_color=(51,168,212),bg_color=(5,5,5)))
    return counter

def run_game():
    global state
    state = 'running'

def pause_game():
    global state
    state = 'paused'

def reset_grid():
     global state
     state = 'setting'
     game_window.reset_grid()


gen = 0
pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window,100,180)
buttons = make_buttons()
running = True
state = 'setting'
print(len(buttons))
counter = make_counter(gen)



while running:
    mouse_pos = pygame.mouse.get_pos()
    pygame.display.update()
    if state == 'setting':
        gen = 0
        counter = make_counter(gen)
        get_events()
        update()
        draw()
    if state == 'running':
        time.sleep(0.1)
        gen += 1
        counter = make_counter(gen)
        running_get_events()
        running_update()
        running_draw()
        if game_window.evaluate() == 'stop':
            state = 'paused'
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
    print(state)
sys.exit()