import pygame

pygame.init()

screen = pygame.display.set_mode((1024, 728))

background = pygame.image.load("./imagens/fundo.jpg")
background = pygame.transform.scale(background, (1024, 728))
screen.blit(background, (0,0))

"""fonte = pygame.font.Font(None, 75)
texto_inicio = fonte.render("TEXTO INICIO", True, pygame.Color("WHITE"))
screen.blit(texto_inicio, (390, 300))"""

d1 = pygame.image.load("./imagens/ellen_block.png")
d1 = pygame.transform.scale(d1, (250, 245))
screen.blit(d1, (675,230))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



