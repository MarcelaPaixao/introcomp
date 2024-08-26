import pygame
from personagens import *
from menu import *

def select_ally(screen, heroes, idx_hero):
    selected_idx = 0
    run = True
    allies = []
    
    for ally in heroes:
        if ally != heroes[idx_hero]:
            allies.append(ally)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return -1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_idx = (selected_idx + 1) % len(allies)
                elif event.key == pygame.K_LEFT:
                    selected_idx = (selected_idx - 1) % len(allies)
                elif event.key == pygame.K_z:
                    return allies[selected_idx]
                elif event.key == pygame.K_x:
                    return None  # Volta ao menu de ações

            draw_ally_selection(screen, selected_idx, allies)
        
        pygame.display.flip()

def select_enemy(screen, enemies):
    run = True
    selected_idx = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return []
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_idx = (selected_idx + 1) % len(enemies)
                elif event.key == pygame.K_LEFT:
                    selected_idx = (selected_idx - 1) % len(enemies)
                elif event.key == pygame.K_z:
                    return enemies[selected_idx]
                elif event.key == pygame.K_x:
                    return None
            
            draw_enemies_selection(screen, enemies, selected_idx)

def battle_actions(screen, idx_hero, heroes, enemies):
    run = True
    selected_action = 0
    ATTACK = 0
    DEFEND = 1
    SKILL = 2
    actions = ["ATTACK", "DEFEND", "SKILL"]
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return []
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_action = (selected_action + 1) % len(actions)
                elif event.key == pygame.K_LEFT:
                    selected_action = (selected_action - 1) % len(actions)
                elif event.key == pygame.K_z:
                    if selected_action == ATTACK:
                        selected_enemy = select_enemy(screen, enemies)
                        if selected_enemy == None:
                            continue  # Volta ao menu de ações
                        else:
                            heroes[idx_hero].attack_enemy(selected_enemy)
                            run = False  # Finaliza o menu
                    
                    #ta dando erro aqui
                    elif selected_action == DEFEND:
                            heroes[idx_hero].defense *= 2  # Dobra a defesa do herói
                            run = False  # Finaliza o menu                     
                    
                    elif selected_action == SKILL:
                        if heroes[idx_hero].is_skill_ready() == True:
                            if isinstance(heroes[idx_hero], Patricia_Abravanel):
                                selected_ally = select_ally(screen, heroes, idx_hero)
                                if selected_ally == None:
                                    continue
                                else:
                                    heroes[idx_hero].special_skill(selected_ally)
                                    run = False
                            elif isinstance(heroes[idx_hero], Faustao) or isinstance(heroes[idx_hero], Rodrigo_Faro):
                                selected_enemy = select_enemy(screen, enemies)
                                if selected_enemy == None:
                                    continue  # Volta ao menu de ações
                                else:
                                    heroes[idx_hero].special_skill(selected_enemy)
                                    run = False
                            else:
                                heroes[idx_hero].special_skill(enemies)
                                run = False
                   
            draw_actions_menu(screen, selected_action, heroes[idx_hero])

    
    pygame.display.flip()