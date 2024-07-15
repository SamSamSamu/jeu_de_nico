from kandinsky import *
import time
import keyboard

from random import randint

def afficher_grille(grille):
    longueur = int(320/len(grille[0]))
    largeur = int(222/len(grille))
    haut_x= 0
    haut_y= 0
    bas_x= longueur
    bas_y= largeur
    # print('longueur: ', longueur)
    
    # print('largeur: ', largeur)

    for ligne in grille:
        for case in ligne:
            fill_rect(haut_x, haut_y, bas_x, bas_y, case)
            haut_x += longueur
        haut_x =0
        haut_y += largeur
        
    for i in range(1,len(grille[0])):
        fill_rect((i*longueur)-1,0,1, 222, (115,115,115))
    for i in range(1, len(grille)):
        fill_rect(0,(i*largeur)-1,320,1, (115,115,115))

        


def creerGrille(nombreColonnes, nombreLignes):
 grid = [[]] * nombreLignes
 for ligne in range(nombreLignes):
    grid[ligne] = [(255, 255, 255)] * nombreColonnes
 return grid

class snake():
    def __init__(self, head_position):
        self.body = [head_position, [head_position[0],head_position[1]-1], [head_position[0],head_position[1]-2]]
        self.len = 3
        self.direction = 's'
        print("head_x", head_position[0])
        print("head_y", head_position[1])
        self.direction_interdite = 'z'
        
    def ajouter_snake(self):
        grille[self.body[0][1]][self.body[0][0]] = (255, 0, 0)
        for case in self.body[1:]:
            grille[case[1]][case[0]] = (200,0,50)
            print(case[1], case[0])
        
    def deplacer(self):
        rep = obtenir_rep_user()
        if rep != self.direction or not rep != self.direction_interdite:
            self.direction = rep
        for i in range(-1, (-len(self.body))+1, -1):
            self.body[i] = self.body[i-1]          
        if self.direction == 'z':
            self.body[0]= [self.body[0][0], self.body[0][1]-1]
        if self.direction == 's':
            self.body[0]= [self.body[0][0], self.body[0][1]+1]
        if self.direction == 'q':
            self.body[0]= [self.body[0][0]-1, self.body[0][1]]
        if self.direction == 'd':
            self.body[0]= [self.body[0][0]+1, self.body[0][1]]
        
        
        self.ajouter_snake()


def obtenir_rep_user():
        moment_1 = time.time()
        while time.time()- moment_1<2:
            if keyboard.read_key() in ('z','q', 's', 'd'):
                choix = keyboard.read_key()
        return choix    

# grille = creerGrille(int(input('nb ligne: ')), int(input('nb_colonne')))
grille = creerGrille(12,10)     
S = snake([4,5])  
S.ajouter_snake()
for i in range(5):
    afficher_grille(grille)
    S.deplacer()
    afficher_grille(grille)