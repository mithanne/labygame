#---|   INFORMATIONS
#---|
#---|   Date du fichier : 03/03/25 - 23h23
#---|
#---|   A FAIRE  :
#---|
#---|   - rajouter des sfx pour ce qui est déplacement, musique de combat pour le boss
#---|   - réussir à bien cibler chaque endroit ou il y doit avoir le click, pas compter sur un coup de chance
#---|   - finaliser la boutique
#---|   - trouver un 4e objet pour remplacer le couteau pendant le jeu, le couteau étant réservé au boss
#---|
#---------------------- IMPORT -----------------------

import pygame
import random
import sys
import json

#---------------------- CUSTOMISATION  -----------------------

temps = 35
nombre_niv = 5
resolution = 800
point_de_vie = 5
pv = point_de_vie

version = 1

#---------------------- TOUCHES -----------------------

KeyZ = pygame.K_z
KeyS = pygame.K_s
KeyD = pygame.K_d
KeyQ = pygame.K_q

KeyVarUp = "Z"
KeyVarLeft = "Q"
KeyVarDown = "S"
KeyVarRight = "D"

apple_key = "T"
remit_key = "Y"
stop_key = "G"
sword_key = "H"

#---------------------- INITIALISATION VARIABLE -----------------------

# Initialisation du jeu
pygame.init()

# Etat du jeu
etat = "ACCUEIL"

# Définition des couleurs (R,V,B)
noir = (0, 0, 0)
blanc = (255, 255, 255)
vert = (0, 255, 0)
bleu = (100,100,255)
rouge = (255, 0, 0)
jaune = (215, 199, 15)
gris = (128, 128, 128)

blanclaby = (255, 255, 255)

timer = (215,199,15)

# Couleur des 4 textes des pouvoirs
qA = (255,255,255)
qR = (255,255,255)
qS = (255,255,255)
qW = (255,255,255)

# Clock
clock = pygame.time.Clock()

# Dimensions du labyrinthe
longueur = 10
hauteur = 10

# Resolution de la fenêtre
Ratio = 16/9           
PH = resolution
PL = int(PH*Ratio)

# Taille d'une cellule
cell = int( ( 1/hauteur ) * PH-hauteur )

# Importation de la police
font = "assets/fonts/AlfaSlabOne-Regular_9.ttf"
taille_texte = int(PH / 20)

# a finit les niveaux requis ?
WIN = False

# a battu le boss ?
BOSS = False

# peut bouger
MOVE = False

#--------------------- Data JSON ----------------------

played_time = 0

lvl = 0
score = 0
total_time = 0
time_level = 0

total_pieces = 0
total_level = 0
apple = 0
remit = 0
stop = 0
sword = 0

win = 0
lose = 0
forfait = 0

coul_var = 0
icon_var = 0

s_music = 0
s_sfx = 0

data = {
    "played_time": played_time,
    "total_pieces": total_pieces,
    "total_level": total_level,
    "apple": apple,
    "remit": remit,
    "stop": stop,
    "sword": sword,

    "win": win,
    "lose" : lose,
    "forfait" : forfait,

    "coul_var" : coul_var,
    "icon_var" : icon_var,
    "s_music" : s_music,
    "s_sfx" : s_sfx
}


def charger_donnees():
    global played_time, total_pieces, total_level, apple, remit, stop, sword, win, lose, forfait, coul_var, icon_var, s_music, s_sfx
    try:
        with open('donnees.json', 'r') as fichier:
            donnees = json.load(fichier)
            played_time = donnees['played_time']
            total_pieces = donnees['total_pieces']
            total_level = donnees['total_level']
            apple = donnees['apple']
            remit = donnees['remit']
            stop = donnees['stop']
            sword = donnees['sword']
            win = donnees['win']
            lose = donnees['lose']
            forfait = donnees['forfait']
            coul_var = donnees['coul_var']
            icon_var = donnees['icon_var']
            s_music = donnees['s_music']
            s_sfx = donnees['s_sfx']

    except FileNotFoundError:
            played_time = 0
            total_pieces = 0
            total_level = 0
            apple = 0
            remit = 0
            stop = 0
            sword = 0
            win = 0
            lose = 0
            forfait = 0
            coul_var = 0
            icon_var = 0
            s_music = 0
            s_sfx = 0

def sauvegarder_donnees():
    donnees = {
        'played_time': played_time, 
        'total_pieces': total_pieces,
        'total_level' : total_level,
        'apple' : apple,
        'remit' : remit,
        'stop' : stop,
        'sword' : sword,
        'win' : win,
        'lose' : lose,
        'forfait': forfait,
        'coul_var' : coul_var,
        'icon_var' : icon_var,
        's_music' : s_music,
        's_sfx' : s_sfx
    }
    with open('donnees.json', 'w') as fichier:
        json.dump(donnees, fichier)

#--------------------- Sounds effects -------------------------

son_music_all = "assets/sound/music_game.wav"
pygame.mixer.music.load(son_music_all)
pygame.mixer.music.play()


son_click = pygame.mixer.Sound("assets/sound/click.wav")

liste_s_name = [son_click]


def sfx_sound(sfx_v):
    for name in liste_s_name:
        pygame.mixer.Sound.set_volume(name, sfx_v)

charger_donnees()

pygame.mixer.music.set_volume(s_music)
sfx_sound(s_sfx)

#------------------------- Importation d'autres donnés (options, controles, boutique, etc...) ---------------------

coul_var = 1
var_text = "VERT"

icon_var = 1
icon_text = "JOUEUR"

icon_pic = "assets/icons/default.png"


s_music = 0.5
s_sfx = 0.5


charger_donnees()




#--------------------- Importation des différentes images + mise à l'échelle -------------------------

charger_donnees

background_vert = pygame.image.load("assets/background_vert.jpg")
background_vert = pygame.transform.scale(background_vert, (PL, PH))
background_bleu = pygame.image.load("assets/background_bleu.jpg")
background_bleu = pygame.transform.scale(background_bleu, (PL, PH))
background_rouge = pygame.image.load("assets/background_rouge.jpg")
background_rouge = pygame.transform.scale(background_rouge, (PL, PH))
background_jaune = pygame.image.load("assets/background_jaune.jpg")
background_jaune = pygame.transform.scale(background_jaune, (PL, PH))
background_rose = pygame.image.load("assets/background_rose.jpg")
background_rose = pygame.transform.scale(background_rose, (PL, PH))

background_img = background_vert

if coul_var == 1:
    background_img = background_vert
    var_text = "VERT"
if coul_var == 2:
    background_img = background_bleu
    var_text = "BLEU" 
if coul_var == 3:
    background_img = background_rose
    var_text = "ROSE"
if coul_var == 4:
    background_img = background_rouge
    var_text = "ROUGE"
if coul_var == 5:
    background_img = background_jaune
    var_text = "JAUNE"




