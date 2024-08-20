import pygame

COOLDOWN_TIME = 3
FREEZE = 2

class personagem_gen(pygame.sprite.Sprite):
    """
    Propriedades:
        
    name
    speed
    attack
    defense
    life
    image
    max_life
    cooldown : skill só pode ser usada a cada 3 rodadas
    #pos
    
    """
    def __init__(self, name, speed, attack, defense, life, max_life):
        super().__init__()
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.max_life = max_life
        self.life = life
        self.cooldown = 0
        
        self.pos = [0,0]
        self.imagem = pygame.image.load(f"./imagens/{name}.jpg")
     
    #varios defs pra pegar coisas   
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
    
    def return_life(self):
        return self.life
    
    def return_cooldown(self):
        return self.cooldown
    
    def is_skill_ready(self):
        if self.cooldown == 0:
            return True
        else:
            return False
    
    def is_alive(self):
        if self.life > 0:
            return True
        else:
            return False
    
    def increase_life(self, life_points):
        self.life += life_points
        if self.life > self.max_life:
            self.life = self.max_life
        
    
    def receive_attack(self, damage):
        if self.life > 0:
            self.life -= damage * (50/(50 + self.defense))
            
    def attack_enemy(self, enemy):
        enemy.receive_attack(self.attack) #(self.return_attack)

    #atualiza o tempo para uso da skill dos herois e freexe dos vilões
    #Chamar essa função toda vez que o jogador atacar
    def update_cooldown(heroes, villains): 
        for hero in heroes:
            if hero.cooldown > 0:
                hero.cooldown -= 1
        for villain in villains:
            if villain.cooldown > 0:
                villain.cooldown -= 1

    
class Silvio_Santos(personagem_gen):
    """"
        -lança aviãozinho de dinheiro que explode e causa dano na area
        -tem MUITA VIDA, mas é o mais lento
        -ataque mediano e defesa muito fraca
    """
    def __init__(self):
        super().__init__("Silvio", 70, 230, 75, 500) #(name, speed, attack, defense, life)
        
        def special_skill(self, enemies): #enemy: personagem_gen
            for enemy in enemies:
                enemy.receive_attack(40) #dano causdo pelo avião
            self.cooldown = COOLDOWN_TIME

            
        
class Faustao(personagem_gen):
    """"
        -as dançarinas dele mantem o inimigo imóvel por 2 rodadas
        -tem vida media, velocidade media
        -ataque forte e defesa ok
    """
    def __init__(self):
        super().__init__("Faustão", 100, 230, 190, 250) #(name, speed, attack, defense, life)

        def special_skill(self, enemy): #enemy: personagem_gen
            enemy.cooldown = FREEZE
            self.cooldown = COOLDOWN_TIME



class Ana_Maria_Braga(personagem_gen):  
    """"
        -Solta o louro José e ele ataca os 2 inimigos 
        -tem vida media, velocidade ok
        -ataque muito forte e defesa fraca
    """
    def __init__(self):
        super().__init__("Ana Maria Braga", 210, 100, 100, 120) #(name, speed, attack, defense, life)

        def special_skill(self, enemies):
            for enemy in enemies:
                enemy.receive_attack(30) #dano infligido pelo louro josé
            self.cooldown = COOLDOWN_TIME
            #self.attack_enemy(enemy) #ataca o 2 inimigo
    
    
class Patricia_Abravanel(personagem_gen):   
    """"
        -perfume jequiti aumenta em 50 pontos a vida de um aliado 
        -tem vida baixa, velocidade alta
        -ataque muito fraco e defesa media
        
        def attack_enemy(self, enemy): #enemy: personagem_gen
            enemy.receive_attack(self.attack) #(self.return_attack)
    """
    def __init__(self):
        super().__init__("Patricia Abravanel", 200, 75, 100, 120) #(name, speed, attack, defense, life)

        def special_skill(self, ally): #enemy: personagem_gen
            ally.increase_life(50)
            self.cooldown = COOLDOWN_TIME

    
    
class Rodrigo_Faro(personagem_gen):  
    """"
    """