import pygame

class personagem_gen(pygame.sprite.Sprite):
    """
    Propriedades:
        
    name
    speed
    attack
    defense
    life
    image
    #pos
    
    """
    def __init__(self, name, speed, attack, defense, life):
        super().__init__()
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.life = life
        
        self.pos = [0,0]
        self.imagem = pygame.image.load(f"./imagens/{name}.jpg")
     
    #varios defs pra pegar coisas   
    def retorn_name(self):
        return self.name
    
    def retorn_speed(self):
        return self.speed
    
    def retorn_attack(self):
        return self.attack
    
    def retorn_defense(self):
        return self.defense
    
    def retorn_life(self):
        return self.life
    
    def retorn_pos(self):
        return self.pos
    
    
class Silvio_Santos(personagem_gen):
    def __init__(self):
        super().__init__("Silvio", 100, 230, 75, 900)
        
        
    
    
    