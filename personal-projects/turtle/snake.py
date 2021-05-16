# modules nécessaires
import turtle
import time
import random

# variables utiles
delai = 0.5
largeur = 800
hauteur = 600
taille_case = 40
cases_horizontales = int(largeur / taille_case)
cases_verticales = int(hauteur / taille_case)

# fenêtre
fenetre = turtle.Screen()
fenetre.title('Snake')
fenetre.bgcolor('black')
fenetre.setup(width=largeur, height=hauteur)
fenetre.tracer(0)

# tete du serpent
tete = turtle.Turtle()
tete.speed = 0
tete.shape('square')
tete.color('white')
tete.penup()
tete.goto(0, 0)
tete.direction = 'stop'

# nourriture
nourriture= turtle.Turtle()
nourriture.speed(0)
nourriture.shape('square')
nourriture.color('green')
nourriture.penup()
nourriture.goto(
    random.randrange(-cases_horizontales / 2, cases_horizontales / 2) * taille_case,
    random.randrange(-int(cases_verticales / 2), int(cases_verticales / 2)) * taille_case
    )

# queue
segments = []


# fonctions
def monter():
    if tete.direction != 'bas':
        tete.direction = 'haut'
        
        
def descendre():
    if tete.direction != 'haut':
        tete.direction = 'bas'
        
        
def aller_a_gauche():
    if tete.direction != 'droite':
        tete.direction = 'gauche'
        
        
def aller_a_droite():
    if tete.direction != 'gauche':
        tete.direction = 'droite'
        
        
def move():
    if tete.direction == 'haut':
        y = tete.ycor()
        tete.sety(y + taille_case)
    if tete.direction == 'bas':
        y = tete.ycor()
        tete.sety(y - taille_case)
    if tete.direction == 'gauche':
        x = tete.xcor()
        tete.setx(x - taille_case)
    if tete.direction == 'droite':
        x = tete.xcor()
        tete.setx(x + taille_case)
        

# gestion des contrôles (clavier AZERTY)
fenetre.listen()
fenetre.onkeypress(monter, 'z')
fenetre.onkeypress(descendre, 's')
fenetre.onkeypress(aller_a_gauche, 'q')
fenetre.onkeypress(aller_a_droite, 'd')

# boucle principale
while True:
    fenetre.update()

    # vérification de collision avec les bords
    if tete.xcor() > largeur / 2 or tete.xcor() < -largeur / 2 or tete.ycor() > hauteur / 2 or tete.ycor() < -hauteur / 2:
        time.sleep(1)
        tete.goto(0, 0)
        tete.direction = 'stop'

        # effacer les segments
        segments.clear()

        # réinitilialisation du delai
        delai = 0.5

    # vérifier la collision avec la nourriture
    if tete.distance(nourriture) < 20:
        # déplacer la nourriture nourriture à un endroit aléatoire
        nourriture.goto(
            random.randrange(-cases_horizontales / 2, cases_horizontales / 2) * taille_case,
            random.randrange(-int(cases_verticales / 2), int(cases_verticales / 2)) * taille_case
            )

        # ajouter un nouveau segment à la tête
        nouveau_segment = turtle.Turtle()
        nouveau_segment.speed(0)
        nouveau_segment.shape('square')
        nouveau_segment.color('gray')
        nouveau_segment.penup()
        segments.append(nouveau_segment)

        # réduit le délai
        delai -= 0.001 

    # déplace les segments dans l'ordre inverse
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # déplace le segment 0 sur la tête
    if len(segments) > 0:
        x = tete.xcor()
        y = tete.ycor()
        segments[0].goto(x, y)

    move()

    # vérification de collision avec le corps du serpent
    for segment in segments:
        if segment.distance(tete) < 20:
            time.sleep(1)
            tete.goto(0, 0)
            tete.direction = 'stop'

            segments.clear()
            delai = 0.5

    time.sleep(delai)
    
fenetre.mainloop()
