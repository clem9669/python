# coding: utf-8

import math

t = input('Please fill in your height (Meter):  ')
p = input ('Please fill in you weight (KG) : ')

t = float(t)
p = int(p)

IMC = ((p)/(t * t))
IMC1 = round(IMC,1)
s = 'Here\'s your BMI: ' + repr(IMC1)
print s
