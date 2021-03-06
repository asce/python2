#!/usr/bin/env python

import random, os.path
import sys

#import basic pygame modules
import pygame
from pygame.locals import *


BACKGROUND = 0
SNAKE = 1
FOOD = 2
ENEMY = 3
WALL = 4

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

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
    scenario = Scene(10,10,5)
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


#call the "main" function if running this script
if __name__ == '__main__': main()

