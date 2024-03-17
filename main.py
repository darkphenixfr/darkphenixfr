from random import*
import pygame
import os
# initialisation//
pygame.init()
PATH = os.path.abspath(".") + "/"  # the path of the file
Longueur = 1280
largeur = 720
screen = pygame.display.set_mode((Longueur,largeur), pygame.SCALED|pygame.FULLSCREEN)
clock = pygame.time.Clock()

# variables de Money//
money = float(0)
add_money_value = float(0.1)
buy_value = float(10)
boost_pets = float(1)
Affichage = 0
Affichage1 =0
Affichage2 = 1
# Prefixe de money //
liste_prefixe = [
    1000,#0
    1000000,
    1000000000,#2
    1000000000000,
    1000000000000000,#4
    1000000000000000000,
    1000000000000000000000,#6
    1000000000000000000000000,
    1000000000000000000000000000,#8
    1000000000000000000000000000000,
    1000000000000000000000000000000000,#10
    1000000000000000000000000000000000000,
    1000000000000000000000000000000000000000,#12
    1000000000000000000000000000000000000000000]

# textuels //
font = pygame.font.Font(None, 36)

# time //
temps_dernier_clic = 0
delai_clic = 50

# Mise en echelle
Lby2 = Longueur/4
Lby4 = Longueur/4
l10 = Longueur/(Longueur/10)

# import d'Image //
money_icon = PATH+"images/money_icon.png"
money_icon_load = pygame.image.load(money_icon)
money_icon_load = pygame.transform.scale(money_icon_load,(50,50))
money_icon_rect = money_icon_load.get_rect()
money_icon_rect.x = 260
money_icon_rect.y = 10

shop_icon = PATH+"images/shop_icon.png"
shop_icon_load = pygame.image.load(shop_icon)
shop_icon_rect = money_icon_load.get_rect()
shop_icon_rect.x = 10
shop_icon_rect.y = 130

gui_set_icon = PATH+"images/gui_set.png"
gui_set_icon_load = pygame.image.load(gui_set_icon)
gui_set_icon_load = pygame.transform.scale(gui_set_icon_load,(Lby4,largeur))
gui_set_icon_rect = gui_set_icon_load.get_rect()
# x2
gui_set_icon1 = gui_set_icon
gui_set_icon_load1 = pygame.image.load(gui_set_icon)
gui_set_icon_load1 = gui_set_icon_load
gui_set_icon_rect1 = gui_set_icon_load.get_rect()
"Liste de Couleur // Palette //"
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
bc_off = (255, 183, 0)
bc_on = (255, 214, 110)

#Liste de boucles
running1 = True
running2 = True

# exemple de screen basic :
"""
def ...():
    global running1

    
    while running1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running1 = False
                pygame.quit()
        
        pygame.display.update()
        clock.tick(120)
    """

