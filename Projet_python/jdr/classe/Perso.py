class Perso:
    #Constructeur
    def __init__(self):
        """
        Constructeur de la classe mère Perso
        attribut:
            - Nom UNIQUE ET VALIDE
            - HP, MP, XP, LVL

        """
        print("création d'un personnage")
        self.nomPerso="default"
        self.hp=0
        self.mp=0
        self.xp=0
        self.lvl=0
        

    def direBonjour(self):
        print("Salut, je m'appelle",self.nomPerso)
    





