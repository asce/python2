#!/usr/bin/env python
# -*- coding: utf-8 -*-                                                   
import random, os.path
import sys

#import basic pygame modules
import pygame
from pygame.locals import *
from random import randint

if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'


TIME_EVENT = 1
BACKGROUND = 0
SNAKE = 1
FOOD = 2
ENEMY = 3
WALL = 4

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

dirtyrects = [] # list of update_rects                                    
next_tick = 0   # used for timing                                         
class Img: pass # container for images
main_dir = os.path.split(os.path.abspath(__file__))[0]  # Program's diret
def load_image(file, transparent):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' %
                         (file, pygame.get_error()))
    if transparent:
        corner = surface.get_at((0, 0))
        surface.set_colorkey(corner, RLEACCEL)
    return surface.convert()


class Scene:

    def __init__(self,rows,cols,snake_size):
        # Menos intuitiva pero mas eficiente
        self.colision_flag = 0
        self.move = RIGHT
        self.snake_size = snake_size
        self.rows = rows
        self.cols = cols
        self.mat = [BACKGROUND] * rows
        for i in range(rows):
            if(i==0 or i==rows-1):
                self.mat[i] = [WALL] * cols
            else:
                self.mat[i] = [BACKGROUND] * cols
                (self.mat[i][0],self.mat[i][cols-1]) = (WALL,WALL)

                
        col_snake = cols/2 - self.snake_size/2
        row_snake = rows/2
        self.snake_pos = []
        for i in range(self.snake_size):
            if(col_snake > 0 and col_snake < cols-1):
                self.snake_pos.append([row_snake,col_snake])
                self.mat[row_snake][col_snake] = SNAKE
                col_snake+=1
            else:
                self.snake_size-=1
                col_snake+=1
        
        row = randint(0,rows-1)
        col = randint(0,cols-1)
        for i in range(5):
            while(self.mat[row][col]!=BACKGROUND):
                row = randint(0,rows-1) 
                col = randint(0,cols-1)
            self.mat[row][col] = ENEMY
    def show(self):
        for i in range(self.rows):
            print self.mat[i]
    def next(self):
        previous_pos = self.snake_pos[len(self.snake_pos)-1]
        new_pos = previous_pos[:]
        if(self.move == RIGHT):
            new_pos[1] += 1 #La siguiente columna
        elif(self.move == LEFT):
            new_pos[1] -= 1
        elif(self.move == UP):
            new_pos[0] -= 1
        elif(self.move == DOWN):
            new_pos[0] += 1
        last_pos = self.snake_pos[0]
        self.snake_pos = self.snake_pos[1:]
        self.snake_pos.append(new_pos)
        print self.snake_pos
        self.mat[last_pos[0]][last_pos[1]] = BACKGROUND
        if(self.mat[new_pos[0]][new_pos[1]] != BACKGROUND):
            print "colision!"
            self.colision_flag = 1
        self.mat[new_pos[0]][new_pos[1]] = SNAKE

        
        
def main():
    ROWS = 20
    COLS = 25
    CELL_SIZE = 20
    SCREENRECT = Rect(0, 0, COLS*CELL_SIZE, ROWS*CELL_SIZE)
    scenario = Scene(ROWS,COLS,10)
    # Initialize SDL components                                           
    pygame.init()
    screen = pygame.display.set_mode(SCREENRECT.size, 0)
    clock = pygame.time.Clock()

    # Load the Resources                                                  
    Img.background = pygame.transform.scale(load_image('background.jpg', 0),SCREENRECT.size)
    Img.player = pygame.transform.scale(load_image('body1.png', 1),(CELL_SIZE,CELL_SIZE))
    #Img.player = load_image('snake_body.gif', 1)
    #Img.player = load_image('snake_head.gif', 1)
    Img.wall = pygame.transform.scale(load_image('wall.gif', 1),(CELL_SIZE,CELL_SIZE))
    #Img.enemy = load_image('enemy.gif', 1)

    # Create the background                                               

    background = pygame.Surface(SCREENRECT.size)
    
    #for x in range(0, SCREENRECT.width, Img.background.get_width()):
    #    background.blit(Img.background, (x, 0))

    def repaint():
        screen.blit(Img.background,(0,0))    
        for i in range(ROWS):
            for j in range(COLS):
            
                if(scenario.mat[i][j]==SNAKE): elem = Img.player
                if(scenario.mat[i][j]==FOOD): pass
                if(scenario.mat[i][j]==WALL): elem = Img.wall
                if(scenario.mat[i][j]==ENEMY): elem = Img.wall
                if(scenario.mat[i][j]!=BACKGROUND):
                    screen.blit(elem,(j*CELL_SIZE,i*CELL_SIZE))
    #screen.blit(background, (0,0))
        pygame.display.flip()
        print "Repainted"
        scenario.show()
        
    repaint()
    pygame.time.set_timer(pygame.USEREVENT+TIME_EVENT, 256)
    pygame.display.set_caption("¡Hola pyGame!")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print "QUIT"
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: scenario.move = DOWN
                elif event.key == pygame.K_UP: scenario.move = UP
                elif event.key == pygame.K_RIGHT: scenario.move = RIGHT
                elif event.key == pygame.K_LEFT: scenario.move = LEFT
                elif event.key == pygame.K_ESCAPE:
                    print "Escape"
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.USEREVENT+TIME_EVENT:
                #pygame.time.set_timer(TIME_EVENT, 1000)
                scenario.next()
                if(scenario.colision_flag): pygame.time.wait(50) ;return 0 
                repaint() 

    return 0


"""
    scenario.show()
    EOF = 0
    while not EOF:
        try:
            entrada = raw_input()
            if(entrada == 'a'): scenario.move = LEFT
            elif(entrada == 's'): scenario.move = DOWN
            elif(entrada == 'd'): scenario.move = RIGHT
            elif(entrada == 'w'): scenario.move = UP
            scenario.next()
            scenario.show()
            if(scenario.colision_flag):
                EOF = 1
            #sys.stdout.flush()

        except EOFError:
            EOF = 1

"""
#call the "main" function if running this script
if __name__ == '__main__': 
    pygame.init()
    main()

