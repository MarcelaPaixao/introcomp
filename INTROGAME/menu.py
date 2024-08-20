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

selected_idx = 0
selected_heroes = []

def draw_heroes(screen, selected_idx):
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
    
    pygame.display.flip()        