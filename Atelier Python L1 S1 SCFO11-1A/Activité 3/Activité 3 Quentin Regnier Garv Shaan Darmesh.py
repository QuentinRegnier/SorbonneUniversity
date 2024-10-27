# Quentin Regnier
# Garv Shaan Darmesh
# Exercice 1:
# Question 1:
def divise(k : int , n : int) -> bool :
    """ Pre : k > 0 and n >= 0
    Decide si k divise n """
    return n % k == 0
assert divise(5,25)==True
assert divise(3,9)==True
assert divise(9,27)==True
assert divise(19,2)==False

def est_parfait (n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
    return n == s
assert est_parfait(6)==True
assert est_parfait(9)==False
assert est_parfait(8)==False

# Question 2:
def est_parfait_simulee (n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    print("=== Evaluation of : 'est_parfait_simulee("+str(n)+")' ===")
    print('début de boucle, s = '+str(s))
    print('début de boucle, i = '+str(i))
    print('====================')
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
        print('fin du tour 1 , s = '+str(s))
        print('fin du tour 1 , i = '+str(i))
        print('====================')
    print('sortie de boucle, s = '+ str(s) + ' et n = ' +str(n))
    print(n == s)
    return n == s
assert est_parfait_simulee(6)==True
assert est_parfait_simulee(9)==False
assert est_parfait_simulee(4)==False
# Exercice 2:
def test_parfait(n:int)->bool:
    """Précondition: n>=1 ans n<=137438691328
    vérifie si est parfait(k) est vrai si et seulement si le nombre k apparait dans la list     e."""
    i:int
    verification:bool
    for i in range(1,n+1):
        verification= i==6 or i==28 or i==496 or i==8128 or i==33550336 or i==8589869096 or i==137438691328
        if est_parfait(i)!=verification :
            return False
    return True
assert test_parfait(40)==True
assert test_parfait(2005)==True
assert test_parfait(14203)==True

# Exercice 3:

# Question 2 :
def invariant(i:int,n:int,s:int, prev_s:int)->bool:
    """Précondition : n>0 and i>0 and s>=0
    Vérifie si l'invariant est vrai pour n,i,s donné"""
    if divise(i,n):
        return s == prev_s + i
    else :
        return s == prev_s
assert invariant(2,6,3,1) == True
assert invariant(3,6,6,3) == True
assert invariant(4,5,6,3) == False

def est_parfait_invariant (n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    prev_s:int=0
    i : int = 1
    print("=== Evaluation of : 'est_parfait_2("+str(n)+")' ===")
    while i != n :
        if divise(i, n):
            s = s + i
        print("The Invariant is " + str(invariant(i,n,s,prev_s)))
        i = i + 1
        prev_s = s
    return n == s
assert est_parfait_invariant(6)==True
assert est_parfait_invariant(9)==False
assert est_parfait_invariant(8)==False

# Question 4 :
# Itérations pour n = 6 avec l'évolution de i et s
# On justifie à chaque étape.
#
#| Itération | i  | Diviseur de n ? | s | s_prev | Invariant                                                      | i | s_prev |
#|-----------|----|-----------------|---|--------|----------------------------------------------------------------|---|--------|
#| Départ 1  | 1  | Oui             | 1 | 0      | 1 est diviseur de 6  et s = s_prev + i <=> 1 = 0 + 1 donc True | 2 | 2      |
#| 2         | 2  | Oui             | 3 | 1      | 2 est diviseur de 6  et s = s_prev + i <=> 3 = 1 + 2 donc True | 3 | 1      |
#| 3         | 3  | Oui             | 6 | 3      | 3 est diviseur de 6  et s = s_prev + i <=> 6 = 3 + 3 donc True | 4 | 3      |
#| 4         | 4  | Non             | 6 | 6      | 4 n'est pas diviseur de 6  et s = s_prev <=> 6 = 6 donc True   | 5 | 6      |
#| 5         | 5  | Non             | 6 | 6      | 5 n'est pas diviseur de 6  et s = s_prev <=> 6 = 6 donc True   | 6 | 6      |
#| Fin 6     | 6  | --------------- | 6 | ------ | -------------------------------------------------------------- | - | ------ |
#
#Donc on a prouver que l'invariant de boucle est vrai pour le cas n=6

# Exercice 4 :
# Question 1 :
# Le fichier se trouve dans MrPython-master/mrpython de plus j'ai mis a au lieu de w sinon les assert n'on aucun intérêt
def est_parfait_simulee_2 (n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    jl: str = "\n"
    save:str= "=== Evaluation of : 'est_parfait_simulee("+str(n)+")' ==="+jl+ "début de boucle, s = "+str(s)+jl+"début de boucle, i = "+str(i)+jl+"===================="
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
        save=save + "\n"+ "fin du tour 1 , s = "+str(s)+jl+"fin du tour 1 , i = "+str(i)+jl+"===================="
    save=save +jl+"sortie de boucle, s = "+ str(s) + " et n = " +str(n) + jl+str(n == s)+jl
    with open('save_est_parfait.txt', 'a') as fichier:
            fichier.write(save)
    return n == s
assert est_parfait_simulee_2(6)==True
assert est_parfait_simulee_2(9)==False
assert est_parfait_simulee_2(4)==False

#Question 2 :
import math
def space(i:int,a:int,n:int,f:int,s:int)->str:
    """Précondition : i>0 and a>0 and n>=0 and (f==1 or f==2) and (s==1 or s==2) and i<=a
    Calcul les espaces à mettre pour un élément de taille 'i+n' dans un espace 'a' avec 's' intervale"""
    result:str=""
    k:int
    nb:int
    if f==1 :
        nb=math.floor((a-(i+n))/s)
        
    else :
        nb=math.ceil((a-(i+n))/s)
    for k in range(nb):
        result = result + " "
    return result
assert space(26,50,2,1,2)=="           "
assert space(26,50,1,1,2)=="           "
assert space(26,50,0,1,1)=="                        "

def est_parfait_tableau(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    jl: str = "\n"
    bar:str="=================================================="
    space_title:int=22
    space_information:int=15
    longueur_information:int=3
    first:int=1
    second:int=2
    save:str= bar+jl+"|"+space(26,50,len(str(abs(n))),first,2)+"Simulation est_parfait("+str(n)+")"+space(26,50,len(str(abs(n))),second,2)+"|"+jl+bar+jl+"|"+space(6,space_title,0,first,2)+"tour"+space(6,space_title,0,second,2)+"|"+space(longueur_information,space_information,0,first,2)+"i"+space(longueur_information,space_information,0,second,2)+"|"+space(longueur_information,space_information,0,first,2)+"s"+space(longueur_information,space_information,0,second,2)+"|"+jl+bar+jl+"| entrée"+space(9,space_title,0,first,1)+"|"+space(longueur_information,space_information,len(str(abs(i))),first,1)+str(i)+" |"+space(longueur_information,space_information,len(str(abs(s))),first,1)+str(s)+" |"+jl+bar+jl
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
        save=save+"| tour "+str(i-1)+space(8,space_title,len(str(abs(i-1))),first,1)+"|"+space(longueur_information,space_information,len(str(abs(i))),first,1)+str(i)+" |"+space(longueur_information,space_information,len(str(abs(s))),first,1)+str(s)+" |"+jl+bar+jl
    save=save+"| tour "+str(i)+space(17,space_title,len(str(abs(i-1))),first,1)+"(sortie) |"+space(longueur_information,space_information,len(str(abs(i))),first,1)+str(i)+" |"+space(longueur_information,space_information,len(str(abs(s))),first,1)+str(s)+" |"+jl+bar+jl
    with open('save_est_parfait.txt', 'a') as fichier:
            fichier.write(save)
    return n == s
assert est_parfait_tableau(6)==True
assert est_parfait_tableau(9)==False
assert est_parfait_tableau(4)==False

# Exercice 5 :
# Question 1 :

def est_parfait_appels (n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait ."""
    s : int = 0
    i : int = 1
    while i != n :
        if divise(i, n):
            s = s + i
        i = i + 1
    print(str(i-1)+" appels à la fonction divise")
    print(n==s)
    return n == s
assert est_parfait_appels(6)==True
assert est_parfait_appels(9)==False
assert est_parfait_appels(8)==False

# Question 2 :

def est_parfait_opti(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait """

    s : int = 1
    i : int = 2
    if i == 1 : 
        return False
    while i != int(math.sqrt(n)) + 1 :
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        i = i + 1
    return n == s
assert est_parfait_opti(6)==True
assert est_parfait_opti(9)==False
assert est_parfait_opti(8)==False

def est_parfait_opti_appels(n : int) -> bool :
    """ Pre : n >= 1
    Decide si n est un nombre parfait """

    s : int = 1
    i : int = 2
    if i == 1 : 
        return False
    while i != int(math.sqrt(n)) + 1 :
        if divise(i, n):
            if i != math.sqrt(n) :
                s = s + i + (n // i)
            else :
                s = s + i
        i = i + 1
    print(str(i-2)+" appels à la fonction divise")
    print(n==s)
    return n == s
assert est_parfait_opti_appels(6)==True
assert est_parfait_opti_appels(9)==False
assert est_parfait_opti_appels(8)==False

# Question 3 :

# Pour est_parfait(n) il y a n-1 d'appels à divise fait lors de son évaluation car la fonction divise est appelée à chaque ajout de 1 à la valeur de i avec une valeur de départ de 1 soit i(x)=x+1 où x est le nombre de fois où divise est appellée et étant donné que la boucle s'arrête alors que i==n est vrai alors il faut résoudre i=n soit x+1=n soit x=n-1. CQFD

# Pour est_parfaite_opti(n) il y a int(math.sqrt(n))-1 d'appels à divise fait lors de son évaluation car la fonction divise est appelée à chaque ajout de 1 à la valeur de i avec une valeur de départ de 2 soit i(x)=x+2 où x est le nombre de fois où divise est appellée et étant donné que la boucle s'arrête alors que i==int(math.sqrt(n))+1 est vrai alors il faut résoudre i=int(math.sqrt(n))+1  soit x+2=nt(math.sqrt(n))+1  soit x=nt(math.sqrt(n))-1. CQFD

# Question 4 :
# Je tiens à dire que je vais de la programation depuis un petit moment et j'ai déjà réaliser plusieurs projet il donc compréhensible que je sois capable de faire une fonction qui peut parraître étonnant étant donner notre avancer dans l'année mais je vous assure être le réel créateur de cette fonction, je vous dit cela car on me l'a recommandé vivement pour éviter des quiproquo entre ce que je propose et ce qu'une machine pourrais créer comme code.
def graph()->None:
    """Affiche un graphe de la complexité d'appel de la fonction divise de est_parfait(n) et est_parfait_opti(n) en fonction de x soit n"""
    largeur:int = 150
    hauteur:int = 50
    y:int
    for y in range(hauteur, -2, -1):
        line:str = ""
        x:int
        for x in range(0, largeur):
            f_x:int = x - 1
            g_x:int = int(math.sqrt(x))-1
            if abs(f_x - y) == 0:
                line = line + "*"
            elif abs(g_x - y) == 0:
                line = line + "o"
            elif x == 0 and y == 0:
                line = line + "+"
            elif x == 0:
                line = line + "|"
            elif y == 0:
                line = line + "-"
            else:
                line = line + " "
        print(line) 