def shop():
    global running1,money,add_money_value,boost_pets, Affichage, Affichage2

    # Source de l'icone close //
    close_icon = PATH+"images/close.png"
    close_icon_load = pygame.image.load(close_icon)
    close_icon_rect = money_icon_load.get_rect()
    close_icon_rect.x = 1170
    close_icon_rect.y = l10
    # Source de l'icone pet_egg1 //
    price_egg1 = 1000
    pet_egg1_icon = "images/pet_egg1.png"
    pet_egg1_icon_load = pygame.image.load(pet_egg1_icon)
    pet_egg1_icon_rect = pet_egg1_icon_load.get_rect()
    pet_egg1_icon_rect.x = Lby4 + l10
    pet_egg1_icon_rect.y = l10
    # Variables //
    mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],150,50)
    while running1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running1 = False
                pygame.quit()

        screen.fill(black)
        
        # Affichage principale de la boutique //
        pygame.draw.rect(screen,white,[Lby4,l10,840,700])

        # Affichage de boutons //
        yo = screen.blit(close_icon_load,close_icon_rect)
        buy_egg1 = pygame.draw.rect(screen,red,[Lby4+l10,270,250,100])
        buy_egg1_max = pygame.draw.rect(screen,red,[Lby4+l10,400,250,100])

        # Affichage de pet egg1 //
        pet_egg1 = screen.blit(pet_egg1_icon_load,pet_egg1_icon_rect)

        # Money interface
        r_money = pygame.Rect(10,10,240,50)
        r_money_cadre = pygame.draw.rect(screen,white,r_money)
        screen.blit(money_icon_load, money_icon_rect)
        # Action de clic //
        if pygame.mouse.get_pressed()[0] == True:
            if yo.collidepoint(pygame.mouse.get_pos()):
                main()
            if buy_egg1_max.collidepoint(pygame.mouse.get_pos()):
                    if money >= 1000000 :
                        money -= (1000*price_egg1)
                        for j in range(1000):
                            boost_gen= randint(1,100)
                            if boost_gen >= 1 and boost_gen <= 55 :#55%
                                if boost_pets < 1.5:
                                    boost_pets = 1.5
                                else :
                                    boost_pets += 0.002
                            if boost_gen >= 56 and boost_gen <= 85 :#30%
                                if boost_pets < 2.5:
                                    boost_pets = 2.5
                                else :
                                    boost_pets += 0.035
                            if boost_gen >= 86 and boost_gen <= 95 :#10%
                                if boost_pets < 5 :
                                    boost_pets = 5
                                else :
                                    boost_pets += 0.010
                            if boost_gen >= 96 and boost_gen <= 99 :#4%
                                if boost_pets < 10:
                                    boost_pets = 10
                                else :
                                    boost_pets += 0.050
                            if boost_gen == 100 :#1%
                                if boost_pets < 20:
                                    boost_pets = 20
                                else :
                                    boost_pets += 0.10
            if buy_egg1.collidepoint(pygame.mouse.get_pos()):
                # 55|30|10|4|1
                if money >= price_egg1 :
                    money -= price_egg1
                    boost_gen= randint(1,100)
                    if boost_gen >= 1 and boost_gen <= 55 :#55%
                        if boost_pets < 2:
                            boost_pets = 2
                        else :
                            boost_pets += 0.002
                    if boost_gen >= 56 and boost_gen <= 85 :#30%
                        if boost_pets < 3.5:
                            boost_pets = 3.5
                        else :
                            boost_pets += 0.035
                    if boost_gen >= 86 and boost_gen <= 95 :#10%
                        if boost_pets < 10 :
                            boost_pets = 10
                        else :
                            boost_pets += 0.01
                    if boost_gen >= 96 and boost_gen <= 99 :#4%
                        if boost_pets < 100:
                            boost_pets = 50
                        else :
                            boost_pets += 0.05
                    if boost_gen == 100 :#1%
                        if boost_pets < 100:
                            boost_pets = 100
                        else :
                            boost_pets += 0.10
                else :
                    ts1 = font.render(f"Boost : {boost_pets}", True, (0,0,0))
                    text_rect = ts1.get_rect(center=mouse_rect.center)
                    screen.blit(font.render(f"vous n'avez pas assez", True, (0,0,0)), (640,360))
                    
        ts1 = font.render(f"Cost : {price_egg1}", True, (0,0,0))
        text_rect = ts1.get_rect(center=buy_egg1.center)
        screen.blit(ts1, text_rect)

        # Affichage de Money //////
        if money > -1:
            Affichage = round(money,2)
            if money > liste_prefixe[0] :
                Affichage = str(round(money/liste_prefixe[0],3))+"K"
                if money > liste_prefixe[1] :
                    Affichage = str(round(money/liste_prefixe[1],3))+"M"
                    if money > liste_prefixe[2] :
                        Affichage = str(round(money/liste_prefixe[2],3))+"B"
                        if money > liste_prefixe[3] :
                            Affichage = str(round(money/liste_prefixe[3],3))+"T"
                            if money > liste_prefixe[4] :
                                Affichage = str(round(money/liste_prefixe[4],3))+"Qd"
                                if money > liste_prefixe[5] :
                                    Affichage = str(round(money/liste_prefixe[5],3))+"Qn"
                                    if money > liste_prefixe[6] :
                                        Affichage = str(round(money/liste_prefixe[6],3))+"Sx"
                                        if money > liste_prefixe[7] :
                                            Affichage = str(round(money/liste_prefixe[7],3))+"Sp"
                                            if money > liste_prefixe[8] :
                                                Affichage = str(round(money/liste_prefixe[8],3))+"Oc"
                                                if money > liste_prefixe[9] :
                                                    Affichage = str(round(money/liste_prefixe[9],3))+"N"
                                                    if money > liste_prefixe[10] :
                                                        Affichage = str(round(money/liste_prefixe[10],3))+"Dc"
                                                        if money > liste_prefixe[11] :
                                                            Affichage = str(round(money/liste_prefixe[11],3))+"UD"
                                                            if money > liste_prefixe[12] :
                                                                Affichage = str(round(money/liste_prefixe[12],3))+"DD"
        
        ts1 = font.render(f"{Affichage}", True, (0,0,0))
        text_rect = ts1.get_rect()
        text_rect.x = 20
        text_rect.y = 25
        screen.blit(ts1, text_rect)
        ts1 = font.render(f"x1000", True, (0,0,0))
        text_rect = ts1.get_rect(center=buy_egg1_max.center)
        screen.blit(ts1, text_rect)
        if boost_pets > -1:
            Affichage2 = round(boost_pets,2)
            if boost_pets > liste_prefixe[0] :
                Affichage2 = str(round(boost_pets/liste_prefixe[0],3))+"K"
                if boost_pets > liste_prefixe[1] :
                    Affichage2 = str(round(boost_pets/liste_prefixe[1],3))+"M"
                    if boost_pets > liste_prefixe[2] :
                        Affichage2 = str(round(boost_pets/liste_prefixe[2],3))+"B"
                        if boost_pets > liste_prefixe[3] :
                            Affichage2 = str(round(boost_pets/liste_prefixe[3],3))+"T"
                            if boost_pets > liste_prefixe[4] :
                                Affichage2 = str(round(boost_pets/liste_prefixe[4],3))+"Qd"
                                if boost_pets > liste_prefixe[5] :
                                    Affichage2 = str(round(boost_pets/liste_prefixe[5],3))+"Qn"
                                    if boost_pets > liste_prefixe[6] :
                                        Affichage2 = str(round(boost_pets/liste_prefixe[6],3))+"Sx"
                                        if boost_pets > liste_prefixe[7] :
                                            Affichage2 = str(round(boost_pets/liste_prefixe[7],3))+"Sp"
                                            if boost_pets > liste_prefixe[8] :
                                                Affichage2 = str(round(boost_pets/liste_prefixe[8],3))+"Oc"
                                                if boost_pets > liste_prefixe[9] :
                                                    Affichage2 = str(round(boost_pets/liste_prefixe[9],3))+"N"
                                                    if boost_pets > liste_prefixe[10] :
                                                        Affichage2 = str(round(boost_pets/liste_prefixe[10],3))+"Dc"
                                                        if boost_pets > liste_prefixe[11] :
                                                            Affichage2 = str(round(boost_pets/liste_prefixe[11],3))+"UD"
                                                            if boost_pets > liste_prefixe[12] :
                                                                Affichage2 = str(round(boost_pets/liste_prefixe[12],3))+"DD"
        
        ts1 = font.render(f"Boost : {Affichage2}", True, (255,255,255))
        text_rect = ts1.get_rect()
        text_rect.x = 20
        text_rect.y = 80
        screen.blit(ts1, text_rect)
        pygame.display.update()
        clock.tick(120)
