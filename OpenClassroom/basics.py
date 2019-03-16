# -*-coding: utf-8 -*
#import math as othername
#from PGCD import *
# from math import *
import os, re

# print (sqrt(5))
#os.system("sleep 4")

#create dict
#
# my_dict = dict()
# #print(type(my_dict)) #result = <class 'dict'>
# my_dict["alpha"] = "first input"
# my_dict["beta"] = "second input"
# my_dict['username'] = 'thekiller34'
# my_dict['password'] = 'ind33dit\'sme '
# print(my_dict)

# inventory = [
#     ("fraises", 76),
#     ("prunes", 51),
#     ("pommes", 212),
#     ("poires", 18),
#     ("melons", 4),
# ]
# # print(inventory.sort()) # only for list not tuple list
# print(sorted(inventory, key=lambda inventory: inventory[1])) # sort by number [1] / sort by alphabet [Ø] or none

# string = "this is a long string but not as long as it could be"
# r = re.search('is',string)
# r = re.findall('not', string)
# print(r)

# qtt_a_retirer = 7
# fruits_stockes = [15, 3, 18, 21]
# print([nb_fruits-qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer])


# a,b=2,5
# chain = [1,4,55,77]
# chainz = "Hello Pal, do you really know the difference between UK & England ?"
# print(*chain) # output: 1 4 55 77
# print(chain) #output : [1, 4, 55, 77]
# print(chainz.split("o"))
# print(" ".join(chainz))

# string =[1, 2, 3, 5, 7, 11]
# string[3]='ZE' # overwrite 5
# string.append(12) # add 12 @ the end
# string.insert(0,0)
# string.insert(len(string),1000)
# string.insert(len(string),10001)
# del string[4]
# string.remove(3)
# print(string)
# for var in string:
#     print(var)

# mot = "lacavale"
# mot = "b" + mot[1:]
# autremot = mot[3:len(mot)]
# print(mot,autremot)


# p = "lalk alk eraefrefreafearfre far flkaef fkre lafkr akf zmlalfr amlf lrflafl almfrlfal"
# r = p.split(' ')
# for i in range(0, len(r)):
#     print(p.split(' ')[i])
#     print(i)

# name = "paul"
# age = 44
# city ="London"
# print("my name is {0},i am {1} years old, i live in {2} ".format(name,age,city))




# try:
#     nb= int(input("Print multiplication table of: "))
#     b = int(input("Table lenght:"))
# except NameError:
#     print("erreur")
# except ValueError:
#     print ("[*] Entered value is incorrect\n")
#
# for i in range (0, b+1):
#     print (i,"*", nb,"=",i*nb)

# i =0
# while i < 10:
#     print (i)
#     i+=1

# for i in range (0,10):
#     print(i)

# def pgcd(a,b):
#     while a%b != 0:
#         a, b = b, a%b
#     return b

# string="lmljcazboiaiur"
# for letters in string:
#     if letters in "akmlpbc":
#         print (letters)
#     else:
#         print ("*")

# while 1:
#     a = input("press q to quit \n")
#     if a == 'q':
#         print("fin")
#         break
#     else:
#         print("hint =q")
