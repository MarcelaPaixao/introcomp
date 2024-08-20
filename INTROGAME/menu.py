import pygame

# Carregar imagens dos personagens
hero_images = [
    pygame.image.load("./imagens/hero1.png"),
    pygame.image.load("./imagens/hero2.png"),
    pygame.image.load("./imagens/hero3.png"),
    pygame.image.load("./imagens/hero4.png"),
    pygame.image.load("./imagens/hero5.png")
]

# Definir posições dos personagens
hero_positions = [(100, 300), (250, 300), (400, 300), (550, 300), (700, 300)]

selected_idx = 0
selected_heroes = []