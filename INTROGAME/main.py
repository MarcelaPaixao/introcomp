import pygame
from menu import *
from personagens import *
from batalha import *

# Dimensões da tela
height = 768/2
width = 1024/2

"""height = 768
width = 1024"""

pygame.init()

clock = pygame.time.Clock()

# Configurar a tela
screen = pygame.display.set_mode((width, height))

# Carregar e exibir o plano de fundo da tela inicial
background = pygame.transform.scale(pygame.image.load("./imagens/tela_inicio.jpg"), (width, height))
screen.blit(background, (0, 0))
pygame.display.flip()

# Inicializar listas de heróis e inimigos
selected_heroes = []
enemies = []

# Seleção de personagens
select_characters(screen, selected_heroes, enemies)

# Carregar o plano de fundo da batalha
background = pygame.transform.scale(pygame.image.load("./imagens/fundo.jpg"), (width, height))
screen.blit(background, (0, 0))

"""
    1-Carregar imagens de vitória e derrota (mantido comentado para futura implementação)
    2-ajustar imagem ded seleção (colocar um titulo no quadrado do meio)
    3-musicas e sons
    4-colocar o nome (e atributos?) dos personagens na hora da seleção
    
"""
 
win_panel = pygame.transform.scale(pygame.image.load("./imagens/win.jpg"), (width/1.5, height/1.5))
lost_panel = pygame.transform.scale(pygame.image.load("./imagens/lost.jpg"), (width/1.5, height/1.5))

run = True
current_hero_idx = -1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #screen.blit(background, (0, 0))
    
    selected_heroes = update_heroes_list(selected_heroes)
    
    if not selected_heroes and enemies:
        screen.blit(lost_panel, (width/2 - 100, height/2 - 100))
        pygame.display.flip()
        pygame.time.delay(2000)
        break
    
    draw_characters(screen, selected_heroes, enemies)
    hero_status(screen, selected_heroes)
    update_cooldown(selected_heroes, enemies)

    current_hero_idx = (current_hero_idx + 1) % len(selected_heroes)
    current_hero = selected_heroes[current_hero_idx]
    
    battle_actions(screen, current_hero_idx, selected_heroes, enemies)

    enemies = update_enemies_list(enemies)
    if not enemies:
        screen.blit(win_panel, (width/2, height/2))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    #função de ataque do inimigo, que reveza entre os dois atacando
    enemies[0].attack_enemy(current_hero)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
