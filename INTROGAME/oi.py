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
        
        self.pos = [0, 0]
        self.imagem = pygame.image.load(f"./imagens/{name}.jpg")
     
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
    
    def increase_life(self, life_points):
        self.life += life_points
        if self.life > self.max_life:
            self.life = self.max_life
        
    def receive_attack(self, damage):
        if self.life > 0:
            self.life -= damage * (50 / (50 + self.defense))
            
    def attack_enemy(self, enemy):
        enemy.receive_attack(self.attack)

    # Método estático para atualizar o cooldown
    def update_cooldown(heroes, villains): 
        for hero in heroes:
            if hero.cooldown > 0:
                hero.cooldown -= 1
        for villain in villains:
            if villain.cooldown > 0:
                villain.cooldown -= 1

    
class Silvio_Santos(personagem_gen):
    """"
        - Lança aviãozinho de dinheiro que explode e causa dano na área.
        - Tem muita vida, mas é o mais lento.
        - Ataque mediano e defesa muito fraca.
    """
    def __init__(self):
        super().__init__("Silvio", 70, 230, 75, 500, 500) # (name, speed, attack, defense, life, max_life)

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
        super().__init__("Faustão", 100, 230, 190, 250, 250)  # (name, speed, attack, defense, life, max_life)

    def special_skill(self, enemy):
        enemy.cooldown = FREEZE
        self.cooldown = COOLDOWN_TIME


class Ana_Maria_Braga(personagem_gen):  
    """"
        - Solta o Louro José e ele ataca os 2 inimigos.
        - Tem vida média, velocidade ok.
        - Ataque muito forte e defesa fraca.
    """
    def __init__(self):
        super().__init__("Ana Maria Braga", 210, 100, 100, 120, 120)  # (name, speed, attack, defense, life, max_life)

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
        super().__init__("Patricia Abravanel", 200, 75, 100, 120, 120)  # (name, speed, attack, defense, life, max_life)

    def special_skill(self, ally):
        ally.increase_life(50)
        self.cooldown = COOLDOWN_TIME


class Rodrigo_Faro(personagem_gen):  
    """"
        - Implementação de exemplo para Rodrigo Faro.
        - Características podem ser ajustadas.
    """
    def __init__(self):
        super().__init__("Rodrigo Faro", 180, 150, 150, 200, 200)  # (name, speed, attack, defense, life, max_life)

    def special_skill(self, enemy):
        enemy.receive_attack(100)  # Dano alto de exemplo
        self.cooldown = COOLDOWN_TIME
