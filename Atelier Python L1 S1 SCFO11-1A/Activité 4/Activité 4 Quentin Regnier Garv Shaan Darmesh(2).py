# Exercice 1 :
def identite(s : str) -> str :
    """ Renvoie la chaine s telle quelle """
    return s

assert identite("LU1IN011") == "LU1IN011"
assert identite("") == ""

def identite_texte(nom : str) -> None :
    """ Precondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-copie.txt """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-copie.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(identite(ligne))
assert identite_texte('bovary')==None
# Exercice 2 :
# Question 1 :
def est_majuscule(t:str)->bool :
    """Précondition : len(t)==1
    Vérifie si la lettre est bien une majuscule"""
    return ord(t)>64 and ord(t)<91
def est_minuscule(t:str)->bool:
    """Précondition : len(t)==1
    Vérifie si la lettre est bien une majuscule"""
    return ord(t)>96 and ord(t)<123
assert est_majuscule("C")
assert not est_minuscule("C")
assert est_minuscule("c")
assert not est_majuscule("c")
assert not est_minuscule(" ")
assert not est_majuscule(" ")

# Question 2 :
def est_chiffre(t:str)->bool:
    """Précondition : len(t)==1
    Vérifie si le string correspond à un chiffre"""
    return ord(t)>47 and ord(t)<58
assert est_chiffre("1")
assert est_chiffre("0")
assert est_chiffre("9")
assert not est_chiffre(" ")
assert not est_chiffre("a")

def caractere_decale(c:str,n:int)->str:
    """Précondition : len(c)==1
    Décale de 'n' lettre la lettre de variable 'c'"""
    if est_majuscule(c):
        return chr(((ord(c)-65+n)%26)+65)
    elif est_minuscule(c):
        return chr(((ord(c)-97+n)%26)+97)
    return c
assert caractere_decale("a", 0) == "a"
assert caractere_decale("a", 3) == "d"
assert caractere_decale("A", 3) == "D"
assert caractere_decale("V", 8) == "D"
assert caractere_decale(" ", 3) == " "

# Question 3\a
def ligne_chiffre_cesar(s:str,n:int)->str:
    """Précondition : len(s)>=0
    Renvoie une chaine de caractère en appliquant le chiffrement de César de clef 'n' à 's' """
    i:int
    result:str=""
    for i in range(len(s)):
        result = result + caractere_decale(s[i],n)
    return result
assert ligne_chiffre_cesar(" Bonjour LU1IN011 ", 3) == " Erqmrxu OX1LQ011 "
assert ligne_chiffre_cesar(" Bonjour LU1IN011 ", 0) == " Bonjour LU1IN011 "

# Question 3\b :
def ligne_dechiffre_cesar(s:str,n:int)->str:
    """Précondition : len(s)>=0
    Renvoie une chaine de caractère en déchiffrant le chiffrement de César de clef 'n' à 's '"""
    return ligne_chiffre_cesar(s,(-n))
assert ligne_dechiffre_cesar(" Erqmrxu OX1LQ011 ", 3) == " Bonjour LU1IN011 "
assert ligne_dechiffre_cesar(" Bonjour LU1IN011 ", 0) == " Bonjour LU1IN011 "
beaute1:str = "Je suis belle , o mortels ! comme un reve de pierre ,"
assert ligne_dechiffre_cesar(ligne_chiffre_cesar(beaute1,12),12) == beaute1

# Question 4 :
def chiffre_fichier_cesar(nom:str,n:int)->None:
    """Précondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-cesar.txt et chiffre le contenu du fichier originel en appliquant le chiffrement de César avec pour clef 'n'"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-cesar.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_chiffre_cesar(ligne,n))
assert chiffre_fichier_cesar('bovary',15)==None

def dechiffre_fichier_cesar(nom:str,n:int)->None :
    """Précondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-cesar.txt et chiffre le contenu du fichier originel en déchiffrant le code César avec pour clef 'n'"""
    chiffre_fichier_cesar(nom,(-n))
assert dechiffre_fichier_cesar('bovary-cesar',15)==None

# Exercice 3 :

def attaque_cesar(nom:str,debut:int,fin:int)->None:
    """Preconditions : debut<fin and len(nom)>0
    Cherche par la force brute la valeur de la clef qui code le texte entre les bornes 'debut' et 'fin' et affiche cette recherche dans un fichier '{nom}-decode' """
    with open(nom + ".txt", "r") as source :
        with open(nom + "-decode.txt", "w") as destination :
            lignes:List[str]=source.readlines()
            sdl:str='\n'
            result:str='Ligne choisies : '+str(debut)+'-'+str(fin)+sdl
            i:int
            j:int
            if debut<len(lignes) and fin<=len(lignes) :
                for i in range(1,27):
                    result=result+'================================'+sdl+"Decalage de : "+str(i)+sdl
                    for j in range(debut,fin):
                        result=result+ligne_chiffre_cesar(lignes[j],i)+sdl
            else :
                result=result+"Itération "+str(i+1)+" : Plage de lignes invalide."
            result=result+sdl
            destination.write(result)
assert attaque_cesar('bovary-cesar',300,306)==None

# Exercice 4 :

def in_tableau(x:int, tableau:List[int])->bool:
    """Vérifie si 'x' est compris dans la liste 'tableau'"""
    i:int
    for i in range(len(tableau)):
        if x==tableau[i]:
            return True
    return False
assert in_tableau(2,[1,2,3,4])==True
assert in_tableau(5,[1,2,3,4])==False

def resultat_unique(a:int,b:int)->bool:
    """Vérifie si il n'y a pas de répétion dans les valeurs obtenu avec a*k+b pour k appartenant à [0,25]"""
    resultats:List[int]=[]
    k:int
    for k in range(26) :
        valeur:int=(a*k+b)%26
        if in_tableau(valeur,resultats):
            return False
        else :
            resultats.append(valeur)
    return True
