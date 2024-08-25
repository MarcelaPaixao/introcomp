import pygame
from personagens import *

"""hero_width = 160
hero_height = 210

screen_height = 768
screen_width = 1024"""

hero_width = 160/2
hero_height = 210/2
villain_width = 160/2
villain_height = 210/2

screen_height = 768/2
screen_width = 1024/2

panel_color = (60, 50, 70)
border_color = (200, 200, 200)
text_color = (255, 255, 255)
arrow_color = "RED"

heroes = [
    Silvio_Santos(), #1
    Patricia_Abravanel(), #2
    Ana_Maria_Braga(), #3
    Rodrigo_Faro(), #4
    Faustao() #5
]

enemy = [
    Ellen_DeGeneres(),
    Villain2()
]

# Carregar imagens dos personagens
hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Silvio Santos.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Patricia Abravanel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Ana Maria.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Rodrigo Faro.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Faustão.png"), (hero_width, hero_height))
]

# Carregar imagens dos personagens quando forem selecionados
selected_hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/selecao/silvio_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/patricia_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/ana_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/rodrigo_sel.png"), (hero_width, hero_height)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/faustao_sel.png"), (hero_width, hero_height))
]

# Definir posições dos personagens
"""hero_positions = [(190, 115), (700, 115), (150, 310), (450, 310), (725, 310)] """
hero_positions = [(190/2, 115/2), (700/2, 115/2), (150/2, 310/2), (450/2, 310/2), (725/2, 310/2)] 

#Define as ações possíveis do jogador
actions = ["ATTACK", "DEFEND", "SKILL"]

def draw_heroes_selection(screen, selected_idx, selected_heroes):
    background = pygame.image.load("./imagens/selecao/selection.png")
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
    
    enemies.append(enemy[0])
    enemies.append(enemy[1])       
    
def hero_status(screen, heroes):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 9)
    panel_width = screen_width/2.5   
    panel_height = screen_height/5  
    panel_x = screen_width - panel_width - 5
    panel_y = screen_height - panel_height - 5
    space = 22

    # Desenhar o fundo do painel
    pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, border_color, (panel_x, panel_y, panel_width, panel_height), 2)
    
    for i, hero in enumerate(heroes):
        nome = font.render(f"{hero.name.upper()}", True, text_color)
        status = font.render(f"{hero.life} / {hero.max_life}", True, text_color)
        screen.blit(nome, (panel_x + 15, panel_y + 10 + i * space))
        screen.blit(status, (panel_x + panel_x/2, panel_y + 10 + i * space))
    
    pygame.display.flip()

def draw_actions_menu(screen, selected_action, hero):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 10)
    panel_width = screen_width/1.8
    panel_height = screen_height/5  
    panel_x = 5
    panel_y = screen_height - panel_height - 5
    space = 80

    # Desenhar o fundo do painel
    pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, border_color, (panel_x, panel_y, panel_width, panel_height), 2)

    hero_name = font.render(f"{hero.name.upper()} 'S TURN:", True, text_color)
    screen.blit(hero_name, (panel_x + 15, panel_y + 10))

    for i, action in enumerate(actions):
        # Desenhar o nome da ação
        action_name = font.render(action, True, text_color)

        if hero.is_skill_ready() == False:
            if action == "SKILL":     
                action_name = font.render(action, True, "GRAY")

        screen.blit(action_name, (panel_x + 40 + i * space, panel_y + 35))        
        
        # Desenhar a seta ao lado da ação selecionada
        if i == selected_action:
            pygame.draw.polygon(screen, arrow_color, [
                (panel_x + 30 + i * space, panel_y + 40),   
                (panel_x + 20 + i * space, panel_y + 35),   
                (panel_x + 20 + i * space, panel_y + 45)    
            ])
    
    pygame.display.flip()

def draw_enemies_selection(screen, enemies, selected_idx):
    # Configurações da fonte e do fundo
    font = pygame.font.Font("./fonte/Lexend-Regular.ttf", 10)
    panel_width = screen_width/1.8
    panel_height = screen_height/5  
    panel_x = 5
    panel_y = screen_height - panel_height - 5
    space = 140

    # Desenhar o fundo do painel
    pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, border_color, (panel_x, panel_y, panel_width, panel_height), 2)

    for i, enemy in enumerate(enemies):
        # Desenhar o nome da ação
        enemy_name = font.render(enemy.name.upper(), True, text_color)
        screen.blit(enemy_name, (panel_x + 40 + i * space, panel_y + 35))        
        
        # Desenhar a seta ao lado da ação selecionada
        if i == selected_idx:
            pygame.draw.polygon(screen, arrow_color, [
                (panel_x + 30 + i * space, panel_y + 40),   
                (panel_x + 20 + i * space, panel_y + 35),   
                (panel_x + 20 + i * space, panel_y + 45)    
            ])
    
    pygame.display.flip()

def select_enemy(screen, enemies):
    run = True
    selected_idx = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return []
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_idx = (selected_idx + 1) % len(enemies)
                elif event.key == pygame.K_LEFT:
                    selected_idx = (selected_idx - 1) % len(enemies)
                elif event.key == pygame.K_z:
                    return selected_idx
                elif event.key == pygame.K_x:
                    return -1
            
            draw_enemies_selection(screen, enemies, selected_idx)
                    

def actions_menu(screen, idx_hero, heroes, enemies):
    run = True
    selected_action = 0
    #ATTACK = 0
    #DEFEND = 1
    #SKILL = 2
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return []
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_action = (selected_action + 1) % len(actions)
                elif event.key == pygame.K_LEFT:
                    selected_action = (selected_action - 1) % len(actions)
                elif event.key == pygame.K_z:
                    if selected_action == 0:
                        selected_enemy = select_enemy(screen, enemies)
                        if selected_enemy == -1:
                            continue  # Volta ao menu de ações
                        else:
                            heroes[idx_hero].attack_enemy(enemies[selected_enemy])
                            run = False  # Finaliza o menu
                    """elif selected_action == 1:
                        #selected_enemy = select_enemy(screen, enemies)                      
                        #ta errado, ver a logica da defesa
                        heroes[idx_hero].receive_attack(selected_enemy)
                        run = False  # Finaliza o menu
                    elif selected_action == 2:
                        if heroes[idx_hero].is_skill_ready() == True:
                            #fazer uma função para usar dependendo de quem for o heroi (o paramtro de cada um muda)
                    """
            draw_actions_menu(screen, selected_action, heroes[idx_hero])

    
    pygame.display.flip()
 