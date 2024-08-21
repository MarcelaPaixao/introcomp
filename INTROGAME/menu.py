import pygame

hero_l = 160
hero_h = 210

screen_height = 768
screen_width = 1024

# Carregar imagens dos personagens
hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/hero1.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero2.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero3.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero4.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero5.png"), (hero_l, hero_h))
]

# Carregar imagens dos personagens quando forem selecionados
selected_hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/hero1_selected.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero2_selected.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero3_selected.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero4_selected.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero5_selected.png"), (hero_l, hero_h))
]

# Definir posições dos personagens
hero_positions = [(190, 115), (700, 115), (150, 310), (450, 310), (725, 310)] 

def draw_heroes(screen, selected_idx, selected_heroes):
    background = pygame.image.load("./imagens/selection.png")
    background = pygame.transform.scale(background, (screen_width, screen_height))
    screen.blit(background, (0,0))

    for i, pos in enumerate(hero_positions):
        
        if i in selected_heroes:
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
                    if len(selected_heroes) < 3 and selected_idx not in selected_heroes:
                        selected_heroes.append(selected_idx)
                    if len(selected_heroes) == 3:
                        run = False  # Finaliza o menu
                elif event.key == pygame.K_BACKSPACE and selected_heroes:
                    selected_heroes.pop()
            
                draw_heroes(screen, selected_idx, selected_heroes)
    
    return selected_heroes  # Retorna os heróis selecionados

def status_heroes(screen, heroes):
    rect_w = screen_width/2.5
    rect_h = screen_height/4
    
    status_rect =  pygame.transform.scale(pygame.image.load("./imagens/status_rect.png"), (rect_w, rect_h))
    screen.blit(status_rect, (screen_width - rect_w - 10, screen_height - rect_w - 10))

    #criar uma variavel pra cada heroi? fazer em um loop??
    
    pygame.display.flip() 


#def menu(screen, )     