assert resultat_unique(12,2)==False
assert resultat_unique(15,2)==True

def trouver_premier_superieur(a: int,b:int) -> int:
    """Precondition : a>=0
    Trouve le plus petit nombre premier avec 26 supérieur ou égal à 'a'."""
    a_n:int=a
    while not resultat_unique(a_n,b):
        a_n=a_n+1
    return a_n
assert trouver_premier_superieur(12,2)==15
assert trouver_premier_superieur(6,5)==7

def caractere_affine(c:str,a:int,b:int)->str:
    """Précondition : len(c)==1 and a>=0 and b>=0
    Transforme la lettre avec a*x+b la lettre de variable 'c'"""
    a_v:int=trouver_premier_superieur(a,b)
    if est_majuscule(c):
        return chr(((a_v*(ord(c)-65)+b)%26)+65)
    elif est_minuscule(c):
        return chr(((a_v*(ord(c)-97)+b)%26)+97)
    return c
assert caractere_affine("a",12,2) == "c"
assert caractere_affine("a",4,7) == "h"
assert caractere_affine("A", 4,7) == "H"
assert caractere_affine("V", 8,32) == "N"
assert caractere_affine(" ", 8,32) == " "

def ligne_chiffre_affine(s:str,a:int,b:int)->str:
    """Précondition : len(s)>=0
    Renvoie une chaine de caractère en appliquant le chiffrement de César de clef affine a*x+b à 's' """
    i:int
    result:str=""
    for i in range(len(s)):
        result = result + caractere_affine(s[i],a,b)
    return result
assert ligne_chiffre_affine("Portez ce vieux whisky au juge blond qui fume ",12,2)=="Texbkn gk fskqj udsmwy cq hqok rlepv iqs zqak "
assert ligne_chiffre_affine(" Bonjour LU1IN011 ! ",5,9)==' Obwcbfq MF1XW011 ! '

def chiffre_fichier_affine(nom:str,a:int,b:int)->None:
    """Précondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-cesar.txt et chiffre le contenu du fichier originel en appliquant le chiffrement de César avec pour clef 'a'*x+'b'"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-affine.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_chiffre_affine(ligne,a,b))
assert chiffre_fichier_affine('bovary',12,2)==None

def pgcd_etendu(a: int, b: int) -> Tuple[int,int,int]:
    """Précondition : a>=0 and b>=0
    Utilise l'algorithme d'Euclide étendu pour trouver le PGCD de a et b ainsi que les coefficients de Bézout."""
    x:int=0
    y:int=0
    if b == 0:
        return (a, 1, 0)
    else:
        pgcd, x1, y1 = pgcd_etendu(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (pgcd, x, y)
assert pgcd_etendu(7,26)==(1, -11, 3)
assert pgcd_etendu(15,26)==(1, 7, -4)

def inverse_modulaire(a: int, m: int) -> Optional[int]:
    """Précondition : a>=0 and m>=0
    Trouve l'inverse de 'a' modulo 'm' en utilisant l'algorithme d'Euclide étendu."""
    pgcd,x,y = pgcd_etendu(a, m)
    if pgcd != 1:
        print("L'inverse modulaire de "+str(a)+" modulo "+str(m)+" n'existe pas.")
        return None
    return x % m

assert inverse_modulaire(7,26) == 15
assert inverse_modulaire(7,15) == 13

def caractere_affine_decode(c:str,a:int,b:int)->str:
    """Précondition : len(c)==1 and a>=0 and b>=0
    Dechiffre la lettre 'c' à une position 'p' en faisant p'=(p-b)*a^(-1) mod 26"""
    a_v:int=trouver_premier_superieur(a,b)
    a_i:int=inverse_modulaire(a_v,26)
    if est_majuscule(c):
        return chr((((((ord(c)-65)-b)%26)*a_i)%26)+65)
    elif est_minuscule(c):
        return chr((((((ord(c)-97)-b)%26)*a_i)%26)+97)
    return c

assert caractere_affine_decode("c",12,2) == "a"
assert caractere_affine_decode("h",4,7) == "a"
assert caractere_affine_decode("H", 4,7) == "A"
assert caractere_affine_decode("N", 8,32) == "V"
assert caractere_affine_decode(" ", 8,32) == " "

