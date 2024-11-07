# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:29:57 2024

@author: USER
"""
# solution définitive de copy
import copy
a = [2, 3, [6, 3]]
b = a.copy()
b[2][1] = 100
b
a

# deep copy : recommandée
a = [2, 3, [6, 3]]
c = copy.deepcopy(a)
c[2][1] = 100
a
c

#%% opérateur de déballage *
#  cas de listes de tuple
a = [2, 3, [6, 3]]
b =[2]
c = [*a, *b]
c

# cas de dict
x = {'a': 6, 'b':1}
y = {'c': 100}
z = {**x, **y}
z

clefs = {*x, *y}
clefs


#%% fonction dir()
# déballe ce qu'il y a ds une fct
dir(list)
import numpy
dir(numpy.random)

#%% help()
help(numpy.random.test)
