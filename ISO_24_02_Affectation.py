# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:48:53 2024

@author: USER
"""
# affectation multiple

x = y = z = 10
print(x)
print(id(x))
id(y)
print(id(z))

#affect multiple
nom, age, genre = "Boris", 22, "H"
print(nom, age, genre)
id(nom)
id(age)
id(genre)