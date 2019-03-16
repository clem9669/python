# coding: utf-8

# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non
y = input("Input any year : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
y = int(y) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
bissextile = False # On crée un booléen qui vaut vrai ou faux
                   # selon que l'année est bissextile ou non

if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0 ):
    print("This year is a leap year.")
else:
    print("This year is NOT leap year.")
