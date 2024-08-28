import pygame

COOLDOWN_TIME = 4
FREEZE = 3

width = 100
height = 290

class personagem_gen(pygame.sprite.Sprite):
    """
    Propriedades:
  
    name
    speed
    attack
    defense
    is_defending
    life
    image
    max_life
    cooldown : skill só pode ser usada a cada 3 rodadas
    pos
    """
    def __init__(self, name, speed, attack, defense, max_life):
        super().__init__()
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.original_defense = defense
        self.is_defending = False
        self.max_life = max_life
        self.life = max_life
        self.cooldown = 0
        self.pos = [0,0]
        
    # Vários métodos para retornar atributos
    def return_name(self):
        return self.name
    
    def return_speed(self):
        return self.speed
    
    def return_attack(self):
        return self.attack
    
    def return_defense(self):
        return self.defense
    
    def return_life(self):
        return self.life
    
    def return_max_life(self):
        return self.max_life
    
    def return_pos(self):
        return self.pos
    
    def return_cooldown(self):
        return self.cooldown
    
    def is_skill_ready(self):
        return self.cooldown == 0
    
    def is_alive(self):
        return self.life > 0
    
    def defend(self):
        self.defense = self.original_defense * 2
        self.is_defending = True

    def reset_defense(self):
        self.defense = self.original_defense
        self.is_defending = False
    
    def increase_life(self, life_points):
        self.life += life_points
        if self.life > self.max_life:
            self.life = self.max_life
        
    def receive_attack(self, attack):
        damage = attack * (50 / (50 + self.defense))
 
        self.life -= damage
        if self.life < 1:
            self.life = 0
            
    def attack_enemy(self, enemy):
        enemy.receive_attack(self.attack)

    def update_image(self, tam):
       self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"), tam)
    
    def update_position(self, pos):
        self.pos = pos

    def imprime_teste(self):
        print(self.name)

    
class Silvio_Santos(personagem_gen):
    """"
        - Lança aviãozinho de dinheiro que explode e causa dano na área.
    """
    def __init__(self):
        super().__init__("Silvio Santos", 70, 130, 50, 450)
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(140, 315))

    def special_skill(self, enemies):
        for enemy in enemies:
            enemy.receive_attack(100)  # Dano causado pelo avião
        self.cooldown = COOLDOWN_TIME


class Faustao(personagem_gen):
    """"
        - As dançarinas do Faustão mantêm o inimigo imóvel por 2 rodadas.
    """
    def __init__(self):
        super().__init__("Faustão", 100, 100, 190, 250)
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(140, 290))
    
    def special_skill(self, enemy):
        enemy.cooldown = FREEZE
        enemy.image = pygame.transform.scale(pygame.image.load(f"./imagens/skill/{enemy.name}_block.png"), (290, 300))
        if isinstance(enemy, Ellen_DeGeneres):
            enemy.pos = [705, 240]
        elif isinstance(enemy, Jimmy_Falon):
            enemy.pos = [570, 275]
        self.cooldown = COOLDOWN_TIME


class Ana_Maria_Braga(personagem_gen):  
    """"
        - Solta o Louro José e ele ataca os 2 inimigos.
    """
    def __init__(self):
        super().__init__("Ana Maria", 210, 80, 100, 120)
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(110, 240))  
    
    def special_skill(self, enemies):
        for enemy in enemies:
            enemy.receive_attack(90)  # Dano infligido pelo Louro José
        self.cooldown = COOLDOWN_TIME


class Patricia_Abravanel(personagem_gen):   
    """"
        - Perfume Jequiti aumenta em 50 pontos a vida de um aliado.
    """
    def __init__(self):
        super().__init__("Patricia Abravanel", 200, 75, 120, 120)  
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(200, 290))

    def special_skill(self, ally):
        ally.increase_life(60)
        self.cooldown = COOLDOWN_TIME


class Rodrigo_Faro(personagem_gen):  
    """"
        - Inimigo fica atordoado com "Dança gatinho, dança"
    """
    def __init__(self):
        super().__init__("Rodrigo Faro", 180, 90, 150, 200)
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(130, 300))

    def special_skill(self, enemy):
        enemy.receive_attack(110) 
        self.cooldown = COOLDOWN_TIME

class Ellen_DeGeneres(personagem_gen):
    def __init__(self):
        super().__init__("Ellen DeGeneres", 180, 90, 120, 400) 
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(110, 295))
        self.pos = [800, 240]
        
class Jimmy_Falon(personagem_gen):
    def __init__(self):
        super().__init__("Jimmy Fallon", 180, 140, 100, 210) 
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(100, 300))
        self.pos = [665, 275]

#Atualiza o tempo para uso da skill dos herois e freeze dos vilões
#Chamar essa função toda vez que o jogador atacar
def update_cooldown(heroes, villains): 
    tam = [0,0]
    pos = [0,0]
    for hero in heroes:
        if hero.cooldown > 0:
            hero.cooldown -= 1
    for villain in villains:
        if villain.cooldown > 0:
            villain.cooldown -= 1
        if villain.cooldown == 0:
            if isinstance(villain, Ellen_DeGeneres):
                tam = [110, 295]
                pos = [800, 240]
            elif isinstance(villain, Jimmy_Falon):
                tam = [100, 300]
                pos = [665, 275]
            villain.update_image(tam)
            villain.update_position(pos)

def update_positions(heroes):
    pos_hero = [(190, 220), (60, 260), (310, 260)]
    for i, hero in enumerate (heroes): 
            hero.pos = pos_hero[i]

def draw_characters(screen, heroes, enemies):
    for enemy in enemies:
        if enemy.is_alive(): 
            screen.blit(enemy.image, enemy.pos)
   
    for hero in heroes:
        if hero.is_alive(): 
            screen.blit(hero.image, hero.pos)
    
