# -*-coding: utf-8 -*
from math import sqrt

#PPCM
def ppcm(a,b) :
    return (a * b) / pgcd(a,b)

#prime
def premier(a) :
    result = True
    n = 2
    top = sqrt(a)
    while (n <= top) :
        if a % n== 0 :
            return False
        else :
            n += 1
    return True

#DECOMPOSITION
def pdecomp(a) :
    result = ''
    n = 2
    anciena = a
    premier = True
    while (n <= a) :
        if (a % n == 0) :
            premier = False
            if result == '' :
                result = str(n)
        else :
            result = result + '.' + str(n)
        a = a / n
    else :
        n = n + 1
    if premier :
        return str(anciena)
    else :
        return result
#pgcd
def pgcd(a,b):
    while a%b != 0:
        a, b = b, a%b
    return b


if __name__ == "__main__":

    # Core
    while True :
        print ('''MENU :
        1 - Calculer le PGCD de deux nombres
        2 - Calculer le PPCM de deux nombres
        3 - Dterminer si un nombre est premier
        4 - Donner la decomposition en facteur premier d'un nombre
        q - Quitter''')

        choix = input("\nVotre choix :")

        # Quitter
        if (choix == 'q' or choix =='Q' or choix =='quit') :
            break

     # choix 1 : pgcd
        elif (choix == '1') :
            print ("\nSaisissez 2 entiers ")
            entier1 = input()
            entier2 = input()
            print ("Le PGCD de", entier1, "et", entier2, "est", pgcd(entier1,entier2))
            print ('\n')


    # choix 2 : ppcm
        elif (choix == '2') :
            print ("\nSaisissez 2 entiers ")
            entier1 = input()
            entier2 = input()
            print ("Le PPCM de", entier1, "et", entier2, "est", ppcm(entier1,entier2))
            print ('\n')

    # Choix 3: premier ?
        elif (choix == '3') :
            entier = input("Saisissez un entier ")
            if premier(entier) :
                print (entier, "est premier")
                print ('\n')
            else :
                print (entier, "n'est pas premier")
                print ('\n')

    # Choix 4: DECOMPOSITION ?
        elif (choix == '4') :
            entier = input("Saisissez un entier ")
            print ("La decomposition de", entier, "en premiers est", pdecomp(entier))
            print ('\n')
