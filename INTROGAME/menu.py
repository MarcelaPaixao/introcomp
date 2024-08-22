import pygame
from personagens import *

hero_l = 160
hero_h = 210

screen_height = 768
screen_width = 1024

heroes = [
    Silvio_Santos(), #1
    Patricia_Abravanel(), #2
    Ana_Maria_Braga(), #3
    Rodrigo_Faro(), #4
    Faustao() #5
]

# Carregar imagens dos personagens
hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Silvio Santos.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Patricia Abravanel.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Ana Maria.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Rodrigo Faro.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/Faustão.png"), (hero_l, hero_h))
]

# Carregar imagens dos personagens quando forem selecionados
selected_hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/selecao/silvio_sel.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/patricia_sel.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/ana_sel.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/rodrigo_sel.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/selecao/faustao_sel.png"), (hero_l, hero_h))
]

# Definir posições dos personagens
hero_positions = [(190, 115), (700, 115), (150, 310), (450, 310), (725, 310)] 

def draw_heroes(screen, selected_idx, selected_heroes):
    background = pygame.image.load("./imagens/selecao/selection.png")
    background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(background, (0,0))

    for i, pos in enumerate(hero_positions):
        
        if heroes[i] in selected_heroes:
            screen.blit(selected_hero_images[i], pos)
        else:
            screen.blit(hero_images[i], pos)

        if i == selected_idx:
            pygame.draw.polygon(screen, "RED", [
                (pos[0] + hero_l/2, pos[1] - 3),   # Ponto superior da seta
                (pos[0] + hero_l/2 - 20, pos[1] - 20), # Ponto inferior esquerdo
                (pos[0] + hero_l/2 + 20, pos[1] - 20)  # Ponto inferior direito
            ])
    
    pygame.display.flip()  

# Função para o menu de seleção de heróis
def select_heroes(screen):
    selected_idx = 0
    selected_heroes = []
        
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
            
                draw_heroes(screen, selected_idx, selected_heroes)
    
    return selected_heroes  # Retorna os heróis selecionados

def heroes_status(screen, heroes):
    panel_w = screen_width/2.5   #400
    panel_h = panel_h = screen_height/4  #150
    
    status_panel =  pygame.transform.scale(pygame.image.load("./imagens/status_panel.png"), (panel_w, panel_h))
    screen.blit(status_panel, (screen_width - panel_w - 10, screen_height - panel_h - 10))

    #criar uma variavel pra cada heroi? fazer em um loop??
    
    pygame.display.flip() 

def draw_hero_status(screen, selected_heroes):
    # Configurações da fonte e do fundo
    font = pygame.font.Font(None, 36)
    panel_width = screen_width/2.5   #400
    panel_height = screen_height/4  #150
    panel_x = screen_width - panel_width - 20
    panel_y = screen_height - panel_height - 20
    panel_color = (50, 50, 50)
    border_color = (200, 200, 200)
    text_color = (255, 255, 255)
    selected_color = "RED"
    
    # Desenhar o fundo do painel
    pygame.draw.rect(screen, panel_color, (panel_x, panel_y, panel_width, panel_height))
    pygame.draw.rect(screen, border_color, (panel_x, panel_y, panel_width, panel_height), 3)

    # Espaçamento entre as linhas de texto
    spacing = 30
    
    for i, hero in enumerate(selected_heroes):
        # Desenhar o nome e os pontos de vida do herói
        text_surface = font.render(f"{hero.name.upper()}  {hero.life} / {hero.max_life}", True, text_color)
        screen.blit(text_surface, (panel_x + 10, panel_y + 10 + i * spacing))
    
    pygame.display.flip()



#def menu(screen, )     