import pygame

hero_l = 160
hero_h = 210

# Carregar imagens dos personagens
hero_images = [
    pygame.transform.scale(pygame.image.load("./imagens/hero1.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero2.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero3.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero4.png"), (hero_l, hero_h)),
    pygame.transform.scale(pygame.image.load("./imagens/hero5.png"), (hero_l, hero_h))
]

# Definir posições dos personagens
hero_positions = [(190, 115), (700, 115), (150, 310), (450, 310), (725, 310)] 

def draw_heroes(screen, selected_idx, selected_heroes):
    background = pygame.image.load("./imagens/selection.png")
    background = pygame.transform.scale(background, (1024, 728))
    screen.blit(background, (0,0))

    for i, pos in enumerate(hero_positions):
        screen.blit(hero_images[i], pos)

        if i == selected_idx:
            pygame.draw.polygon(screen, "RED", [
                (pos[0] + hero_l/2, pos[1] - 3),   # Ponto superior da seta
                (pos[0] + hero_l / 2 - 20, pos[1] - 20), # Ponto inferior esquerdo
                (pos[0] + hero_l / 2 + 20, pos[1] - 20)  # Ponto inferior direito
            ])
        
        if i in selected_heroes:
            # Desenha uma borda verde ao redor dos heróis já selecionados
            pygame.draw.rect(screen, "GRAY", pygame.Rect(pos[0], pos[1], hero_l, hero_h), 5)
    
    pygame.display.flip()  

# Função para o menu de seleção de heróis
def select_heroes(screen):
    selected_idx = 0
    selected_heroes = []
    
    draw_heroes(screen, -1, selected_heroes)  # Desenhar os heróis antes de processar eventos
    
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
                elif event.key == pygame.K_RETURN:
                    if len(selected_heroes) < 3 and selected_idx not in selected_heroes:
                        selected_heroes.append(selected_idx)
                    if len(selected_heroes) == 3:
                        run = False  # Finaliza o menu
                elif event.key == pygame.K_BACKSPACE and selected_heroes:
                    selected_heroes.pop()
            
                draw_heroes(screen, selected_idx, selected_heroes)
    
    return selected_heroes  # Retorna os heróis selecionados
           
               