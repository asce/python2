#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
import pygame
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

WIDTH = 640
HEIGHT = 480

def main():
	
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("¡Hola pyGame!")
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN: print "Down"
				elif event.key == pygame.K_UP: print "Up"
				elif event.key == pygame.K_RIGHT: print "Right"
				elif event.key == pygame.K_LEFT: print "Left"
				elif event.key == pygame.K_ESCAPE: 
					print "Escape"
					pygame.quit()
					sys.exit()
	return 0

if __name__ == '__main__':
	pygame.init()
	main()
