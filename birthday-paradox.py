# coding: utf-8
import math

#constant

#Function
def p(n,N):
    a=(n*(n-1))
    b=(a/(2*N))
    c=math.exp(-b)
    d=1-c
    return d

def n(p,N):
    a=(1/(1-p))
    b=math.log(a)
    c=math.sqrt(2*N*b)
    return c

# Menu
while True :
    print """MENU :
    1 - With n, calculate probability(p) / BUGGGG
    2 - With p, calculate n(number of elements)
    q - Quit"""
    choice = raw_input("\nYour choice :")

    # Quit
    if (choice == 'q' or  choice =='Q' or choice =='quit'):
        break
    #Choice 1
    elif choice == '1' :
        try:
            input1 = int(input("Enter number of elements: \n"))
            input2 = int(input("Enter number of the group: \n"))
            #print "\n  The probability is egal to ", p(input1,input2)
            prob=1.0
            for i in range(input1):
                prob = prob * (input2-i)/input2
            print "\nThe probability is egal to ",prob
        except NameError:
            print "\nThat was not valid number."
        except SyntaxError:
            print "\nThat was not valid number."

    #Choice 2
    elif choice == '2':
        try:
            input1 = float(input("Enter probability p as 0<p<1, you want: \n"))
            input2 = int(input("Enter number of the group: \n"))
            print "\n  For the probability",input1 ,"the number of elements needed is:", n(input1,input2)
            break
        except ValueError:
            print "\n That was not valid number."
        except NameError:
            print "\nThat was not valid number."
        except SyntaxError:
            print "\nThat was not valid number."
