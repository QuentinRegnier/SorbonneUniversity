# Quentin Régnier
# Garv Shaan Darmesh

import random

# Exercice 1: Cadavre exquis basique
# Question 1:
def sujet(n: int)->str:
    """Précondition: n>=1 and n<=6
    renvoie pour chaque nombre une chaine de caractères différente, correspondant à un         sujet possible d’une phrase"""
    if n==1 :
        return "Dagobert"
    elif n==2 :
        return "Quentin"
    elif n==3 :
        return "Garv"
    elif n==4 :
        return  "Louis"
    elif n==5 :
        return "Martial"
    elif n==6 :
        return "Kévin"
assert sujet(1) == "Dagobert"
assert sujet(5) == "Martial"

# Question 2:
def verbe(n: int)->str:
    """Précondition: n>=1 and n<=6
    renvoie pour chaque nombre une chaine de caractères différente, correspondant à un         verbe possible d’une phrase"""
    if n==1 :
        return "regarde"
    elif n==2 :
        return "dors"
    elif n==3 :
        return "s'étalle"
    elif n==4 :
        return "vole"
    elif n==5 :
        return "détruit"
    elif n==6 :
        return "saute"
assert verbe(1) == "regarde"
assert verbe(5) == "détruit"

def cod(n: int)->str:
    """Précondition: n>=1 and n<=6
    renvoie pour chaque nombre une chaine de caractères différente, correspondant à un        complément d'objet direct possible d’une phrase"""
    if n==1 :
        return "un collier"
    elif n==2 :
        return "une clef"
    elif n==3 :
        return "un vase"
    elif n==4 :
        return "une figurine en bois"
    elif n==5 :
        return "une photographie"
    elif n==6 :
        return "une montre"
assert cod(1) == "un collier"
assert cod(5) == "une photographie"

def lieu(n: int)->str:
    """Précondition: n>=1 and n<=6
    renvoie pour chaque nombre une chaine de caractères différente, correspondant à un         complément circonstanciel de lieu possible d’une phrase"""
    if n==1 :
        return "derrière la statue"
    elif n==2 :
        return "sur le sol"
    elif n==3 :
        return "dans le coin de la salle"
    elif n==4 :
        return  "sur la chaise"
    elif n==5 :
        return "sur la table"
    elif n==6 :
        return "contre le mûr"
assert lieu(1) == "derrière la statue"
assert lieu(5) == "sur la table"

# Question 3:
def phrase(a: int, b: int, c: int, d: int)->str:
    """Précondition: a>0 and a<=6 and b>0 and b<=6 and c>=0 and c<=6 and d>0 and d<=6
    la fonction phrase qui prend en entrée quatre entiers compris entre 1 et 6, et qui
    compose une phrase dont le sujet est donné par la fonction sujet appliqué au premier entier, le verbe par la fonction verbe appliqué au deuxième entier, le complément d'objet     direct par la fonction cod appliqué au troisième entien et le complément circonstanciel     de lieu par la fonction lieu appliqué au quatrième entier"""
    return sujet(a)+" "+verbe(b)+" "+cod(c)+" "+lieu(d)
assert phrase(1,1,1,1) == "Dagobert regarde un collier derrière la statue"
assert phrase(5,5,5,5) == "Martial détruit une photographie sur la table"

# Question 4:
def de6()->int:
    """ Génère un nombre aléatoir entre 1 à 6"""
    return int(6*random.random())+1
    

# Question 5:
# Comme ce programme est un test aléatoire donc on pourra pas effectuer des tests prévisible
def phrase_aléatoire()->str:
    """la fonction phrase_aléatoire génère une phrase aléatoire"""
    return phrase(de6(),de6(),de6(),de6())

# Exercice 3:
def phrase2(a: int, b: int, c: int, d: int)->str:
    """Précondition: a>0 and a<=6 and b>0 and b<=6 and c>=0 and c<=6 and d>0 and d<=6
    la fonction phrase qui prend en entrée quatre entiers compris entre 1 et 6, et qui
    compose une phrase dont le sujet est donné par la fonction sujet appliqué au premier en     tier, le verbe par la fonction verbe appliqué au deuxième entier, le complément d'objet     direct par la fonction cod appliqué au troisième entien et le complément circonstanciel     de lieu par la fonction lieu appliqué au quatrième entier"""
    if c==0 :
        return sujet(a)+" "+verbe(b)+" "+lieu(d)
    else :
        return sujet(a)+" "+verbe(b)+" "+cod(c)+" "+lieu(d)
assert phrase2(1,1,1,1) == "Dagobert regarde un collier derrière la statue"
assert phrase2(5,5,5,5) == "Martial détruit une photographie sur la table"
assert phrase2(5,2,0,5) == "Martial dors sur la table"

def phrase_aléatoire2()->str:
    """la fonction phrase_aléatoire génère une phrase aléatoire"""
    a:int=de6()
    b:int=de6()
    c:int=de6()
    d:int=de6()
    if b==2 or b==3 or b==6 :
        return phrase2(a,b,0,d)
    else:
        return phrase2(a,b,c,d)

# Exercice 4:
def phrase_aléatoire3(personnage:int)->str:
    """la fonction phrase_aléatoire génère une phrase aléatoire"""
    a:int=personnage
    b:int=de6()
    c:int=de6()
    d:int=de6()
    if b==2 or b==3 or b==6 :
        return phrase2(a,b,0,d)
    else:
        return phrase2(a,b,c,d)

