import pygame
from personagens import *

hero_width = 160
hero_height = 210
villain_width = 160
villain_height = 210

screen_height = 750
screen_width = 1024
panel_height = screen_height/4.9 
panel_width = screen_width/1.85
panel_x = 15
panel_y = screen_height - panel_height - 15 

panel_color = (60, 50, 80)
border_color = (200, 200, 200)
text_color = "WHITE"
arrow_color = "RED"

heroes = [
    Silvio_Santos(), #1
    Patricia_Abravanel(), #2
    Ana_Maria_Braga(), #3
    Faustao(), #4
    Rodrigo_Faro() #5
]

enemy = [
    Ellen_DeGeneres(),
    Jimmy_Falon()
]

# Carregar imagens dos personagens
hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/Silvio Santos.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/Patricia Abravanel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/Ana Maria.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/Faustão.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/Rodrigo Faro.png"), (hero_width, hero_height))
]

# Carregar imagens dos personagens quando forem selecionados
selected_hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/silvio_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/patricia_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/ana_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/faustao_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/personagens/selecao/rodrigo_sel.png"), (hero_width, hero_height))
]

# Definir posições dos personagens
hero_positions = [(135, 120), (755, 120), (110, 325), (435, 325), (750, 325)] 

#Define as ações possíveis do jogador
actions = ["ATTACK", "DEFEND", "SKILL"]

def draw_rect(screen, panel_color, panel_x, panel_y, panel_width, panel_height):
    pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, border_color, (panel_x, panel_y, panel_width, panel_height), 3)

def draw_heroes_selection(screen, selected_idx, selected_heroes):
    background = pygame.image.load("./imagens/background/selection.png")
    background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(background, (0,0))

    for i, pos in enumerate(hero_positions):
        
        if heroes[i] in selected_heroes:
            screen.blit(selected_hero_images[i], pos)
        else:
            screen.blit(hero_images[i], pos)

        if i == selected_idx:
            pygame.draw.polygon(screen, arrow_color, [
                (pos[0] + hero_width/2, pos[1]),   # Ponto superior da seta
                (pos[0] + hero_width/2 - 12, pos[1] - 12), # Ponto inferior esquerdo
                (pos[0] + hero_width/2 + 12, pos[1] - 12)  # Ponto inferior direito
            ])
    
    pygame.display.flip()  

# Função para o menu de seleção de heróis
def select_characters(screen, selected_heroes, enemies):
    selected_idx = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return []
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_idx = (selected_idx + 1) % 5
                elif event.key == pygame.K_LEFT:
                    selected_idx = (selected_idx - 1) % 5
                elif event.key == pygame.K_z:
                    if len(selected_heroes) < 3 and heroes[selected_idx] not in selected_heroes:
                        selected_heroes.append(heroes[selected_idx])
                    if len(selected_heroes) == 3:
                        run = False  # Finaliza o menu
                elif event.key == pygame.K_BACKSPACE and selected_heroes:
                    selected_heroes.pop()
            
                draw_heroes_selection(screen, selected_idx, selected_heroes)
                
                if not run:
                    pygame.time.delay(200) 
    
    selected_heroes.sort(key=lambda hero: hero.speed, reverse=True)
    update_positions(selected_heroes)
    enemies.append(enemy[0])
    enemies.append(enemy[1])       
    
def characters_status(screen, heroes, enemies):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 15)
    panel_width = screen_width/2.5   
    panel_x = screen_width - panel_width - 10
    space = 25

    # Desenhar o fundo do painel
    draw_rect(screen, panel_color, panel_x, panel_y, panel_width, panel_height)
    
    for i, hero in enumerate(heroes):
        nome = font.render(f"{hero.name.upper()}", True, text_color)
        status = font.render(f"{hero.life:.0f} / {hero.max_life}", True, text_color)
        screen.blit(nome, (panel_x + 15, panel_y + 10 + i * space))
        screen.blit(status, (panel_x + panel_x/2 - 10, panel_y + 10 + i * space))

    for i, enemy in enumerate(enemies):
        nome = font.render(f"{enemy.name.upper()}", True, text_color)
        status = font.render(f"{enemy.life:.0f} / {enemy.max_life}", True, text_color)
        screen.blit(nome, (panel_x + 15, panel_y + 100 + i * space))
        screen.blit(status, (panel_x + panel_x/2 - 10, panel_y + 100 + i * space))
    
    pygame.display.flip()

def draw_actions_menu(screen, selected_action, hero):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 17)
    space = 150

    # Desenhar o fundo do painel
    draw_rect(screen, panel_color, panel_x, panel_y, panel_width, panel_height)
    
    hero_name = font.render(f"{hero.name.upper()} 'S TURN!", True, text_color)
    screen.blit(hero_name, (panel_x + 20, panel_y + 20))

    for i, action in enumerate(actions):
        # Desenhar o nome da ação
        action_name = font.render(action, True, text_color)

        if hero.is_skill_ready() == False:
            if action == "SKILL":     
                action_name = font.render(action, True, "GRAY")

        screen.blit(action_name, (panel_x + 70 + i * space, panel_y + 70))        
        
        # Desenhar a seta ao lado da ação selecionada
        if i == selected_action:
            pygame.draw.polygon(screen, arrow_color, [
                (panel_x + 42 + i * space, panel_y + 80),   
                (panel_x + 30 + i * space, panel_y + 72),   
                (panel_x + 30 + i * space, panel_y + 88)    
            ])
    
    pygame.display.flip()

def draw_enemies_selection(screen, enemies, selected_idx):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 17)
    space = 230

    # Desenhar o fundo do painel
    draw_rect(screen, panel_color, panel_x, panel_y, panel_width, panel_height)

    for i, enemy in enumerate(enemies):
        # Desenhar o nome da ação
        enemy_name = font.render(enemy.name.upper(), True, text_color)
        screen.blit(enemy_name, (panel_x + 70 + i * space, panel_y + 70))        
        
        # Desenhar a seta ao lado da ação selecionada
        if i == selected_idx:
            pygame.draw.polygon(screen, arrow_color, [
                (panel_x + 42 + i * space, panel_y + 80),   
                (panel_x + 30 + i * space, panel_y + 72),   
                (panel_x + 30 + i * space, panel_y + 88)    
            ])
    
    pygame.display.flip()

def draw_ally_selection(screen, selected_idx, allies):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 17)
    space = 230

    # Desenhar o fundo do painel
    draw_rect(screen, panel_color, panel_x, panel_y, panel_width, panel_height)

    for i, ally in enumerate(allies):
        # Desenhar o nome da ação
        ally_name = font.render(ally.name.upper(), True, text_color)
        screen.blit(ally_name, (panel_x + 70 + i * space, panel_y + 70))        
        
        # Desenhar a seta ao lado da ação selecionada
        if i == selected_idx:
            pygame.draw.polygon(screen, arrow_color, [
                (panel_x + 42 + i * space, panel_y + 80),   
                (panel_x + 30 + i * space, panel_y + 72),   
                (panel_x + 30 + i * space, panel_y + 88)    
            ])
    
    pygame.display.flip()

 