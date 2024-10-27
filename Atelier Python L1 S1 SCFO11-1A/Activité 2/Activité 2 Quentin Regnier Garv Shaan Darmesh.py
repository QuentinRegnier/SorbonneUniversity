# Quentin Régnier & Garv Shaan Darmesh
# Exercice 1:
# Question 1 :
import math
import random
def terme_leibniz(n:int)->float :
    """Précondition n>=0
    Prend en entrée un entier n et qui renvoie le terme d’indice n de la série alternée de      Leibniz"""
    return ((-1)**n)/(2*n+1)

assert terme_leibniz(0)==1.0
assert terme_leibniz(1)==(-1)/3
assert terme_leibniz(10)==1/21
# Question 2 :
def somme_leibniz(n:int)->float :
    """Précondition : n>=0
    Prend en entrée un entier n et qui renvoie la somme des n premiers termes de la série       alternée de Leibniz"""
    i:int=0
    somme:float=1
    while i<n :
        somme = somme + terme_leibniz(i+1)
        i = i+1
    return somme

assert somme_leibniz(0)==1
assert somme_leibniz(1)==1-1/3
assert somme_leibniz(4)==1-1/3+1/5-1/7+1/9
# Question 3 :
def approx_leibniz(n:int)->float :
    """Précondition : n>=0
    Prend en entrée un entier n et calcule une approximation de π en utilisant la somme des     n premiers termes de la série alternée de Leibniz"""
    return somme_leibniz(n)*4

assert approx_leibniz(10)==3.232315809405594
assert approx_leibniz(100)==3.1514934010709914
# Question 4 :
assert abs(approx_leibniz(9)-math.pi)<10**(-1)
assert abs(approx_leibniz(99)-math.pi)<10**(-2)
assert abs(approx_leibniz(999)-math.pi)<10**(-3)
# Exercice 2 :
# Question 1 :
def factoriel(n:int)->int :
    """Précondition : n>=0
    Cacule le produit factoriel de n"""
    i:int=1
    produit:int=1
    while i<=n :
        produit = produit * (i)
        i = i+1
    return produit
assert factoriel(1)==1
assert factoriel(3)==6
assert factoriel(5)==120

def m_q(q:int)->float :
    """Précondition : q>=0
    Calcule le terme M_q de la formule des frères Chudovsky"""
    return (factoriel(6*q))/(factoriel(3*q)*factoriel(q)**3)
assert m_q(1)==120
assert m_q(2)==83160
assert m_q(3)==81681600

def l_q(q:int)->float :
    """Précondition : q>=0
    Calcule le terme L_q de la formule des frères Chudovsky"""
    return 545140134*q+13591409
assert l_q(1)==558731543
assert l_q(2)==1103871677
assert l_q(3)==1649011811

def x_q(q:int)->float :
    """Précondition : q>=0
    Calcule le terme X_q de la formule des frères Chudovsky"""
    return (-262537412640768000)**q
assert x_q(1)==-262537412640768000
assert x_q(2)==68925893036108889235415629824000000
assert x_q(3)==-18095625621654356959022098935941777779064832000000000

def approx_chudovsky(q:int)->float :
    """Précondition : q>=0
    Calcule un approximation de pi grâce à la formule des frères Chudovsky"""
    i:int=0
    somme:float=0
    while i<q :
        somme = somme + (m_q(i)*l_q(i))/(x_q(i))
        i = i+1
    return 426880*math.sqrt(10005)*(somme)**(-1)
assert abs(approx_chudovsky(1)-math.pi)<10**(-12)
assert abs(approx_chudovsky(2)-math.pi)<10**(-14)
assert abs(approx_chudovsky(3)-math.pi)<10**(-100)

# Exercice 3 :
def approx_chudovsky_optim(q:int)->float :
    """Précondition : q>=0
    Calcule un approximation de pi grâce à la formule des frères Chudovsky"""
    i:int=0
    lq:int=13591409
    mq:float=1
    xq:float=1
    somme:float = 0
    if q>=1 :
       while i<q :
           somme = somme + (mq*lq)/(x_q(i))
           i = i+1
           xq=xq*(-262537412640768000)
           lq=lq+545140134
           mq=mq*(((6*i+6)*(6*i+5)*(6*i+4)*(6*i+3)*(6*i+2)*(6*i+1))/((3*i+3)*(3*i+2)*(3*i+1)*((i+1)**3)))
       return 426880*math.sqrt(10005)*(somme)**(-1)
    else:
       return 426880*math.sqrt(10005)*((mq*lq)/(xq))**(-1)
assert abs(approx_chudovsky_optim(1)-math.pi)<10**(-12)
assert abs(approx_chudovsky_optim(2)-math.pi)<10**(-12)
assert abs(approx_chudovsky_optim(3)-math.pi)<10**(-12)
# Exercice 4 :
def approx_pi(n:int)->float:
    """Précondition : n>0
    Appromise la valeur de pi en utilisant la probabilité qu'un point appartienne au cercle de       rayon 1/2 dans le graphique allant de (0,0) à (1,1)"""
    dans_le_cercle:int= 0
    i:int
    for i in range(0,n):
        x:float = random.random() 
        y:float = random.random()
        distance:float = (x - 0.5)**2 + (y - 0.5)**2
        if distance <= (0.5)**2:
            dans_le_cercle = dans_le_cercle + 1
    return 4 * (dans_le_cercle / n)