def den(n:int)->int:
    """ Génère un nombre aléatoir entre 1 à n"""
    return int(n*random.random())+1

def ldevlh(n: int, etat_objet: int, etat_personnage: int, interaction :int, personnage_avant :int, objet_avant :int) -> None:
    """Précondition: n > 0
    Génère une description d'une salle avec un personnage et un objet s'ils ne sont pas encore rencontrés.
    Retourne la description, l'état de l'objet et l'état du personnage."""
    
    personnage_id:int = de6()
    personnage:str = str(sujet(personnage_id))
    personnage_avant_str:str
    objet_id:int = de6()
    objet:str = str(cod(objet_id))
    objet_avant_str:str
    lieux:str = str(lieu(de6()))
    prochaine_salle:int = den(de6()*de6())
    prochaine_salle2:int = den(de6()*de6())
    description:str = ""
    fin:int = de6()
    personnage_cmd:int
    objet_cmd:int
    etat_personnages:int
    etat_objets:int
    start_str:int= de6()
    action_var_choice:int
    if  personnage_avant > 0 and objet_avant > 0 :
        personnage_avant_str = str(sujet(personnage_avant))
        objet_avant_str = str(cod(objet_avant))
    if interaction == 0:
        description = "BIENVENUE dans le Donjon."
    elif interaction == 1:
        description = "Vous êtes dans la salle " + str(n) + "."
    
    if start_str == 1:
        description = description + " Vous entrez dans une grande pièce aux murs humides. La lumière est faible."
    elif start_str == 2:
        description = description + " La salle semble plus petite, des toiles d'araignées pendent des coins."
    elif start_str == 3:
        description = description + " Le sol est recouvert de poussière, et il y a des traces de pas anciennes."
    elif start_str == 4:
        description = description + " Vous remarquez une grande porte ornée de symboles mystérieux."
    elif start_str == 5:
        description = description + " Un écho résonne dans la pièce, comme si quelque chose vous suivait."
    elif start_str == 6:
        description = description + " La salle est plongée dans le noir, seule une petite torche éclaire le chemin."

    if etat_personnage == 0:
        description = description + " " + personnage + " apparaît soudainement et semble ne pas vouloir vous parler."
        personnage_cmd = personnage_id
        action_var_choice = personnage_id
        etat_personnages = 1
    elif etat_personnage == 1 and interaction % 2 == 0:
        description = description + " " + personnage_avant_str + " disparaît soudainement."
        description = description + " " + personnage + " apparaît soudainement et semble ne pas vouloir vous parler."
        etat_personnages = 1
        personnage_cmd = personnage_id
        action_var_choice = personnage_id
    elif etat_personnage == 1 and interaction % 2 != 0:
        description = description + " " + personnage_avant_str + " semble étrange et porte du desintérêt pour vous."
        personnage_cmd = personnage_avant
        action_var_choice = personnage_avant
        etat_personnages = 1

    description = description + " " + phrase_aléatoire3(action_var_choice) + "."

    if etat_objet == 0:
        description = description + " Vous trouvez " + objet + " " + lieux + "."
        objet_cmd = objet_id
        etat_objets = 1
    elif etat_objet == 1 and interaction % 2 != 0:
        description = description + " L'objet " + objet_avant_str + " que vous aviez trouvé semble avoir disparu."
        description = description + " Vous trouvez un nouvel objet: " + objet + " " + lieux + "."
        objet_cmd = objet_id
        etat_objets = 1
    elif etat_objet == 1 and interaction % 2 == 0:
        description = description + " L'objet " + objet_avant_str + " que vous aviez trouvé semble être intact et toujours là."
        objet_cmd = objet_avant
        etat_objets = 1
    
    if prochaine_salle == n:
        prochaine_salle = (n % 6) + 1
    if prochaine_salle2 == n or prochaine_salle2 == prochaine_salle :
        prochaine_salle2 = (n % 6) + 1

    print(description)

    if fin == 6 and interaction > 4 :
        print(" Vous avez atteint la fin de l'histoire.")
    elif fin == 1 or fin == 2 or fin == 3 :
        print(" Vous pouvez aller dans la salle " + str(prochaine_salle) + ".")
        print("Utiliser la fonction suivante pour aller dans la salle " + str(prochaine_salle) + "  : ldevlh(" + str(prochaine_salle) + ", " + str(etat_objets) + ", " + str(etat_personnages) + ", " + str(interaction + 1) + ", " + str(personnage_cmd) + ", " + str(objet_cmd) + ")")
    else :
        print(" Vous pouvez aller dans la salle " + str(prochaine_salle) + " ou aller dans la salle " + str(prochaine_salle2) + ".")
        print("Utiliser la fonction suivante pour aller dans la salle " + str(prochaine_salle) + " : ldevlh(" + str(prochaine_salle) + ", " + str(etat_objets) + ", " + str(etat_personnages) + ", " + str(interaction + 1) + ", " + str(personnage_cmd) + ", " + str(objet_cmd) + ")")
        print("Utiliser la fonction suivante pour aller dans la salle " + str(prochaine_salle2) + " : ldevlh(" + str(prochaine_salle2) + ", " + str(etat_objets) + ", " + str(etat_personnages) + ", " + str(interaction + 1) + ", " + str(personnage_cmd) + ", " + str(objet_cmd) + ")")

def start_story()->None :
    """Lance la fonction ldevlh qui créer une histoire à choix multiple ou non avec les variables standart d'initialisation"""
    return ldevlh(1, 0, 0, 0, 0, 0)
