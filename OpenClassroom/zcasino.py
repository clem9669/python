# -*-coding: utf-8 -*
import time
from random import *
from math import ceil
#Improvement:
#Exception
#q to quit
# E = 3(1/50)+0,5(0,5)+(-1)(1/5) = 0,11 (approx. but almost equilibrate)
print('''
                Welcome in ZCasino
__________________________________________________________

Every player start with 50$.
Pick a number in range of 0 to 49.
Set your bet amount.
Even number are red / Odd are black.

Winning condition:
* Have the same color = gain*0.5
* Match the number = gain*3

                                        --Good luck folks\n
Press enter to continue
__________________________________________________________''')

my_money = 50
my_bet = 0
result_from_bet = 0

while my_money > 0:
    try:
        my_num = int(input("Please select a number [0-49]: "))
    except ValueError:
        print("Enter a number")
        break
    if my_num > 49 or my_num < 0:
        print ("0<number<49")
    else:
        print ("You have ", my_money , "$")
        my_bet = int(input("Enter the amount of the bet: "))
        if my_bet > my_money or my_bet < 0:
            print ("Invalid number")
        else:
            if my_num % 2 == 0:
                print ("Your number is:", my_num , ", an even number (red).")
                my_color = 1
                pass # Even
            else:
                print ("Your number is:", my_num , ", an odd number (black).")
                my_color = 0
                pass # Odd
            print("\n Let's roulette ! \n")
            time.sleep(2)
            correct_num = randrange(0,49)
            if correct_num % 2 == 0:
                print("The correct number is:", correct_num,", an Even (red).")
                correct_color = 1
                pass
            else:
                print("The correct number is:", correct_num,", an Odd (black).")
                correct_color = 0
                pass
            if my_num == correct_num:
                my_bet = ceil(my_bet * 3)
                my_money = my_money + my_bet
                print("!!! Win !!!")
                print ("You have: ", my_money, "$\n")
            elif my_color == correct_color:
                my_bet = ceil(my_bet * 0.5)
                my_money = my_money + my_bet
                print("WIN")
                print ("You have: ", my_money, "$\n")
            else:
                my_money = ceil(my_money - my_bet)
                print ("UNLUCKY ")
                print ("You have: ", my_money, "$\n")

print("Bye !")
