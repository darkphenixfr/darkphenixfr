from random import*
import pygame
import time

# initialisation//
pygame.init()
Longueur = 1280
largeur = 720
screen = pygame.display.set_mode((Longueur,largeur))
clock = pygame.time.Clock()

# variables de Money//
money = float(0)
add_money_value = float(1)
buy_value = float(100)
boost_pets = 1
Affichage = 0
Affichage1 =0
# Prefixe de money //
liste_prefixe = [1000,1000000,1000000000,1000000000000,1000000000000000,1000000000000000000,1000000000000000000000,1000000000000000000000000,1000000000000000000000000000]
# textuels //
font = pygame.font.Font(None, 36)

# import d'Image //
money_icon = "images/money_icon.png"
money_icon_load = pygame.image.load(money_icon)
money_icon_load = pygame.transform.scale(money_icon_load,(50,50))
money_icon_rect = money_icon_load.get_rect()
money_icon_rect.x = 260
money_icon_rect.y = 10
money_icon = (640,0)

"Liste de Couleur // Palette //"
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
bc_off = (255, 183, 0)
bc_on = (255, 214, 110)

#Liste de boucles
running1 = True
running2 = True

def shop():
    global running1,money,add_money_value,boost_pets

    # Source de l'icone close //
    close_icon = "images/close.png"
    close_icon_load = pygame.image.load(close_icon)
    close_icon_rect = money_icon_load.get_rect()
    close_icon_rect.x = 1170
    close_icon_rect.y = 10
    # Source de l'icone pet_egg1 //
    price_egg1 = 1000
    pet_egg1_icon = "images/pet_egg1.png"
    pet_egg1_icon_load = pygame.image.load(pet_egg1_icon)
    pet_egg1_icon_rect = pet_egg1_icon_load.get_rect()
    pet_egg1_icon_rect.x = 110
    pet_egg1_icon_rect.y = 10
    # Variables //
    mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],150,50)
    while running1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running1 = False
                pygame.quit()

        screen.fill(black)
        
        # Affichage principale de la boutique //
        pygame.draw.rect(screen,white,[100,10,1060,700])

        # Affichage de bouton //
        yo = screen.blit(close_icon_load,close_icon_rect)
        buy_egg1 = pygame.draw.rect(screen,red,[110,270,250,100])

        # Affichage de pet egg1 //
        pet_egg1 = screen.blit(pet_egg1_icon_load,pet_egg1_icon_rect)

        # Action de clic //
        if pygame.mouse.get_pressed()[0] == True:
            if yo.collidepoint(pygame.mouse.get_pos()):
                main()
            if buy_egg1.collidepoint(pygame.mouse.get_pos()):
                if money >= price_egg1 :
                    money -= price_egg1
                    boost_gen= randint(1,100)
                    holding = True
                    if boost_gen >= 1 and boost_gen <= 50 :
                        if boost_pets < 2:
                            boost_pets = 2
                    if boost_gen >= 51 and boost_gen <= 75 :
                        if boost_pets < 3:
                            boost_pets = 3
                    if boost_gen >= 76 and boost_gen <= 95 :
                        if boost_pets < 5:
                            boost_pets = 5
                    if boost_gen >= 96 and boost_gen <= 100 :
                        if boost_pets < 100:
                            boost_pets = 100
            else :
                ts1 = font.render(f"Boost : {boost_pets}", True, (0,0,0))
                text_rect = ts1.get_rect(center=mouse_rect.center)
                screen.blit(font.render(f"vous n'avez pas assez", True, (0,0,0)), (640,360))
                    
        ts1 = font.render(f"Cost : {price_egg1}", True, (0,0,0))
        text_rect = ts1.get_rect(center=buy_egg1.center)
        screen.blit(ts1, text_rect)
        pygame.display.update()
        clock.tick(30)

def main():
    global running1,money,buy_value, add_money_value,boost_pets,Affichage,Affichage1,liste_prefixe
    while running1 :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running1 = False
        


        theback = pygame.draw.rect(screen,(255,255,255),[320,0,Longueur-640,largeur])
        red1 = pygame.draw.rect(screen,red,[0,0,320,largeur])
        red2 = pygame.draw.rect(screen,red,[Longueur-320,0,320,largeur])

        #score interface
        r_money = pygame.Rect(10,10,240,50)
        r_money_cadre = pygame.draw.rect(screen,white,r_money)
        rectangle1 = pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],150,50)

        #score button
        score_button = pygame.draw.rect(screen,white,[10,70,250,50])
        score_rect1 = pygame.Rect(70,100,150,50)
        
        #bouton boutique
        shop_button = pygame.draw.rect(screen,white,[10,150,150,50])
        
        # Affichage du boost //
        boost_panel = pygame.draw.rect(screen,white,[Longueur-310,10,150,50])
        ts1 = font.render(f"Boost : {boost_pets}", True, (0,0,0))
        text_rect = ts1.get_rect(center=boost_panel.center)
        screen.blit(ts1, text_rect)

        if pygame.mouse.get_pressed()[0] == True :
            if theback.collidepoint(pygame.mouse.get_pos()):
                temp_add_money = add_money_value*boost_pets
                money += temp_add_money
                ts1 = font.render(f"+ {temp_add_money}", True, (0,0,0))
                text_rect = ts1.get_rect(center=rectangle1.center)
                screen.blit(ts1, text_rect)

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

        # Affichage de money //
        screen.blit(money_icon_load, money_icon_rect)

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
            ts1 = font.render(f"Price : {Affichage1}", True, (0,0,0))
            text_rect = ts1.get_rect(center=score_button.center)
            screen.blit(ts1, text_rect)
        else:
            ts1 = font.render(f"Price : {buy_value}", True, (0,0,0))
            text_rect = ts1.get_rect(center=score_button.center)
            screen.blit(ts1, text_rect)
        if money > liste_prefixe[0] :
            Affichage = str(money/liste_prefixe[0])+"K"
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
            ts1 = font.render(f"{Affichage}", True, (0,0,0))
        else :
            ts1 = font.render(f"{money}", True, (0,0,0))
        text_rect = ts1.get_rect()
        text_rect.x = 20
        text_rect.y = 25
        screen.blit(ts1, text_rect)
        # Affichage du bouton boutique //
        ts1 = font.render(f"Boutique", True, (0,0,0))
        text_rect = ts1.get_rect(center=shop_button.center)
        screen.blit(ts1, text_rect)
            
        pygame.display.update()
        clock.tick(30)
main()
