import pygame
from menu import *
from personagens import *

height = 768
width = 1024

pygame.init()

screen = pygame.display.set_mode((width, height))

"""background = pygame.image.load("./imagens/tela_inicio.jpg")
background = pygame.transform.scale(background, (width, height))
screen.blit(background, (0,0))

pygame.display.flip()"""

selected_heroes = select_heroes(screen)

background = pygame.image.load("./imagens/fundo.jpg")
background = pygame.transform.scale(background, (width, height))
screen.blit(background, (0,0))

pygame.display.flip()

draw_hero_status(screen, selected_heroes)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    