def ligne_dechiffre_affine(s:str,a:int,b:int)->str:
    """Précondition : len(s)>=0
    Renvoie une chaine de caractère en appliquant le dechiffrement de César à 's' """
    i:int
    result:str=""
    for i in range(len(s)):
        result = result + caractere_affine_decode(s[i],a,b)
    return result
assert ligne_dechiffre_affine("Texbkn gk fskqj udsmwy cq hqok rlepv iqs zqak ",12,2)=="Portez ce vieux whisky au juge blond qui fume "
assert ligne_dechiffre_affine(" Obwcbfq MF1XW011 ! ",5,9)==' Bonjour LU1IN011 ! '

def dechiffre_fichier_affine(nom:str,a:int,b:int)->None:
    """Précondition : <nom>.txt est un fichier existant
    recopie le contenu du fichier <nom>.txt dans <nom>-cesar.txt et chiffre le contenu du fichier originel en appliquant le chiffrement de César avec pour clef 'a'*x+'b'"""
    with open(nom + ".txt", "r") as source :
        with open(nom + "-decode.txt", "w") as destination :
            ligne : str
            for ligne in source.readlines() :
                destination.write(ligne_dechiffre_affine(ligne,a,b))
assert dechiffre_fichier_affine('bovary-affine',12,2)==None

# Exercice 5 :
def caractere_vigenere(c:str,key:str)->str:
    """Précondition : len(c)==1 and len(key)==1 and (est_majuscule(key) or est_minuscule(key))
    Chiffre la lettre 'c' à une position en la décalant de la position de la 'key' dans l'alphabet"""
    n:int=0
    if est_majuscule(key):
        n=65
    elif est_minuscule(key):
        n=97
    if est_majuscule(c):
        return chr((((ord(c)-65)+(ord(key)-n))%26)+65)
    elif est_minuscule(c):
        return chr((((ord(c)-97)+(ord(key)-n))%26)+97)
    return c

assert caractere_vigenere("B","c") == "D"
assert caractere_vigenere("o","l") == "z"
assert caractere_vigenere("n","e") == "r"
assert caractere_vigenere("j","c") == "l"
assert caractere_vigenere(" ","l") == " "

def ligne_chiffre_vigenere(s:str,key:str)->str:
    """Précondition : len(s)>=0 and len(key)>=1
    Renvoie une chaine de caractère en appliquant le chiffrement de Vigenere à 's' """
    i:int
    result:str=""
    for i in range(len(s)):
        result = result + caractere_vigenere(s[i],key[i%len(key)])
    return result
assert ligne_chiffre_vigenere("Bonjour","cle")=='Dzrlzyt'
assert ligne_chiffre_vigenere("Portez ce vieux whisky au juge blond qui fume ","alcool")=='Pzthsk ng jtefz ksidmm lu liup mncbo bww quxg '

def caractere_vigenere_decode(c:str,key:str)->str:
    """Précondition : len(c)==1 and len(key)==1 and (est_majuscule(key) or est_minuscule(key))
    Chiffre la lettre 'c' à une position en la décalant de moins la position de la 'key' dans l'alphabet"""
    n:int=0
    if est_majuscule(key):
        n=65
    elif est_minuscule(key):
        n=97
    if est_majuscule(c):
        return chr((((ord(c)-65)-(ord(key)-n))%26)+65)
    elif est_minuscule(c):
        return chr((((ord(c)-97)-(ord(key)-n))%26)+97)
    return c

assert caractere_vigenere_decode("D","c") == "B"
assert caractere_vigenere_decode("z","l") == "o"
assert caractere_vigenere_decode("r","e") == "n"
assert caractere_vigenere_decode("l","c") == "j"
assert caractere_vigenere_decode(" ","l") == " "

def ligne_dechiffre_vigenere(s:str,key:str)->str:
    """Précondition : len(s)>=0 and len(key)>=1
    Renvoie une chaine de caractère en appliquant le dechiffrement de Vigenere à 's' """
    i:int
    result:str=""
    for i in range(len(s)):
        result = result + caractere_vigenere_decode(s[i],key[i%len(key)])
    return result
assert ligne_dechiffre_vigenere("Dzrlzyt","cle")=='Bonjour'
assert ligne_dechiffre_vigenere("Pzthsk ng jtefz ksidmm lu liup mncbo bww quxg ","alcool")=='Portez ce vieux whisky au juge blond qui fume '

# Exercice 6 :

def chiffre_scytale(s: str, n: int) -> str:
    """Divise une chaîne en n sous-listes avec répartition équitable des éléments."""
    m:int=0
    if len(s)%n==0:
        m=len(s)//n
    else:
        m=(len(s)//n)+1
    tableau:List[List[str]]=[]
    i:int
    j:int
    for i in range(n):
        tableau2:List[str]=[]
        for j in range(m*i,m*(i+1)):
            if j>len(s)-1:
                tableau2.append("_")
            else :
                tableau2.append(s[j])
        tableau.append(tableau2)
    s2:str=""
    k:int
    l:int
    for k in range(m):
        for l in range(n):
            s2=s2+tableau[l][k]
    return s2
assert chiffre_scytale("0123456789",3)=='04815926_37_'
assert chiffre_scytale("0123456789",8)=='02468___13579___'
