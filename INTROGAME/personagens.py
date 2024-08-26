import pygame

COOLDOWN_TIME = 4
FREEZE = 3

width = 160/2
height = 190/2

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
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{name}.png"),(width, height))
     
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
        if self.life < 0:
            self.life = 0
            
    def attack_enemy(self, enemy):
        enemy.receive_attack(self.attack)

    def update_image(self):
        self.image = pygame.transform.scale(pygame.image.load(f"./imagens/personagens/{self.name}.png"),(width, height))

    def imprime_teste(self):
        print(self.name)

    
class Silvio_Santos(personagem_gen):
    """"
        - Lança aviãozinho de dinheiro que explode e causa dano na área.
        - Tem muita vida, mas é o mais lento.
        - Ataque mediano e defesa muito fraca.
    """
    def __init__(self):
        super().__init__("Silvio Santos", 70, 230, 75, 500) # speed, attack, defense, max_life

    def special_skill(self, enemies):
        for enemy in enemies:
            enemy.receive_attack(40)  # Dano causado pelo avião
        self.cooldown = COOLDOWN_TIME


class Faustao(personagem_gen):
    """"
        - As dançarinas dele mantêm o inimigo imóvel por 2 rodadas.
        - Tem vida média, velocidade média.
        - Ataque forte e defesa ok.
    """
    def __init__(self):
        super().__init__("Faustão", 100, 230, 190, 250)
    
    def special_skill(self, enemy):
        enemy.cooldown = FREEZE
        #se o tamanho der errado, mandar o tamanho como parametro
        enemy.image = pygame.transform.scale(pygame.image.load(f"./imagens/{enemy.name}_block.png"), (width, height))
        self.cooldown = COOLDOWN_TIME


class Ana_Maria_Braga(personagem_gen):  
    """"
        - Solta o Louro José e ele ataca os 2 inimigos.
        - Tem vida média, velocidade ok.
        - Ataque muito forte e defesa fraca.
    """
    def __init__(self):
        super().__init__("Ana Maria", 210, 100, 100, 120)  
    def special_skill(self, enemies):
        for enemy in enemies:
            enemy.receive_attack(30)  # Dano infligido pelo Louro José
        self.cooldown = COOLDOWN_TIME


class Patricia_Abravanel(personagem_gen):   
    """"
        - Perfume Jequiti aumenta em 50 pontos a vida de um aliado.
        - Tem vida baixa, velocidade alta.
        - Ataque muito fraco e defesa média.
    """
    def __init__(self):
        super().__init__("Patricia Abravanel", 200, 75, 100, 120)  

    def special_skill(self, ally):
        ally.increase_life(50)
        self.cooldown = COOLDOWN_TIME


class Rodrigo_Faro(personagem_gen):  
    """"
        - Implementação de exemplo para Rodrigo Faro.
        - Características podem ser ajustadas.
    """
    def __init__(self):
        super().__init__("Rodrigo Faro", 180, 150, 150, 200)

    def special_skill(self, enemy):
        enemy.receive_attack(100)  # Dano alto de exemplo
        self.cooldown = COOLDOWN_TIME

class Ellen_DeGeneres(personagem_gen):
    """"

    """
    def __init__(self):
        super().__init__("Ellen DeGeneres", 180, 100, 110, 200) 
        self.pos = [320, 185]
        
class Villain2(personagem_gen):
    """"

    """
    def __init__(self):
        super().__init__("Villain2", 180, 100, 110, 200) 
        self.pos = [380, 160]

#Atualiza o tempo para uso da skill dos herois e freeze dos vilões
#Chamar essa função toda vez que o jogador atacar
def update_cooldown(heroes, villains): 
    for hero in heroes:
        if hero.cooldown > 0:
            hero.cooldown -= 1
    for villain in villains:
        if villain.cooldown > 0:
            villain.cooldown -= 1
        if villain.cooldown == 0:
            villain.update_image()

def update_positions(heroes):
    pos_hero = [(120, 155), (20, 170), (80, 200)]
    for i, hero in enumerate (heroes): 
            hero.pos = pos_hero[i]

def draw_characters(screen, heroes, enemies):
    for enemy in enemies:
        if enemy.is_alive(): 
            screen.blit(enemy.image, enemy.pos)
   
    for hero in heroes:
        if hero.is_alive(): 
            screen.blit(hero.image, hero.pos)
    
