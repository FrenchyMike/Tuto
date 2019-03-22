import json

perso = \
    {\
        "joueur":"3","points":"25"\
    }
    
with open("liste_perso/liste_perso.json","w") as fichier:
    json.dump(perso, fichier)