def game():
    global running1,temps_dernier_clic,projectile_player

    player_x = 0
    player_y = 700

    score_point = 0

    projectiles_x = randint(0,1240)
    projectiles_y = 0
    
    delai_ = 1000
    reloading_valu = 100
    bht = 100

    shoot_icon = PATH+"images/shoot.png"
    shoot_icon_load = pygame.image.load(shoot_icon)
    shoot_icon_rect = shoot_icon_load.get_rect()
    shoot_icon_rect.x = player_x 
    shoot_icon_rect.y = player_y - 80

    tirs = []

    while running1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running1 = False
                pygame.quit()

        keys = pygame.key.get_pressed()   

        if keys[pygame.K_d] and player_x < Longueur - 20:
            player_x += 20

        if keys[pygame.K_q] and player_x > 0 :
            player_x -= 20

        screen.fill(black)

        score_board = pygame.draw.rect(screen,(20,20,20),[(Longueur/2)-200,(largeur/2)-100,200,100])

        player = pygame.draw.rect(screen,white,(player_x,player_y,20,20))

        if projectiles_y > 680 :                            
            projectiles_y = 0
            projectiles_x = randint(0,1220)
        else :
            projectiles_y += 5

        temps_actuel = pygame.time.get_ticks()
        if temps_actuel - temps_dernier_clic >= bht :
            bht += 100
            reloading_valu += 10
            if bht == 1000 and pygame.mouse.get_pressed()[0] :
                reloading_valu = 0
                bht = 100
                tirs.append([player_x - 25, player_y - 20])
        temps_dernier_clic = temps_actuel

        #if pygame.mouse.get_pressed()[0]:
            #temps_actuel = pygame.time.get_ticks()
            #if temps_actuel - temps_dernier_clic >= delai_ :
                #reloading_valu = 0
                #bht = 100
                #tirs.append([player_x - 25, player_y - 20])


            #temps_dernier_clic = temps_actuel
            
        print(tirs)
        for tir in tirs:
            tir[1] -= 10
            if tir[1] < 0:
                tirs.remove(tir)

        #projectiles ENNEMIS
        projectiles = pygame.draw.rect(screen,(142,3,86),[projectiles_x,projectiles_y,60,60])
        
        for tir in tirs:
            shoot_icon_rect.x = tir[0]
            shoot_icon_rect.y = tir[1]
            projectile_player = screen.blit(shoot_icon_load,shoot_icon_rect)
            if projectile_player.colliderect(projectiles):
                score_point += 1
            if projectiles.colliderect(projectile_player):
                projectiles_y = 0
                projectiles_x = randint(0,1220)
                tirs.remove(tir)
        if projectiles.colliderect(player) :
            projectiles_y = 0
            projectiles_x = randint(0,1220)

        reloading_bar_bg = pygame.draw.rect(screen,white,[30,30,120,40])
        reloading_bar = pygame.draw.rect(screen,black,[40,40,reloading_valu,20])
        
        ts1 = font.render(f"SCORE : {score_point}", True, white)
        text_rect = ts1.get_rect(center=score_board.center)
        screen.blit(ts1, text_rect)

        pygame.display.flip()
        clock.tick(60)

