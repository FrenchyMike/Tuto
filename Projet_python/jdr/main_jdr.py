"""
Objectifs:
    1-Menu de selection:
        1.1-Créer un perso
        1.2-Jouer un perso existant


Tech:
    1-Menu de selection:
        while
        input

    1.1-Créer un perso:
        Nom valide (string) e UNIQUE -> toLowerCase
        Sexe (char) > H ou F
        Type: Hériter de la classe Perso:
            Mage
            Guerrier
        Le rentrer dans un JSON -> Dico
    
    1.2-Jouer un perso existant:
        Afficher liste
        Choisir un perso à partir de son nom
"""
from fonction.menu import *
from classe.Perso import *
centrer("")
centrer("Bienvenue dans la jeu des bidous")
centrer("")
br()
choixUser1=affichageMenu1()
persoTest = Perso()
persoTest.nomPerso=input("Votre nom ?")
persoTest.direBonjour()

