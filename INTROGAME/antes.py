import pygame
from menu import *
from personagens import *
from batalha import *

"""height = 768
width = 1024"""

height = 768/2
width = 1024/2

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

background = pygame.transform.scale(pygame.image.load("./imagens/tela_inicio.jpg"), (width, height))
screen.blit(background, (0,0))

pygame.display.flip()

selected_heroes = []
enemies = []
select_characters(screen, selected_heroes, enemies)
#sorted(selected_heroes)

background = pygame.transform.scale(pygame.image.load("./imagens/fundo.jpg"), (width, height))
screen.blit(background, (0,0))

#dar o blit e flip dentro do loop quando um dos dois acontecer
#win_panel = pygame.transform.scale(pygame.image.load("./imagens/win.jpg"), (width, height))
#lost_panel = pygame.transform.scale(pygame.image.load("./imagens/lost.jpg"), (width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    hero_status(screen, selected_heroes)
    #battle_actions(screen, idx_hero, selected_heroes, enemies)
    battle_actions(screen, 0, selected_heroes, enemies)
    
    hero_status(screen, selected_heroes)
    update_cooldown(selected_heroes, enemies)

    #fazer uma função pra desenhar os herois selecionados e os inimigos

    screen.blit(enemies[0].image, (10,170))
    screen.blit(enemies[1].image, (110,170))
    screen.blit(selected_heroes[0].image, (300,170))
    screen.blit(selected_heroes[1].image, (350,170))
    screen.blit(selected_heroes[2].image, (400,170))
    
    pygame.display.flip()

    clock.tick(60)

    