# Boucle Principale
def main():
    global running1,money,buy_value, add_money_value,boost_pets,Affichage,Affichage1,liste_prefixe, Affichage2, temps_dernier_clic, delai_clic
    while running1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running1 = False
        
        theback = pygame.draw.rect(screen,(255,255,255),[Lby4,0,Longueur-640,largeur])
        
        # Affichage du gui //
        screen.blit(gui_set_icon_load,gui_set_icon_rect)
        gui_set_icon_rect1.x = gui_set_icon_rect.x + Longueur-Lby4
        screen.blit(gui_set_icon_load1,gui_set_icon_rect1)

        # Money interface
        r_money = pygame.Rect(10,10,240,50)
        r_money_cadre = pygame.draw.rect(screen,white,r_money)
        rectangle1 = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],150,50)

        # Upgrade button
        score_button = pygame.draw.rect(screen,white,[10,70,250,50])
        score_rect1 = pygame.Rect(70,100,150,50)
        
        # Affichage du boost //
        boost_panel = pygame.draw.rect(screen,white,[Longueur-300,10,150,50])
        

        # Affichage de la boutique//
        shop_button = screen.blit(shop_icon_load,shop_icon_rect)

        # Affichage du jeu//
        game_button = pygame.draw.rect(screen,red,[10,500,150,100])

        if pygame.mouse.get_pressed()[0] == True :
            if theback.collidepoint(pygame.mouse.get_pos()):
                temps_actuel = pygame.time.get_ticks()
                if temps_actuel - temps_dernier_clic > delai_clic:
                    temp_add_money = add_money_value*boost_pets
                    money += temp_add_money
                    ts1 = font.render(f"+ {temp_add_money}", True, (0,0,0))
                    text_rect = ts1.get_rect(center=rectangle1.center)
                    screen.blit(ts1, text_rect)
                temps_dernier_clic = temps_actuel

            if score_button.collidepoint(pygame.mouse.get_pos()):
                if money > buy_value or money == buy_value :
                    money -= buy_value
                    #multiplicateur
                    add_money_value = add_money_value*2
                    buy_value = float(buy_value*2)
                    ts1 = font.render(f"Achat effectué...", True, (0,0,0))
                    text_rect = ts1.get_rect(center=score_rect1.center)
                    screen.blit(ts1, text_rect)
                else :
                    ts1 = font.render(f"Vous n'avez pas assez", True, (0,0,0))
                    text_rect = ts1.get_rect(center=score_rect1.center)
                    screen.blit(ts1, text_rect)

            if shop_button.collidepoint(pygame.mouse.get_pos()):
                shop()

            if game_button.collidepoint(pygame.mouse.get_pos()):
                game()

        # Affichage de money //
        screen.blit(money_icon_load, money_icon_rect)
        if boost_pets > -1:
            Affichage2 = round(boost_pets,2)
            if boost_pets > liste_prefixe[0] :
                Affichage2 = str(round(boost_pets/liste_prefixe[0],3))+"K"
                if boost_pets > liste_prefixe[1] :
                    Affichage2 = str(round(boost_pets/liste_prefixe[1],3))+"M"
                    if boost_pets > liste_prefixe[2] :
                        Affichage2 = str(round(boost_pets/liste_prefixe[2],3))+"B"
                        if boost_pets > liste_prefixe[3] :
                            Affichage2 = str(round(boost_pets/liste_prefixe[3],3))+"T"
                            if boost_pets > liste_prefixe[4] :
                                Affichage2 = str(round(boost_pets/liste_prefixe[4],3))+"Qd"
                                if boost_pets > liste_prefixe[5] :
                                    Affichage2 = str(round(boost_pets/liste_prefixe[5],3))+"Qn"
                                    if boost_pets > liste_prefixe[6] :
                                        Affichage2 = str(round(boost_pets/liste_prefixe[6],3))+"Sx"
                                        if boost_pets > liste_prefixe[7] :
                                            Affichage2 = str(round(boost_pets/liste_prefixe[7],3))+"Sp"
                                            if boost_pets > liste_prefixe[8] :
                                                Affichage2 = str(round(boost_pets/liste_prefixe[8],3))+"Oc"
                                                if boost_pets > liste_prefixe[9] :
                                                    Affichage2 = str(round(boost_pets/liste_prefixe[9],3))+"N"
                                                    if boost_pets > liste_prefixe[10] :
                                                        Affichage2 = str(round(boost_pets/liste_prefixe[10],3))+"Dc"
                                                        if boost_pets > liste_prefixe[11] :
                                                            Affichage2 = str(round(boost_pets/liste_prefixe[11],3))+"UD"
                                                            if boost_pets > liste_prefixe[12] :
                                                                Affichage2 = str(round(boost_pets/liste_prefixe[12],3))+"DD"
        ts1 = font.render(f"Boost : {Affichage2}", True, (0,0,0))
        text_rect = ts1.get_rect(center=boost_panel.center)
        screen.blit(ts1, text_rect)

        if buy_value > liste_prefixe[0] :
            Affichage1 = str(buy_value/liste_prefixe[0])+"K"
            if buy_value > liste_prefixe[1] :
                Affichage1 = str(round(buy_value/liste_prefixe[1],3))+"M"
                if buy_value > liste_prefixe[2] :
                    Affichage1 = str(round(buy_value/liste_prefixe[2],3))+"B"
                    if buy_value > liste_prefixe[3] :
                        Affichage1 = str(round(buy_value/liste_prefixe[3],3))+"T"
                        if buy_value > liste_prefixe[4] :
                            Affichage1 = str(round(buy_value/liste_prefixe[4],3))+"Qd"
                            if buy_value > liste_prefixe[5] :
                                Affichage1 = str(round(buy_value/liste_prefixe[5],3))+"Qn"
                                if buy_value > liste_prefixe[6] :
                                    Affichage1 = str(round(buy_value/liste_prefixe[6],3))+"Sx"
                                    if buy_value > liste_prefixe[7] :
                                        Affichage1 = str(round(buy_value/liste_prefixe[7],3))+"Sp"
                                        if buy_value > liste_prefixe[8] :
                                            Affichage1 = str(round(buy_value/liste_prefixe[8],3))+"Oc"
                                            if buy_value > liste_prefixe[9] :
                                                Affichage1 = str(round(buy_value/liste_prefixe[9],3))+"N"
                                                if buy_value > liste_prefixe[10] :
                                                    Affichage1 = str(round(buy_value/liste_prefixe[10],3))+"Dc"
                                                    if buy_value > liste_prefixe[11] :
                                                        Affichage1 = str(round(buy_value/liste_prefixe[11],3))+"UD"
                                                        if buy_value > liste_prefixe[12] :
                                                            Affichage1 = str(round(buy_value/liste_prefixe[12],3))+"DD"

            ts1 = font.render(f"Price : {Affichage1}", True, (0,0,0))
            text_rect = ts1.get_rect(center=score_button.center)
            screen.blit(ts1, text_rect)
        else:
            ts1 = font.render(f"Price : {buy_value}", True, (0,0,0))
            text_rect = ts1.get_rect(center=score_button.center)
            screen.blit(ts1, text_rect)

        if money > -1:
            Affichage = round(money,2)
            if money > liste_prefixe[0] :
                Affichage = str(round(money/liste_prefixe[0],3))+"K"
                if money > liste_prefixe[1] :
                    Affichage = str(round(money/liste_prefixe[1],3))+"M"
                    if money > liste_prefixe[2] :
                        Affichage = str(round(money/liste_prefixe[2],3))+"B"
                        if money > liste_prefixe[3] :
                            Affichage = str(round(money/liste_prefixe[3],3))+"T"
                            if money > liste_prefixe[4] :
                                Affichage = str(round(money/liste_prefixe[4],3))+"Qd"
                                if money > liste_prefixe[5] :
                                    Affichage = str(round(money/liste_prefixe[5],3))+"Qn"
                                    if money > liste_prefixe[6] :
                                        Affichage = str(round(money/liste_prefixe[6],3))+"Sx"
                                        if money > liste_prefixe[7] :
                                            Affichage = str(round(money/liste_prefixe[7],3))+"Sp"
                                            if money > liste_prefixe[8] :
                                                Affichage = str(round(money/liste_prefixe[8],3))+"Oc"
                                                if money > liste_prefixe[9] :
                                                    Affichage = str(round(money/liste_prefixe[9],3))+"N"
                                                    if money > liste_prefixe[10] :
                                                        Affichage = str(round(money/liste_prefixe[10],3))+"Dc"
                                                        if money > liste_prefixe[11] :
                                                            Affichage = str(round(money/liste_prefixe[11],3))+"UD"
                                                            if money > liste_prefixe[12] :
                                                                Affichage = str(round(money/liste_prefixe[12],3))+"DD"
            ts1 = font.render(f"{Affichage}", True, (0,0,0))
            text_rect = ts1.get_rect()
            text_rect.x = 20
            text_rect.y = 25
            screen.blit(ts1, text_rect)
            
        pygame.display.update()
        clock.tick(30)
main()