argent1 = pygame.image.load("assets/argent.png")
argent2 = pygame.transform.scale(argent1,(taille_texte, taille_texte))
argent3 = argent2.get_rect()
argent3.center = (PL - (int(PL / 5)) // 2, (PH/2)-cell)

level1 = pygame.image.load("assets/level.png")
level2 = pygame.transform.scale(level1,(taille_texte, taille_texte))
level3 = level2.get_rect()
level3.center = (PL - int(PL / 5) // 2, (PH/10)*3-cell)

time1 = pygame.image.load("assets/clock.png")
time2 = pygame.transform.scale(time1,(taille_texte, taille_texte))
time3 = time2.get_rect()
time3.center = (PL - int(PL / 5) // 2, (PH/10)*3-cell)


# IMAGE DE PROFIL :

Pic1 = pygame.image.load('assets/icons/default.png')
Pic1 = pygame.transform.scale(Pic1, (cell*0.8, cell*0.8))

Pic2 = pygame.image.load('assets/icons/pessi.png')
Pic2 = pygame.transform.scale(Pic2, (cell*0.8, cell*0.8))

Pic3 = pygame.image.load('assets/icons/happy.png')
Pic3 = pygame.transform.scale(Pic3, (cell*0.8, cell*0.8))

pic_var = Pic1.get_rect()
pic_var.center = (100, 100)

choix_pic = Pic1


police = pygame.font.Font(font, taille_texte)

# Plus petit que Police
police2 = pygame.font.Font(font, int(taille_texte/2))
police3 = pygame.font.Font(font, int(taille_texte/3))
police4 = pygame.font.Font(font, int(taille_texte/4))
police5 = pygame.font.Font(font, int(taille_texte/5))

# Plus grand que Police
police21 = pygame.font.Font(font, int(taille_texte*1.5))
police31 = pygame.font.Font(font, int(taille_texte*2))
police41 = pygame.font.Font(font, int(taille_texte*2.5))

#--------------------- Fonctions d'écriture de texte et d'images -------------------------

# texte basique
def basic_text(font, txt, co_x, co_y, center, coul):
    name = font.render(txt, True, coul)
    if center==True:
        name_rect = name.get_rect(center=(co_x, co_y))
        screen.blit(name, name_rect)
    elif center==False:
        screen.blit(name, (co_x,co_y))
    else:
        raise NameError
    
# texte avec 2 arguments pour PV
def advance_text(font, co_x, co_y, argm1, argm2, center):
    name = font.render("{}/{}".format(argm1,argm2), True, blanc)
    if center==True:
        name_rect = name.get_rect(center=(co_x, co_y))
        screen.blit(name, name_rect)
    elif center==False:
        screen.blit(name, (co_x,co_y))
    else:
        raise NameError

# texte avec un argument
def Argms_text(font, co_x, co_y, argm1, coul, center):
    name = font.render("{}".format(argm1), True, coul)
    if center==True:
        name_rect = name.get_rect(center=(co_x, co_y))
        screen.blit(name, name_rect)
    elif center==False:
        screen.blit(name, (co_x,co_y))
    else:
        raise NameError
    
# texte avec un argument
def Clock_Argms_text(font, co_x, co_y, argm1, coul, center):
    name = font.render("{:.2f}".format(argm1), True, coul)
    if center==True:
        name_rect = name.get_rect(center=(co_x, co_y))
        screen.blit(name, name_rect)
    elif center==False:
        screen.blit(name, (co_x,co_y))
    else:
        raise NameError
    

# rectangle basique
def basic_button(screen, x, y, long, larg, coul, center):
    name = pygame.Rect(x,y,long,larg)
    if center == True:
        name.center = (x,y)
        pygame.draw.rect(screen,coul,name, border_radius = 15)
        pygame.draw.rect(screen, blanc, name, 1, border_radius=15)

    elif center == False :
        pygame.draw.rect(screen,coul,name, border_radius = 15)
        pygame.draw.rect(screen, blanc, name, 1, border_radius=15)
    else:
        raise NameError

# affichage d'image
def aff_image(screen, nom, x, y, taille_x, taille_y, center):
    name = pygame.image.load(nom)
    name2 = pygame.transform.scale(name,(taille_x, taille_y))
    if center == True:
        name3 = name2.get_rect()
        name3.center = (x, y)
        screen.blit(name2, name3)
    elif center == False:
        screen.blit(name2,(x,y))
    else:
        raise NameError



#---------------------- CODE DU JEU (PROGRAMMATION) -----------------------
    
sortie_x = random.randint(6,8)
sortie_y = 9

def generer_labyrinthe():
    global longueur, hauteur, sortie_x, sortie_y
    
    def dfs(labyrinthe, visite, position, sortie):
        """Recherche en profondeur pour vérifier la faisabilité du niveau"""
        stack = [position]
        while stack:
            position = stack.pop()
            i, j = position
            if position == sortie:
                return True
            if 0 <= i < len(labyrinthe) and 0 <= j < len(labyrinthe[0]) and labyrinthe[i][j] == 0 and not visite[i][j]:
                visite[i][j] = True
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for neighbor in neighbors:
                    ni, nj = neighbor
                    if 0 <= ni < len(labyrinthe) and 0 <= nj < len(labyrinthe[0]) and not visite[ni][nj]:
                        stack.append(neighbor)
        return False


    def est_faisable(labyrinthe):
        entree = (1, 0)
        sortie = (sortie_x, sortie_y)
        visite = [[False for _ in range(len(labyrinthe[0]))] for _ in range(len(labyrinthe))]
        return dfs(labyrinthe, visite, entree, sortie)

    def placer_pieces(labyrinthe):
        for i in range(len(labyrinthe)):
            for j in range(len(labyrinthe[i])):
                if labyrinthe[i][j] == 0:
                    if random.randint(1, 4) == 1:
                        labyrinthe[i][j] = 2

    while True:
        labyrinthe = [[random.randint(0, 1) for _ in range(longueur)] for _ in range(hauteur)]
        labyrinthe[0] = [1] * longueur
        labyrinthe[-1] = [1] * longueur
        for i in range(hauteur):
            labyrinthe[i][0] = 1
            labyrinthe[i][-1] = 1
        labyrinthe[1][0] = 0  # Entrée
        
        # Marquer les cases spécifiques comme blanches
        labyrinthe[6][1] = 0
        labyrinthe[8][4] = 0
        labyrinthe[1][7] = 0
        
        if est_faisable(labyrinthe):
            # Parcours DFS pour marquer les cases accessibles depuis l'entrée
            visite = [[False for _ in range(longueur)] for _ in range(hauteur)]
            dfs(labyrinthe, visite, (1, 0), (sortie_x, sortie_y))
            
            # Transformer les cases non visitées en murs
            for i in range(len(labyrinthe)):
                for j in range(len(labyrinthe[i])):
                    if not visite[i][j]:
                        labyrinthe[i][j] = 1
            
            # Placer la sortie
            labyrinthe[sortie_x][sortie_y] = 0
            
            placer_pieces(labyrinthe)
            
            return labyrinthe


def a_rejoint_sortie(player_pos):
    """Fonction pour vérifier si le joueur a atteint la sortie"""
    global hauteur
    global sortie_x
    global sortie_y
    return player_pos == [sortie_x, sortie_y] 


def dessiner_labyrinthe(screen, labyrinthe, player_pos, remaining_time, score, lvl):
    global temps
    global total_pieces
    global PH, PL
    global blanclaby
    global nombre_niv
    global choix_pic
    

    """Dessiner le labyrinthe dans la fenêtre Pygame"""
    # centrage du labyrinthe
    start_x = (PL - longueur * cell) // 2 
    start_y = (PH - hauteur * cell) // 2  
    
    # transparence et réglage de l'opacité
    transparent_surface = pygame.Surface((PL/5, PH), pygame.SRCALPHA) 
    transparent_surface.fill((0, 0, 0, 60))
    
    # largeur des rectangles sur les côtés à gauche et à droite
    rect_width = int(PL / 5)
    
    screen.blit(transparent_surface, (PL - rect_width, 0))
    screen.blit(transparent_surface, (0,0))

    # génération des couleurs du labyrinthe sur l'affichage pygame
    for i in range(len(labyrinthe)):
        for j in range(len(labyrinthe[0])):
            color = noir if labyrinthe[i][j] == 1 else blanclaby

            #cellules
            pygame.draw.rect(screen, color, (start_x + j * cell, start_y + i * cell, cell, cell))
            pygame.draw.rect(screen, gris, (start_x + j * cell, start_y + i * cell, cell, cell), 1, border_radius = 0)
            if labyrinthe[i][j] == 2:
                # pieces
                pygame.draw.circle(screen, jaune, (start_x + j * cell + cell // 2, start_y + i * cell + cell // 2), cell/5) 

    #joueur 
    pygame.draw.ellipse(screen, blanclaby, (start_x + player_pos[1] * cell, start_y + player_pos[0] * cell, 1, 1))
    pygame.draw.rect(screen, gris, (start_x, start_y, len(labyrinthe[0]) * cell, len(labyrinthe) * cell), 2)
    hero_rect = pygame.Rect(start_x + player_pos[1] * cell+cell*0.1, start_y + player_pos[0] * cell+cell*0.1, cell, cell)

    screen.blit(choix_pic, hero_rect)
    

    # PARTIE DROITE

    # clock
    basic_button(screen, PL-rect_width//2, PH/2-cell*4.5, cell*3, cell, noir, True)
    Clock_Argms_text(police, PL-rect_width//2, PH/2-cell*4.5, remaining_time, timer, True)
    

    # format du texte / centrage et affichage du LVL
    basic_button(screen, PL-rect_width/2, PH/2-cell*2.5, cell*3, cell, noir, True)
    basic_text(police2, "{}/{}".format(lvl+1, nombre_niv), PL-rect_width/2, PH/2-cell*2.5, True, blanc)
    aff_image(screen, "assets/level.png", PL-rect_width/2-cell, PH/2-cell*2.5, cell*0.5, cell*0.5, True)
    basic_button(screen, PL-rect_width/2, PH/2-cell*3, cell*2, cell*0.33, noir, True)
    basic_text(police3, "NIVEAU", PL-rect_width/2, PH/2-cell*3, True, blanc)


    basic_button(screen, PL-rect_width/2, PH/2-cell*0.5, cell*3, cell, noir, True)
    basic_text(police2, "{} (+{})".format(total_pieces, score), PL-rect_width/2, PH/2-cell*0.5, True, blanc)
    aff_image(screen, "assets/argent.png", PL-rect_width/2-cell, PH/2-cell*0.5, cell*0.5, cell*0.5, True)
    basic_button(screen, PL-rect_width/2, PH/2-cell, cell*2, cell*0.33, noir, True)
    basic_text(police3, "NIVEAU", PL-rect_width/2, PH/2-cell, True, blanc)


    basic_button(screen, PL-rect_width/2, PH/2+cell*1.5, cell*3, cell, noir, True)
    basic_text(police2, "FORFAIT", PL-rect_width/2, PH/2+cell*1.5, True, blanc)
    basic_button(screen, PL-rect_width/2, PH/2+cell, cell*0.5, cell*0.33, noir, True)
    basic_text(police3, "F", PL-rect_width/2, PH/2+cell, True, blanc)

    if MOVE==True:
        basic_button(screen, PL-rect_width//2, PH-cell, cell*2, cell*0.75, vert, True)
        basic_text(police4, "DEPLACEMENT", PL-rect_width//2, PH-cell, True, blanc)
    else:
        basic_button(screen, PL-rect_width//2, PH-cell, cell*2, cell*0.75, rouge, True)
        basic_text(police4, "DEPLACEMENT", PL-rect_width//2, PH-cell, True, blanc)
    
    # PARTIE GAUCHE

    

    # insertion des rectangles noirs
    basic_button(screen, 1/10*PL, PH/2-4.5*cell, cell*3,cell*1, noir, True)
    
    basic_button(screen, 1/10*PL, PH/2-2.5*cell, cell*3, cell*1, noir, True)
    basic_button(screen, 1/10*PL, PH/2-0.5*cell, cell*3, cell*1, noir, True)
    basic_button(screen, 1/10*PL, PH/2+1.5*cell, cell*3, cell*1, noir, True)

    # insertion des images
    aff_image(screen, "assets/power_apple.png", PL/10-cell, PH/2 - 4.5*cell, cell*0.5, cell*0.5, True)
    aff_image(screen, "assets/power_remit.png", PL/10-cell, PH/2 - 2.5*cell, cell*0.5, cell*0.5, True)
    aff_image(screen, "assets/power_stop.png", PL/10-cell, PH/2 - 0.5*cell, cell*0.5, cell*0.5, True)
    aff_image(screen, "assets/power_sword.png", PL/10-cell, PH/2 + 1.5*cell, cell*0.5, cell*0.5, True)

    # insertion des touches
    basic_button(screen, PL/10+cell, PH/2-4.5*cell, cell*0.75, cell*0.75, noir, True)
    basic_button(screen, PL/10+cell, PH/2-2.5*cell, cell*0.75, cell*0.75, noir, True)
    basic_button(screen, PL/10+cell, PH/2-0.5*cell, cell*0.75, cell*0.75, noir, True)
    basic_button(screen, PL/10+cell, PH/2+1.5*cell, cell*0.75, cell*0.75, noir, True)

    
    basic_text(police2, "T", PL/10+cell, PH/2 - 4.5*cell, True, blanc)
    basic_text(police2, "Y", PL/10+cell, PH/2 - 2.5*cell, True, blanc)
    basic_text(police2, "G", PL/10+cell, PH/2 - 0.5*cell, True, blanc)
    basic_text(police2, "H", PL/10+cell, PH/2 + 1.5*cell, True, blanc)

    # insertion de la quantité des objets
    Argms_text(police2, PL/10, PH/2 - 4.5*cell, apple, qA, True)
    
    Argms_text(police2, PL/10, PH/2 - 2.5*cell, remit, qR, True)
    Argms_text(police2, PL/10, PH/2 - 0.5*cell, stop, qS, True)
    Argms_text(police2, PL/10, PH/2 + 1.5*cell, sword, qW, True)

    # point de vie
    basic_button(screen, 1*PL/10, PH/2+4.5*cell, cell*3, cell, rouge, True)
    basic_text(police2, "{} HP".format(point_de_vie), 1*PL/10, PH/2+4.5*cell, True, blanc)
    aff_image(screen,"assets/health.png", 1/10*PL-cell, PH/2 + 4.5*cell, cell*0.75, cell*0.5, True)
    

    
    # affichage
    pygame.display.flip()


#---------------------- FENETRE -----------------------

screen = pygame.display.set_mode((PL, PH))
pygame.display.set_caption("The Laby Game")



#-------------------- CODE DU JEU (DEPLACEMENT/AFFICHAGE) -------------------------

def lancer_jeu():
    global etat

    global total_pieces, total_level
    global score, lvl
    global temps
    global timer
    global total_time
    global time_level
    global nombre_niv
    global point_de_vie

    global user_pv, user_init, boss_pv, boss_init
    
    global blanclaby

    global WIN
    global BOSS
    global MOVE

    global qA, qR, qS, qW

    global apple, remit, stop, sword

    global win, lose, forfait

    global apple_key, remit_key, stop_key, sword_key

    # Générer et afficher le labyrinthe
    labyrinthe = generer_labyrinthe()
    player_pos = [1, 0]
    remaining_time = temps # Temps initial
    timer = (215,199,15)
    blanclaby = (255,255,255)
    # ----------------
    user_pv = user_init
    boss_pv = boss_init
    # initalisation du score et des pièces
    lvl = 0
    score = 0
    time_level = 0
    total_time = 0
    point_de_vie = pv

    time_add = 0

    qA = (255,255,255)
    qR = (255,255,255)
    qS = (255,255,255)
    qW = (255,255,255)
    
    # déplacement en fonction des touches
    MOVE = False
    run = True
    clock = pygame.time.Clock()

    while run:


        elapsed = clock.tick(60) / 1000
        # fonction temps restant pour afficher à la fin du jeu l'écran de fin
        remaining_time -= elapsed
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:

                if event.key == KeyZ and MOVE==True :
                    # ALLER EN HAUT
                    if labyrinthe[player_pos[0] - 1][player_pos[1]] == 0 or labyrinthe[player_pos[0] - 1][player_pos[1]] == 2:
                        player_pos[0] -= 1
                    else:
                        point_de_vie -=1
                    
                elif event.key == KeyS and MOVE==True :
                    # ALLER EN BAS
                    if labyrinthe[player_pos[0] + 1][player_pos[1]] == 0 or labyrinthe[player_pos[0] + 1][player_pos[1]] == 2:
                        player_pos[0] += 1
                    else:
                        point_de_vie -=1
                        
                elif event.key == KeyQ and MOVE==True :
                    # ALLER A GAUCHE
                    if labyrinthe[player_pos[0]][player_pos[1] - 1] == 0 or labyrinthe[player_pos[0]][player_pos[1] - 1] == 2:
                        player_pos[1] -= 1
                    else:
                        point_de_vie -=1

                elif event.key == KeyD and MOVE==True :
                    # ALLER A DROITE
                    if labyrinthe[player_pos[0]][player_pos[1] + 1] == 0 or labyrinthe[player_pos[0]][player_pos[1] + 1] == 2:
                        player_pos[1] += 1
                    else:
                        point_de_vie -=1
                

                elif event.key == pygame.K_t and MOVE == True:
                    # OBJET POMME
                    if apple>0 :
                        apple-=1
                        point_de_vie += 1
                    else :
                        qA =(255,0,0)
                    
                
                elif event.key == pygame.K_y and MOVE == True:
                    # OBJET TEMPS
                    if remit>0:
                        remit-=1
                        remaining_time += 10
                    else :
                        qR =(255,0,0)
                
                elif event.key == pygame.K_g and MOVE == True:
                    # OBJET LUMIERE
                    if stop > 0:
                        stop -= 1
                        MOVE = False
                        position_initiale = player_pos[:]
                        debut_pause = pygame.time.get_ticks()
                        blanclaby = (255, 255, 255)
                        pygame.display.flip()
                        dessiner_labyrinthe(screen, labyrinthe, position_initiale, remaining_time, score, lvl)
                        while pygame.time.get_ticks() - debut_pause < 3000:
                            pygame.display.flip()
                            pygame.event.clear(pygame.KEYDOWN)
                        blanclaby = (0, 0, 0)
                        pygame.display.flip()
                        player_pos = position_initiale
                        MOVE = True
                        remaining_time += 3
                    else:
                        qS = (255, 0, 0)
                    
                
                elif event.key == pygame.K_h and MOVE == True :
                    # OBJET EPEE
                    if sword>0 :
                        sword-=1
                        # propriété de l'usage de l'objet ici
                    else :
                        qW =(255,0,0)

                elif event.key == pygame.K_f:
                    total_pieces -= score
                    score = 0
                    forfait += 1
                    sauvegarder_donnees()

                    WIN = False
                    run = False

                    etat = "FIN"

        
        if labyrinthe[player_pos[0]][player_pos[1]] == 2:
            labyrinthe[player_pos[0]][player_pos[1]] = 0
            total_pieces +=1
            score += 1

            sauvegarder_donnees()


        # recreer le labyrinthe si joueur a atteint sortie
        if a_rejoint_sortie(player_pos):
            lvl+=1
            
            blanclaby = (255,255,255)

            time_add = 0
            if remaining_time > temps :
                time_add = remaining_time - temps
            remaining_time = temps + time_add
            player_pos = [1, 0]
            labyrinthe = generer_labyrinthe()
            time_level = 0
            MOVE = False
            timer = (215,199,15)
            
            

        # affichage des différents éléments
        screen.blit(background_img, (0, 0))
        dessiner_labyrinthe(screen, labyrinthe, player_pos, remaining_time, score, lvl)
        pygame.display.flip()
        
        

        if MOVE == True:
            total_time+= elapsed
            time_level+= elapsed
        
        if remaining_time < int(time_add+temps-5):
            MOVE = True
            timer = (255,255,255)
            
            for i in range(255,0,-1):
                blanclaby=(i,i,i)
            
        
        if remaining_time <= 10:
            timer = (255,0,0)
        
        if remaining_time <= 0 or point_de_vie<=0:
            total_level += lvl
            lose += 1
            sauvegarder_donnees()
            WIN = False
            run = False
            etat ="FIN"

        if lvl== nombre_niv:
            remaining_time = 0
            etat = "BOSS"

        
#-------------------- ACCUEIL -------------------------


def afficher_page_accueil():
    global etat
    global total_pieces
    global total_level
    global police, police2, police3

    charger_donnees()

    # coordonnés des boutons ou ce sera cliquable
    jouer_button = pygame.Rect(PL/2-cell*2, PH/2-cell*1.5, cell*4, cell)
    boutique_button = pygame.Rect(PL/2-cell*2, PH/2, cell*4, cell)
    options_button = pygame.Rect(PL/2-cell*2, PH/2+1.5*cell, cell*4, cell)
    help_button = pygame.Rect(PL/2-cell*2, PH/2+3*cell, cell*4, cell)
    leave_button = pygame.Rect(PL-cell*3, cell, cell*2, cell)
    stats_button = pygame.Rect(PL-cell*5.5, cell, cell*2, cell)

    #boucle tant que la page d'accueil
    while etat == "ACCUEIL":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if jouer_button.collidepoint(event.pos):  
                        etat = "JEU"
                    elif boutique_button.collidepoint(event.pos):
                        etat = "BOUTIQUE"
                    elif options_button.collidepoint(event.pos):
                        etat = "OPTIONS"
                    elif help_button.collidepoint(event.pos):
                        etat = "CTRL"
                    elif stats_button.collidepoint(event.pos):
                        etat = "STATS"
                    elif leave_button.collidepoint(event.pos):
                        etat = "QUITTER"
                        pygame.quit()
                        return
                    
        
        # insertion du fond
        screen.blit(background_img, (0, 0))
        
        # insertion de l'argent en haut à gauche        
        aff_image(screen, "assets/argent.png", cell*2, cell, cell, cell, True) # affiche image asset argent
        basic_button(screen, cell, cell, cell*2, cell, noir, False) # affiche le rectangle noir
        Argms_text(police2, cell*2, cell*1.5, total_pieces, blanc, True) # affiche la quantité
        basic_text(police4,"EUROS", cell*2, cell*1.75, True, blanc)


        # insertion du level en haut à gauche        
        aff_image(screen, "assets/level.png", cell*4.5, cell, cell, cell, True) # affiche image asset argent
        basic_button(screen, cell*3.5, cell, cell*2, cell, noir, False) # affiche le rectangle noir
        Argms_text(police2, cell*4.5, cell*1.5, total_level, blanc, True) # affiche la quantité
        basic_text(police4,"NIV", cell*4.5, cell*1.75, True, blanc)

        
        # insertion du titre
        basic_button(screen, PL/2, cell*1.5, cell*7.5, cell*2, noir, True)
        basic_text(police2, "THE", PL/2, cell*2-taille_texte*2, True, gris)
        basic_text(police21, "LABY GAME", PL/2, cell*1.5, True, blanc)
        basic_text(police3, "Version - {}".format(version), 0, PH-taille_texte/2, False, blanc)

        
        # insertion des rectangles noirs pour les boutons
        jouer = basic_button(screen , PL/2, PH/2-cell, cell*5, cell, noir, True)
        boutique = basic_button(screen , PL/2, PH/2+0.5*cell, cell*5, cell, noir, True)
        options = basic_button(screen , PL/2, PH/2+2*cell, cell*5, cell, noir, True)
        help = basic_button(screen , PL/2, PH/2+3.5*cell, cell*5, cell, noir, True)

        aff_image(screen, "assets/play.png", PL/2-cell*2.5, PH/2-cell, cell*0.7, cell*0.7, True)
        aff_image(screen, "assets/store.png", PL/2-cell*2.5, PH/2+0.5*cell, cell*0.7, cell*0.7, True)
        aff_image(screen, "assets/option.png", PL/2-cell*2.5, PH/2+2*cell, cell*0.7, cell*0.7, True)
        aff_image(screen, "assets/help.png", PL/2-cell*2.5, PH/2+3.5*cell, cell*0.7, cell*0.7, True)

        # insertion des textes pour les boutons
        basic_text(police, "JOUER", PL/2, PH/2-cell, True, blanc)
        basic_text(police, "BOUTIQUE", PL/2, PH/2+0.5*cell, True, blanc)
        basic_text(police, "OPTIONS", PL/2, PH/2+2*cell, True, blanc)
        basic_text(police, "CONTROLES", PL/2, PH/2+3.5*cell, True, blanc)

        aff_image(screen, "assets/door.png", PL-cell*2, cell, cell, cell, True) # affiche image asset argent
        basic_button(screen, PL-cell*3, cell, cell*2, cell, noir, False) # affiche le rectangle noir
        basic_text(police2, "QUITTER", PL-cell*2, cell*1.5, True, blanc)

        aff_image(screen, "assets/stats.png", PL-cell*4.5, cell, cell, cell, True) # affiche image asset argent
        basic_button(screen, PL-cell*5.5, cell, cell*2, cell, noir, False) # affiche le rectangle noir
        basic_text(police2, "STATS", PL-cell*4.5, cell*1.5, True, blanc)

        # maj écran
        pygame.display.flip() 


#-------------------- BOSS DU JEU -------------------------
        
user_pv = 20
user_init = user_pv
boss_pv = 20
boss_init = boss_pv

num_joueur = random.randint(2,5)
num_boss = random.randint(2,5)
pouvoir_boss = "?"
aff_dif_num = ""

critical_hit = False

num_tour = 1

pv_info_J = ""
pv_coul_J = rouge

pv_info_B = ""
pv_coul_B = rouge


logESP = ""
log_coul = blanc


WAIT = False
END = False

def afficher_boss():
    global WIN
    global etat
    global background_img

    global win, lose

    global user_pv, user_init, boss_pv, boss_init

    global critical_hit
    global sword

    global num_boss, num_joueur, pouvoir_boss, aff_dif_num
    global num_tour, WAIT, END

    global pv_info_J, pv_info_B

    global logESP, log_coul

    charger_donnees()

    # Affichage du fond
    screen.blit(background_img, (0, 0))



    # Emplacement de l'inventaire en bas vers la gauche

    basic_button(screen, PL/2-cell*2.5, PH-cell, cell*4, cell, noir, True)

    basic_button(screen, PL/2-cell*2.5, PH-cell*1.5, cell*2, cell*0.33, noir, True)
    basic_text(police3, "INVENTAIRE", PL/2-cell*2.5, PH-cell*1.5, True, blanc)

    aff_image(screen, "assets/power_sword.png", PL/2-cell*3.5, PH-cell, cell*0.6, cell*0.6, True)
    basic_text(police2, "{}".format(sword), PL/2-cell*2, PH-cell, True, blanc)
    


    # Emplacement Informations en haut au milieu
    basic_button(screen, PL/2, cell*3.5, 7*PL/8, cell*6, noir, True)

    basic_button(screen, PL/2, cell*0.5, cell*2, cell*0.5, noir, True)
    basic_text(police3, "TOUR {}".format(num_tour), PL/2, cell*0.5, True, blanc)


    # Informations JOUEUR
    basic_button(screen, 1*PL/4, PH/2-cell*2, cell*4, cell*4, noir, True)
    basic_button(screen, 1*PL/4, PH/2-cell*4, cell*2, cell*0.5, noir, True)
    basic_text(police3, "VOUS", 1*PL/4, PH/2-cell*4, True, blanc)
    basic_text(police3, "POUVOIR", 1*PL/4, PH/2-cell*2.5, True, blanc)
    basic_text(police, "{}".format(num_joueur), 1*PL/4, PH/2-cell*2, True, blanc)

    # Espace sur le coup CRITIQUE
    basic_button(screen, 1*PL/4, PH/2, cell*4, cell*0.75, noir, True)
    basic_text(police3, "CRTIQUE", 1*PL/4-cell, PH/2, True, blanc)

    basic_button(screen, 1*PL/4, PH/2, cell*0.5, cell*0.5, noir, True)
    
    if critical_hit == True:
        basic_text(police3, "ACTIVÉ", 1*PL/4+cell, PH/2, True, vert)
    else :
        basic_text(police3, "DESACTIVÉ", 1*PL/4+cell, PH/2, True, rouge)

    
    basic_text(police3, "F", 1*PL/4, PH/2, True, blanc)

    # Informations BOSS
    basic_button(screen, 3*PL/4, PH/2-cell*2, cell*4, cell*4, noir, True)
    basic_button(screen, 3*PL/4, PH/2-cell*4, cell*2, cell*0.5, noir, True)
    basic_text(police3, "LE CREATEUR", 3*PL/4, PH/2-cell*4, True, blanc)
    basic_text(police3, "POUVOIR", 3*PL/4, PH/2-cell*2.5, True, blanc)
    basic_text(police, "{}".format(pouvoir_boss), 3*PL/4, PH/2-cell*2, True, blanc)
    

    # Informations sur la différence de pouvoir
    basic_text(police, "{}".format(aff_dif_num), PL/2, PH/2-cell*2, True, blanc)
    

    # Touches PLUS ou MOINS, et ESPACE
    if WAIT == False:
        basic_button(screen, PL/2-cell*2, PH/2+cell*2, cell*3, cell, noir, True)
        basic_text(police2, "PLUS", PL/2-cell*2, PH/2+cell*2, True, blanc)

        basic_button(screen, PL/2-cell*2, PH/2+cell*2.5, cell*0.5, cell*0.33, noir, True)
        basic_text(police3, "A", PL/2-cell*2, PH/2+cell*2.5, True, blanc)

        basic_button(screen, PL/2+cell*2, PH/2+cell*2, cell*3, cell, noir, True)
        basic_text(police2, "MOINS", PL/2+cell*2, PH/2+cell*2, True, blanc)

        basic_button(screen, PL/2+cell*2, PH/2+cell*2.5, cell*0.5, cell*0.33, noir, True)
        basic_text(police3, "E", PL/2+cell*2, PH/2+cell*2.5, True, blanc)

    else:
        logESP = "PRESSEZ ESPACE POUR CONTINUER"
        basic_button(screen, PL/2, PH/2+cell*2, cell*7, cell, noir, True)
        basic_text(police2, "{}".format(logESP), PL/2, PH/2+cell*2, True, blanc)    


    # Informations user en bas à gauche
    basic_button(screen, cell*3, PH-cell, cell*4, cell, noir, True)
    basic_button(screen, cell*3, PH-cell*1.5, cell*2, cell*0.33, noir, True)
    basic_text(police3, "VOUS", cell*3, PH-cell*1.5, True, blanc)
    basic_text(police2, "{}/{}".format(user_pv, user_init), cell*3, PH-cell, True, blanc)

    basic_button(screen, cell*1.5, PH-cell*2.1, cell, cell, noir, True)
    aff_image(screen, "assets/user_pic.png", cell*1.5, PH-cell*2.1, cell*0.8, cell*0.8, True)

    basic_text(police2, "{}".format(pv_info_J), cell*4.5, PH-cell, True, pv_coul_J)
   

    # Informations boss en bas à droite
    basic_button(screen, PL-cell*3, PH-cell, cell*4, cell, noir, True)
    basic_button(screen, PL-cell*3, PH-cell*1.5, cell*2, cell*0.33, noir, True)
    basic_text(police3, "LE CRÉATEUR", PL-cell*3, PH-cell*1.5, True, blanc)
    basic_text(police2, "{}/{}".format(boss_pv, boss_init), PL-cell*3, PH-cell, True, blanc)

    basic_button(screen, PL-cell*1.5, PH-cell*2.1, cell, cell, noir, True)
    aff_image(screen, "assets/dragon_boss.png", PL-cell*1.5, PH-cell*2.1, cell*0.8, cell*0.8, True)

    basic_text(police2, "{}".format(pv_info_B), PL-cell*4.5, PH-cell, True, pv_coul_B)


    
    
    if user_pv <=0 and boss_pv>0:
        basic_button(screen, PL/2, PH/2, PL-cell, PH-cell, rouge, True)
        basic_text(police, "VOUS AVEZ PERDU", PL/2, PH/2, True, noir)
        WIN=False
        END = True
        lose += 1

    if user_pv>0 and boss_pv <=0:
        basic_button(screen, PL/2, PH/2, PL-cell, PH-cell, vert, True)
        basic_text(police, "VOUS AVEZ GAGNER", PL/2, PH/2, True, noir)
        WIN = True
        END = True
        win += 1
    

    # boucle des options
    while etat == "BOSS":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                # COUP CRITIQUE
                if WAIT == False :
                    if event.key == pygame.K_f:
                        if sword > 0:
                            if critical_hit == False:
                                critical_hit = True
                            else :
                                critical_hit = False

                        afficher_boss()

                    # PLUS
                    elif event.key == pygame.K_a :
                        if num_joueur > num_boss :
                            dif_num = num_joueur - num_boss
                            if critical_hit == True:
                                sword -= 1
                                sauvegarder_donnees()

                                boss_pv -= dif_num * 2
                                pv_info_B = "-{}".format(dif_num*2)
                                

                            else:
                                boss_pv -= dif_num
                                pv_info_B = "-{}".format(dif_num)

                                

                        elif num_joueur < num_boss :
                            dif_num = num_boss - num_joueur
                            user_pv -= dif_num
                            pv_info_J = "-{}".format(dif_num)
                            
                            dif_num = -dif_num
                        
                        elif num_joueur == num_boss :
                            pv_info_J = ""
                            pv_info_B = ""
                            dif_num = 0
                            
                        aff_dif_num = dif_num
                        pouvoir_boss = num_boss
                        WAIT = True
                        afficher_boss()

                    # MOINS
                    elif event.key == pygame.K_e :
                    
                        if num_joueur < num_boss :
                            dif_num = num_boss - num_joueur
                            if critical_hit == True:
                                sword -= 1
                                sauvegarder_donnees()

                                boss_pv -= dif_num * 2
                                pv_info_B = "-{}".format(dif_num*2)
                            else:
                                boss_pv -= dif_num
                                pv_info_B = "-{}".format(dif_num)
                    
                        else:
                            dif_num = num_joueur - num_boss
                            user_pv -= dif_num
                            pv_info_B = "-{}".format(dif_num)
                            dif_num = -dif_num
                            
                        aff_dif_num = dif_num
                        pouvoir_boss = num_boss
                        WAIT = True
                        afficher_boss()
                
                elif event.key == pygame.K_SPACE :
                    if WAIT == True and END == False:
                        num_tour += 1
                        num_boss = random.randint(2,7)
                        num_joueur = random.randint(2,7)
                        critical_hit = False
                        WAIT = False
                        logESP = ""

                        pv_info_B = ""
                        pv_info_J = ""
                        
                        pouvoir_boss = "?"
                        aff_dif_num = ""
                        afficher_boss()
                        
                    elif WAIT== True and END == True:
                        sauvegarder_donnees()
                        END = True
                        etat = "FIN"

                        user_pv = 20
                        user_init = user_pv
                        boss_pv = 20
                        boss_init = boss_pv

                        num_joueur = random.randint(2,5)
                        num_boss = random.randint(2,5)
                        pouvoir_boss = "?"
                        aff_dif_num = ""

                        critical_hit = False

                        num_tour = 1

                        pv_info_J = ""
                        pv_info_B = ""
                        
                        logESP = ""
                        log_coul = blanc

                        WAIT = False
                        END = False




                

                
            
                

        # Maj écran
        pygame.display.flip()
               

#-------------------- BOUTIQUE -------------------------
        
def warn_text(buy_font):
    warning_text = buy_font.render("VOUS NE POUVEZ PAS ACHETER CET OBJET", True, (255, 0, 0))
    warn2_text = warning_text.get_rect()
    warn2_text.center = ((PL // 2, 7*PH // 9))
    screen.blit(warning_text, warn2_text)

charger_donnees()

item_name = "POMME"
item_loc = "assets/power_apple.png"
item_price = 3
item_quantity = apple
item_var = 1


def afficher_page_boutique():
    global etat
    global background_img
    global total_pieces
    global blanc

    global remit, apple, stop, sword

    global item_name, item_loc, item_price, item_quantity, item_var

    charger_donnees()

    # affichage du fond
    screen.blit(background_img, (0, 0))
    
    # Titre boutique
    basic_button(screen, PL/2, cell*1.5, cell*5, cell, noir, True)
    basic_text(police, "BOUTIQUE", PL/2, cell*1.5, True, blanc)

    # Bouton retour
    retour_button = pygame.Rect(PL/2-cell*2, PH-cell*2, cell*4, cell)
    basic_button(screen, PL/2, PH-cell*1.5, cell*4, cell, noir, True)
    basic_text(police, "RETOUR", PL/2, PH-cell*1.5, True, blanc)

    # insertion de l'argent en haut à gauche           
    aff_image(screen, "assets/argent.png", cell*2, cell, cell, cell, True) # affiche image asset argent
    basic_button(screen, cell, cell, cell*2, cell, noir, False) # affiche le rectangle noir
    Argms_text(police2, cell*2, cell*1.5, total_pieces, blanc, True) # affiche la quantité
    basic_text(police4,"EUROS", cell*2, cell*1.75, True, blanc)
        

    basic_button(screen, PL/2, PH/2, cell*6, PH/2, noir, True)

    
    basic_text(police2, "{}".format(item_name), PL/2, PH/2-cell*2, True, blanc)
    basic_button(screen, PL/2-cell*2, PH/2-cell*2, cell, cell, noir, True)
    aff_image(screen, "{}".format(item_loc), PL/2-cell*2, PH/2-cell*2, cell*0.67, cell*0.67, True)

    basic_button(screen, PL/2-cell*1.5, PH/2, cell*2, cell, noir, True)
    basic_button(screen, PL/2+cell*1.5, PH/2, cell*2, cell, noir, True)

    basic_button(screen, PL/2-cell*1.5, PH/2-cell*0.5, cell*1.5, cell*0.33, noir, True)
    basic_button(screen, PL/2+cell*1.5, PH/2-cell*0.5, cell*1.5, cell*0.33, noir, True)

    basic_text(police3, "PRIX", PL/2-cell*1.5, PH/2-cell*0.5, True, blanc)
    basic_text(police3, "POSSEDÉ", PL/2+cell*1.5, PH/2-cell*0.5, True, blanc)

    basic_text(police2, "{}".format(item_price), PL/2-cell*1.5, PH/2, True, blanc)
    basic_text(police2, "{}".format(item_quantity), PL/2+cell*1.5, PH/2, True, blanc)

    next_button = pygame.Rect(PL/2+cell*4, PH/2-cell*0.5, cell*2, cell)
    basic_button(screen, PL/2+cell*5, PH/2, cell*2, cell, noir, True)
    basic_text(police, ">", PL/2+cell*5, PH/2, True, blanc)
    basic_text(police3, "SUIVANT", PL/2+cell*5, PH/2-cell*0.75, True, blanc)

    buy_button = pygame.Rect(PL/2-cell*1.5, PH/2+cell*1.5, cell*3, cell)
    basic_button(screen, PL/2, PH/2+cell*2, cell*3, cell, noir, True)
    basic_text(police2, "ACHETER", PL/2, PH/2+cell*2, True, blanc)

    # texte si l'user ne peut pas acheter un item
    warning_text = police2.render("", True, (255, 0, 0))
    warn2_text = warning_text.get_rect()
    warn2_text.center = ((PL // 2, 7*PH // 9))
    screen.blit(warning_text, warn2_text)

    charger_donnees()
    item_quantity = apple

    # boucle de la boutique
    while etat == "BOUTIQUE":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if retour_button.collidepoint(event.pos):  
                        etat = "ACCUEIL"

                    if next_button.collidepoint(event.pos):
                        
                        if item_var ==4:
                            item_var = 0
                            
                        if item_var ==0:
                            item_name = "POMME"
                            item_loc = "assets/power_apple.png"
                            item_price = 3
                            item_quantity = apple
                            
                        if item_var ==1:
                            item_name = "TIMER"
                            item_loc = "assets/power_remit.png"
                            item_price = 4
                            item_quantity = remit
                            
                        if item_var ==2:
                            item_name = "STOP"
                            item_loc = "assets/power_stop.png"
                            item_price = 5
                            item_quantity = stop
                            
                        if item_var ==3:
                            item_name = "COUTEAU"
                            item_loc = "assets/power_sword.png"
                            item_price = 2
                            item_quantity = sword

                        item_var +=1

                    if buy_button.collidepoint(event.pos):
                        if total_pieces > item_price:
                            if item_name=="POMME" :
                                apple += 1
                                total_pieces -= item_price
                                item_quantity = apple

                            if item_name=="TIMER" :
                                remit += 1
                                total_pieces -= item_price
                                item_quantity = remit

                            if item_name=="STOP" :
                                stop += 1
                                total_pieces -= item_price
                                item_quantity = stop

                            if item_name=="COUTEAU" :
                                sword += 1
                                total_pieces -= item_price
                                item_quantity = sword
                        
                        sauvegarder_donnees()

                    afficher_page_boutique()
                    pygame.display.flip()
                        
                            
                        
        # maj écran
        pygame.display.flip()

#-------------------- OPTIONS -------------------------


def afficher_options():
    global etat
    global background_img
    global police, police2, police3, police4
    global coul_var, var_text
    global pic_var, icon_var, icon_text
    global choix_pic, icon_pic

    global s_music, s_sfx

    # Affichage du fond
    screen.blit(background_img, (0, 0))
    
    # Titre page option
    basic_button(screen, PL/2, cell*1.5, cell*5, cell, noir, True)
    basic_text(police, "OPTIONS", PL/2, cell*1.5, True, blanc)

    # Bouton retour
    retour_button = pygame.Rect(PL/2-cell*2, PH-cell*2, cell*4, cell)
    basic_button(screen, PL/2, PH-cell*1.5, cell*4, cell, noir, True)
    basic_text(police, "RETOUR", PL/2, PH-cell*1.5, True, blanc)

            
    #Couleur
    couleur_button = pygame.Rect(9*PL/10-cell*3, PH/2-cell*2, cell*4, cell)
    basic_button(screen, PL/2, PH/2-cell*1.5, 9*PL/10, PH/10, noir, True)
    basic_button(screen, 9*PL/10-cell, PH/2-cell*1.5, cell*4, cell, noir, True)
    basic_text(police2, "CHANGER LA COULEUR", 9*PL/10-cell, PH/2-cell*1.5, True, blanc)
    basic_text(police2, "COULEUR DE FOND SELECTIONNER   ,", PL/4, PH/2-cell*1.5, True, blanc)
    basic_text(police2, var_text, PL/2, PH/2-cell*1.5, True, blanc)
    basic_text(police2, "{}/5".format(coul_var), 3*PL/4-cell, PH/2-cell*1.5, True, blanc)


    icon_button = pygame.Rect(9*PL/10-cell*3, PH/2-cell*0.5, cell*4, cell)
    basic_button(screen, PL/2, PH/2, 9*PL/10, PH/10, noir, True)
    basic_button(screen, 9*PL/10-cell, PH/2, cell*4, cell, noir, True)
    basic_text(police2, "CHANGER L'ICONE", 9*PL/10-cell, PH/2, True, blanc)
    basic_text(police2, "ICONE SELECTIONNE   ,", PL/4, PH/2, True, blanc)
    basic_text(police2, icon_text, PL/2, PH/2, True, blanc)
    basic_text(police2, "{}/3".format(icon_var), 3*PL/4-cell, PH/2, True, blanc)
    aff_image(screen,icon_pic, PL/2+cell*2, PH/2, cell*0.8, cell*0.8, True)


    music_min_button = pygame.Rect(1*PL/4+cell*2-cell*0.75/2, PH/2+cell*1.5-cell*0.75/2, cell*0.75, cell*0.75)
    music_plus_button = pygame.Rect(1*PL/4+cell*3-cell*0.75/2, PH/2+cell*1.5-cell*0.75/2, cell*0.75, cell*0.75)
    basic_button(screen, 1*PL/4, PH/2+cell*1.5, 4*PL/10, cell, noir, True)

    basic_text(police2, "MUSIQUE   ,", 1*PL/4-cell*2, PH/2+cell*1.5, True, blanc)
    basic_text(police2, "{:.0f}%".format(s_music*100), 1*PL/4+cell*0.5, PH/2+cell*1.5, True, blanc)

    basic_button(screen, 1*PL/4+cell*2, PH/2+cell*1.5, cell*0.75, cell*0.75, blanc, True)
    basic_text(police, "-", 1*PL/4+cell*2, PH/2+cell*1.5, True, noir)

    basic_button(screen, 1*PL/4+cell*3, PH/2+cell*1.5, cell*0.75, cell*0.75, blanc, True)
    basic_text(police, "+", 1*PL/4+cell*3, PH/2+cell*1.5, True, noir)

    sfx_min_button = pygame.Rect(3*PL/4+cell*2-cell*0.75/2, PH/2+cell*1.5-cell*0.75/2, cell*0.75, cell*0.75)
    sfx_plus_button = pygame.Rect(3*PL/4+cell*3-cell*0.75/2, PH/2+cell*1.5-cell*0.75/2, cell*0.75, cell*0.75)
    basic_button(screen, 3*PL/4, PH/2+cell*1.5, 4*PL/10, cell, noir, True)

    basic_text(police2, "SFX   ,", 3*PL/4-cell*2, PH/2+cell*1.5, True, blanc)
    basic_text(police2, "{:.0f}%".format(s_sfx*100), 3*PL/4+cell*0.5, PH/2+cell*1.5, True, blanc)

    basic_button(screen, 3*PL/4+cell*2, PH/2+cell*1.5, cell*0.75, cell*0.75, blanc, True)
    basic_text(police, "-", 3*PL/4+cell*2, PH/2+cell*1.5, True, noir)

    basic_button(screen, 3*PL/4+cell*3, PH/2+cell*1.5, cell*0.75, cell*0.75, blanc, True)
    basic_text(police, "+", 3*PL/4+cell*3, PH/2+cell*1.5, True, noir)

    # Boucle des options
    while etat == "OPTIONS":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if retour_button.collidepoint(event.pos):
                        etat = "ACCUEIL"
                    if couleur_button.collidepoint(event.pos):
                        if coul_var == 5:
                            coul_var = 0
                        if coul_var == 0:
                            background_img = background_vert
                            var_text = "VERT"
                        if coul_var == 1:
                            background_img = background_bleu
                            var_text = "BLEU"
                        if coul_var == 2:
                            background_img = background_rose
                            var_text = "ROSE"
                        if coul_var == 3:
                            background_img = background_rouge
                            var_text = "ROUGE"
                        if coul_var == 4:
                            background_img = background_jaune
                            var_text = "JAUNE"
                        coul_var+=1
                        sauvegarder_donnees()

                    if icon_button.collidepoint(event.pos):
                        if icon_var ==3:
                            icon_var =0
                            
                        if icon_var == 0:
                            choix_pic = Pic1
                            icon_text = "JOUEUR"
                            icon_pic = "assets/icons/default.png"
                            
                        if icon_var == 1 :
                            choix_pic = Pic2
                            icon_text = "PESSI"
                            icon_pic = "assets/icons/pessi.png"
                            
                        if icon_var == 2 :
                            choix_pic = Pic3
                            icon_text = "JOYEUX"
                            icon_pic = "assets/icons/happy.png"
                            
                        icon_var+=1
                        sauvegarder_donnees()

                    
                    if music_min_button.collidepoint(event.pos):
                        if s_music > 0.04 :
                            s_music -= 0.05
                            pygame.mixer.music.set_volume(s_music)
                            sauvegarder_donnees()

                    if music_plus_button.collidepoint(event.pos):
                        if s_music <= 1 :
                            s_music += 0.05
                            pygame.mixer.music.set_volume(s_music)
                            sauvegarder_donnees()
                    
                    if sfx_min_button.collidepoint(event.pos):
                        if s_sfx > 0.04 :
                            s_sfx -= 0.05
                            sfx_sound(s_sfx)
                            sauvegarder_donnees()

                    if sfx_plus_button.collidepoint(event.pos):
                        if s_sfx <= 1 :
                            s_sfx += 0.05
                            sfx_sound(s_sfx)
                            sauvegarder_donnees()
                        

                    afficher_options()
                    pygame.display.flip()
                        

        # Maj écran
        pygame.display.flip()

#-------------------- CONTROLES -------------------------

key_var = 1
name_key_var = "TOUCHES"

def afficher_ctrl():
    global etat
    global background_img
    global police, police2, police3, police4

    global KeyZ, KeyQ, KeyS, KeyD
    global KeyVarUp, KeyVarDown, KeyVarLeft, KeyVarRight
    global key_var, name_key_var

    # Affichage du fond
    screen.blit(background_img, (0, 0))
    
    # Titre page aide
    basic_text(police, "CONTROLES", PL/2, cell*1.5, True, blanc)

    # Bouton retour
    retour_button = pygame.Rect(PL/2-cell*2, PH-cell*2, cell*4, cell)
    basic_button(screen, PL/2, PH-cell*1.5, cell*4, cell, noir, True)
    basic_text(police, "RETOUR", PL/2, PH-cell*1.5, True, blanc)

    
    basic_button(screen, PL/2, PH/4+cell*0.75, cell*3, cell*0.75, noir, True)
    basic_text(police3, "MODIFIER", PL/2, PH/4+cell*0.75, True, blanc)

    edit_key_button = pygame.Rect(PL/2-cell*1.5, PH/4+cell*(0.75/2), cell*3, cell*0.75)

    basic_button(screen, PL/2, PH/4, cell*6, cell, noir, True)
    basic_text(police, name_key_var, PL/2, PH/4, True, blanc)

    basic_button(screen, PL/2-3*cell, PH/2, cell*2, cell, noir, True)
    basic_button(screen, PL/2-1*cell, PH/2, cell*2, cell, noir, True)
    basic_button(screen, PL/2+1*cell, PH/2, cell*2, cell, noir, True)
    basic_button(screen, PL/2+3*cell, PH/2, cell*2, cell, noir, True)

    basic_text(police2, "HAUT", PL/2-3*cell, PH/2, True, blanc)
    basic_text(police2, "GAUCHE", PL/2-1*cell, PH/2, True, blanc)
    basic_text(police2, "BAS", PL/2+1*cell, PH/2, True, blanc)
    basic_text(police2, "DROITE", PL/2+3*cell, PH/2, True, blanc)


    basic_button(screen, PL/2-3*cell, PH/2+cell, cell*1.25 ,cell*0.75, noir, True)
    basic_button(screen, PL/2-1*cell, PH/2+cell, cell*1.25 ,cell*0.75, noir, True)
    basic_button(screen, PL/2+1*cell, PH/2+cell, cell*1.25 ,cell*0.75, noir, True)
    basic_button(screen, PL/2+3*cell, PH/2+cell, cell*1.25 ,cell*0.75, noir, True)

    basic_text(police2, "{}".format(KeyVarUp), PL/2-3*cell, PH/2+cell, True, blanc)
    basic_text(police2, "{}".format(KeyVarLeft), PL/2-1*cell, PH/2+cell, True, blanc)
    basic_text(police2, "{}".format(KeyVarDown), PL/2+1*cell, PH/2+cell, True, blanc)
    basic_text(police2, "{}".format(KeyVarRight), PL/2+3*cell, PH/2+cell, True, blanc)

    

    # Boucle des options
    while etat == "CTRL":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if retour_button.collidepoint(event.pos):
                        etat = "ACCUEIL"
                    if edit_key_button.collidepoint(event.pos):
                        if key_var ==3:
                            key_var =1
                        if key_var == 1:
                            KeyZ = pygame.K_UP
                            KeyQ = pygame.K_LEFT
                            KeyS = pygame.K_DOWN
                            KeyD = pygame.K_RIGHT

                            KeyVarUp = ":"
                            KeyVarLeft = ";"
                            KeyVarDown = "!"
                            KeyVarRight = ","

                            name_key_var = "FLECHES"

                        if key_var == 2:
                            KeyZ = pygame.K_z
                            KeyQ = pygame.K_q
                            KeyS = pygame.K_s
                            KeyD = pygame.K_d

                            KeyVarUp = "Z"
                            KeyVarLeft = "Q"
                            KeyVarDown = "S"
                            KeyVarRight = "D"

                            name_key_var = "TOUCHES"

                        key_var +=1

                        afficher_ctrl()
                        pygame.display.flip()

        # Maj écran
        pygame.display.flip()

#-------------------- STATISTIQUES -------------------------

def afficher_stats():
    global etat
    global background_img
    global police, police2, police3, police4

    # Affichage du fond
    screen.blit(background_img, (0, 0))

    # Titre page aide
    basic_button(screen, PL/2, cell*1.5, cell*5, cell, noir, True)
    basic_text(police, "STATISTIQUES", PL/2, cell*1.5, True, blanc)

    # Bouton retour
    retour_button = pygame.Rect(PL/2-cell*2, PH-cell*2, cell*4, cell)
    basic_button(screen, PL/2, PH-cell*1.5, cell*4, cell, noir, True)
    basic_text(police, "RETOUR", PL/2, PH-cell*1.5, True, blanc)

    basic_button(screen, 1*PL/3, PH/2-cell*2, cell*4, cell, noir, True)
    basic_button(screen, 1*PL/3, PH/2-cell*2.5, cell*3, cell*0.33, noir, True)
    basic_text(police3, "NIVEAU(X) COMPLETÉ(S)", 1*PL/3, PH/2-cell*2.5, True, bleu)
    basic_text(police2, "{}".format(total_level), 1*PL/3, PH/2-cell*2, True, blanc)

    basic_button(screen, 2*PL/3, PH/2-cell*2, cell*4, cell, noir, True)
    basic_button(screen, 2*PL/3, PH/2-cell*2.5, cell*2, cell*0.33, noir, True)
    basic_text(police3, "PIÈCES", 2*PL/3, PH/2-cell*2.5, True, jaune)
    basic_text(police2, "{}".format(total_pieces), 2*PL/3, PH/2-cell*2, True, blanc)


    basic_button(screen, 1*PL/4, PH/2, cell*4, cell, noir, True)
    basic_button(screen, 1*PL/4, PH/2-cell*0.5, cell*3, cell*0.33, noir, True)
    basic_text(police3, "VICTOIRE", 1*PL/4, PH/2-cell*0.5, True, vert)
    basic_text(police2, "{}".format(win), 1*PL/4, PH/2, True, blanc)

    basic_button(screen, 2*PL/4, PH/2, cell*4, cell, noir, True)
    basic_button(screen, 2*PL/4, PH/2-cell*0.5, cell*3, cell*0.33, noir, True)
    basic_text(police3, "FORFAIT", 2*PL/4, PH/2-cell*0.5, True, gris)
    basic_text(police2, "{}".format(forfait), 2*PL/4, PH/2, True, blanc)

    basic_button(screen, 3*PL/4, PH/2, cell*4, cell, noir, True)
    basic_button(screen, 3*PL/4, PH/2-cell*0.5, cell*3, cell*0.33, noir, True)
    basic_text(police3, "DÉFAITE", 3*PL/4, PH/2-cell*0.5, True, rouge)
    basic_text(police2, "{}".format(lose), 3*PL/4, PH/2, True, blanc)

    basic_button(screen, 1*PL/3, PH/2+cell*2, cell*4, cell, noir, True)
    basic_button(screen, 1*PL/3, PH/2+cell*1.5, cell*3, cell*0.33, noir, True)
    basic_text(police3, "TEMPS DE JEU", 1*PL/3, PH/2+cell*1.5, True, blanc)
    basic_text(police2, "{:.0f} min".format(played_time), 1*PL/3, PH/2+cell*2, True, blanc)




    while etat == "STATS":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if retour_button.collidepoint(event.pos):  
                        etat = "ACCUEIL"

        pygame.display.flip()

#---------------------- ECRAN DE FIN --------------------


def afficher_ecran_fin():
    global screen
    global score 
    global lvl
    global etat
    global WIN
    global total_time
    
    # affichage du fond et re-importation de la police
    screen.blit(background_img, (0, 0))

    # Bouton retour
    retour_button = pygame.Rect(PL/2-cell*2, PH-cell*2, cell*4, cell)
    basic_button(screen, PL/2, PH-cell*1.5, cell*4, cell, noir, True)
    basic_text(police, "RETOUR", PL/2, PH-cell*1.5, True, blanc)


    basic_button(screen, PL/2, cell*2, cell*6, cell*2, noir, True)

    # définition du texte fin de jeu
    if WIN == True:
        basic_text(police, "VICTOIRE", PL/2, cell*2, True, vert)
        
    else :
        basic_text(police, "DEFAITE", PL/2, cell*2, True, rouge)


    basic_button(screen, PL/4, PH/2, cell*4, cell*2, noir, True)
    basic_button(screen, PL/2, PH/2, cell*4, cell*2, noir, True)
    basic_button(screen, 3*PL/4, PH/2, cell*4, cell*2, noir, True)

    aff_image(screen, "assets/argent.png", PL/4-cell*1.8, PH/2-cell*0.9, cell*0.7, cell*0.7, False)
    aff_image(screen, "assets/clock.png", PL/2-cell*1.8, PH/2-cell*0.9, cell*0.7, cell*0.7, False)
    aff_image(screen, "assets/level.png", 3*PL/4-cell*1.8, PH/2-cell*0.9, cell*0.7, cell*0.7, False)

    Argms_text(police, PL/4, PH/2, score, blanc, True)
    if score>1:
        basic_text(police2, "EUROS", 1*PL/4, PH/2+cell*0.5, True, blanc)
    else:
        basic_text(police2, "EURO", 1*PL/4, PH/2+cell*0.5, True, blanc)

    if WIN==True:
        Clock_Argms_text(police, PL/2, PH/2, total_time, blanc, True)
        basic_text(police2, "SECONDES", PL/2, PH/2+cell*0.5, True, blanc)
    else:
        basic_text(police, "NON", PL/2, PH/2, True, blanc)
        basic_text(police2, "TERMINER", PL/2, PH/2+cell*0.5, True, blanc)
    

    advance_text(police, 3*PL/4, PH/2, lvl, nombre_niv, True)
    if lvl>1:
        basic_text(police2, "NIVEAUX", 3*PL/4, PH/2+cell*0.5, True, blanc)
    else:
        basic_text(police2, "NIVEAU", 3*PL/4, PH/2+cell*0.5, True, blanc)

    pygame.display.flip()

    # Boucle pour rester sur l'écran de fin
    while etat == "FIN":
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retour_button.collidepoint(event.pos):
                    etat = "ACCUEIL"
                    pygame.display.flip()



#-------------------- LANCER LE JEU -------------------------

charger_donnees()
x = 0
while True:



    pygame.mixer.Sound.play(son_click)


    x += clock.tick(60) / 1000
    if x>60:
        played_time += ((x-x%60)/60)
        x=x%60
        sauvegarder_donnees()



    elif etat == "ACCUEIL":
        afficher_page_accueil()

    elif etat == "JEU":
        lancer_jeu()

    elif etat == "BOUTIQUE":
        afficher_page_boutique()

    elif etat == "OPTIONS":
        afficher_options()
        

    elif etat == "STATS":
        afficher_stats()

    elif etat == "CTRL":
        afficher_ctrl()

    elif etat == "FIN":
        afficher_ecran_fin()

    elif etat =="BOSS":
        afficher_boss()

    elif etat =="QUITTER":
        break


