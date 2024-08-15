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
    max_life
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
            
    """def attack_en(self, enemy):
        enemy.receive_attack(self.return_attack)
    """
    
class Silvio_Santos(personagem_gen):
    """"
        -lança aviãozinho de dinheiro e reduz vida do inimigo
        -tem MUITA VIDA, mas é o mais lento
        -ataque mediano e defesa muito fraca
    """
    def __init__(self):
        super().__init__("Silvio", 70, 230, 75, 500) #(name, speed, attack, defense, life)
        
        def attack_enemy(self, enemy): #enemy: personagem_gen
            enemy.receive_attack(self.attack) #(self.return_attack)

        
class Faustao(personagem_gen):
        """"
        -bate com microfone? deixa atortoado?
        -tem vida media, velocidade media
        -ataque forte e defesa ok
    """
    def __init__(self):
        super().__init__("Faustão", 100, 230, 190, 250) #(name, speed, attack, defense, life)

        def attack_enemy(self, enemy): #enemy: personagem_gen
            enemy.receive_attack(self.attack) #(self.return_attack)



class Ana_Maria_Braga(personagem_gen):  
    """"
        -Solta o louro José e ele ataca os 2 inimigos
        -tem vida media, velocidade ok
        -ataque muito forte e defesa fraca
        
        def attack_enemy(self, enemy): #enemy: personagem_gen
            enemy.receive_attack(self.attack) #(self.return_attack)
    """
    def __init__(self):
        super().__init__("Ana Maria Braga", 210, 100, 100, 120) #(name, speed, attack, defense, life)

        def attack_enemy(self, enemies):
            for enemy in enemies:
                enemy.receive_attack(30) #dano infligido pelo louro josé
    
    
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

        def cure_ally(self, ally): #enemy: personagem_gen
            ally.increase_life(50)

    
    
class Rodrigo_Faro(personagem_gen):  
    """"
    """