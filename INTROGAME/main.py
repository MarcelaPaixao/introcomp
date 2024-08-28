import pygame
from menu import *
from personagens import *
from batalha import *
from audio import Audio

# Dimensões da tela
height = 750
width = 1024

pygame.init()

clock = pygame.time.Clock()
playlist = ["./sons/musica1.ogg", "./sons/musica2.ogg", "./sons/musica3.ogg"]  
win_sound = "./sons/win_sound.ogg"  # Som de vitória
lose_sound = "./sons/lose_sound.ogg"  # Som de derrota

audio_manager = Audio(playlist, win_sound, lose_sound)
audio_manager.iniciar_musica()

# Configurar a tela
screen = pygame.display.set_mode((width, height))

# Carregar e exibir o plano de fundo da tela inicial
background = pygame.transform.scale(pygame.image.load("./imagens/background/tela_inicio.png"), (width, height))
screen.blit(background, (0, 0))
pygame.display.flip()

# Inicializar listas de heróis e inimigos
selected_heroes = []
enemies = []

# Seleção de personagens
select_characters(screen, selected_heroes, enemies)

# Carregar o plano de fundo da batalha
background = pygame.transform.scale(pygame.image.load("./imagens/background/fundo.png"), (width, height))
screen.blit(background, (0, 0))

win_panel = pygame.transform.scale(pygame.image.load("./imagens/background/win.png"), (width, height))
lost_panel = pygame.transform.scale(pygame.image.load("./imagens/background/lost.png"), (width, height))

run = True
current_hero_idx = -1
current_enemy_idx = -1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    audio_manager.gerencia_musicas(event)
    screen.blit(background, (0, 0))
    
    # Verifica se todos os heróis foram derrotados
    if not selected_heroes and enemies:
        screen.blit(lost_panel, (0, 0))
        audio_manager.tocar_lose_sound()  # Toca o som de derrota
        break
    
    # Reseta a defesa dos heróis que estavam defendendo no turno anterior
    for hero in selected_heroes:
        if hero.is_defending:
            hero.reset_defense()  # Reseta a defesa ao valor normal
    
    # Desenha os personagens e atualiza a interface
    draw_characters(screen, selected_heroes, enemies)
    characters_status(screen, selected_heroes, enemies)
    update_cooldown(selected_heroes, enemies)

    # Atualiza o índice do herói atual e executa as ações de batalha
    current_hero_idx = (current_hero_idx + 1) % len(selected_heroes)
    current_hero = selected_heroes[current_hero_idx]
    
    battle_actions(screen, current_hero_idx, selected_heroes, enemies)

    # Verifica se todos os inimigos foram derrotados
    if not enemies:
        screen.blit(win_panel, (0, 0))
        audio_manager.tocar_win_sound()  # Toca o som de vitória
        break

    # Atualiza o índice do inimigo atual e realiza o ataque
    current_enemy_idx = (current_enemy_idx + 1) % len(enemies)
    current_enemy = enemies[current_enemy_idx]

    enemy_attack(current_enemy, current_hero, selected_heroes)

    # Atualiza a tela e controla o framerate
    pygame.display.flip()
    clock.tick(60)

pygame.display.flip()
pygame.time.delay(10000)
pygame.quit()
