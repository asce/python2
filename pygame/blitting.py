#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys 
import pygame
from pygame.locals import *
 
if not pygame.font: print 'estilos y letras desactivadas!'
if not pygame.mixer: print 'sonidos desactivados!'

WIDTH = 640
HEIGHT = 480

def divide_imagen(image, rect):
    subimage = image.subsurface(rect)
    return subimage, rect 

def carga_imagen(name, colorkey=None):
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'No se puede cargar la imagen:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None: 
        if colorkey is -1: 
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def carga_fondo(name, colorkey=None):
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname) 
    except pygame.error, message: 
        print 'No se puede cargar la imagen:', name
        raise SystemExit, message
    image = image.convert()
    return image, image.get_rect()

def main():
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("¡Hola pyGame!")
    fondo = carga_fondo('fantasy_border.bmp')
    
    sprite = carga_imagen('zombie.png', -1)
    anim0 = []
    anim0.append(divide_imagen(sprite[0], pygame.Rect(0, 0, 30, 80)))
    screen.blit(fondo[0], (0, 0))
    img = pygame.transform.flip(anim0[0][0], 1, 0)
    screen.blit(img, (340, 415))
    
    sprite1 = carga_imagen('skeletonghost.png', -1)
    anim1 = []
    anim1.append(divide_imagen(sprite1[0], pygame.Rect(0, 0, 70, 60)))
    img1 = pygame.transform.flip(anim1[0][0], 1, 0)
    screen.blit(img1, (200, 200))
    screen.blit(img1, (300, 300))
    screen.blit(img1, (400, 200))
    
    pygame.display.flip()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
            key = pygame.key.get_pressed()
            if key[K_RIGHT]:
                pygame.display.update()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()

