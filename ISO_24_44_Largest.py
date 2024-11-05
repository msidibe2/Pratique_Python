# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:57:18 2024

@author: USER
"""

import time
from typing import List


def find_largest(numbers: List[int]) -> int:
    '''
    Args:
        - numbers (List[int]): Des nbres entiers.
    Returns:
        La plus grande valeur parmi les nombres donnés en paramètres.
    '''
    # Write your code here
    if not (1 <= len(numbers) <= 10) :
        return 'la taille du tableau doit être comprise entre 1 et 10'
    for number in numbers:
         if not (-2**31 <= number <= (2**31) - 1):
             return 'le tableau contient une valeur non prise en charge'

    return max(numbers) 


def test(func, args, limite):
    try :
        start_time = time.time()
        result = func(*args)
        #time.sleep(7.5)
        end_time = time.time()
        execution_time = end_time - start_time  
        print(f"Temps d\'exécution : {execution_time:.4f} s")
        if execution_time > limite :
            raise Exception('Temps limite d\'exécution depassé')
        return result
    
    except Exception  as e:
        print(e)        


# Ignore and do not change the code below
numbers = [24, 33, 40, -10**9, 13, 2, 3]

def main():
    res = test(find_largest, [numbers], 6)
    print(res)   
    

if __name__ == "__main__":
    main()
# Ignore and do not change the code above