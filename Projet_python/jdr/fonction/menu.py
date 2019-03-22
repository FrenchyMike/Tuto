"""
Module qui va gérer les menus de selections
"""

def centrer(string):
    """Fonction qui centre un str, pour les menus
    prend un string en paramètre
    retourne un string
    """
    string=str(string)
    string=string.center(50,"=")
    print(string)

def affichageMenu1():
    """
    Fais entrer le user dans une boucle
    retourne :
        -1 :Créer perso
        OU
        -2 :Jouer avec un perso
    """
    while(True):
        centrer("Menu de selection")
        print("tapez 1 pour créer personnage")
        print("tapez pour selectionner un personnage existant")
        print("Q pour quitter")
        userSelec=input("> ")
        userSelec=str(userSelec)
        if userSelec=="q" or "Q":
            break
        elif userSelec=="1" or userSelec =="2":
            return userSelec
            break
        else:
            input(userSelec+" n'est pas une entrée valide!\nSelectionner 1 ou 2 (tapez pour continuer)")
            continue

def br():
    print("\n")