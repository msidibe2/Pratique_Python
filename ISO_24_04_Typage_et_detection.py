# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:02:06 2024

@author: USER
"""

# variables itérables
tableau = [3,4,1,12, 33]

## détection du type de variables
# avec type()
a = "Python"
x = 23
estNombre = True

print(type(a))
type(x)
type(estNombre)

# avec isinstance()
print(isinstance(x, int))
print(isinstance(a, int))
print(isinstance(tableau, list))
