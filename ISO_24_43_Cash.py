# Python code​​​​​​‌​‌‌‌‌​​‌​​‌​‌​​​​​​​‌​​​ below
# Use print("messages...") to debug your solution.

def change(cash):
    '''
    Give back a change at the cash register
    Args :
        - cash : positive integer.
            matches the money the costumer put into the cash register.
    Returns :
        - dict which matchs change as bill and/or coin
    '''
    # precondition monnaie est un nbre positif inférieur à 9007199254740991
    if not (0 < cash < 9007199254740991) :
        return "Le montant est hors de la portée de la machine"
    
    else :
        
        # si la monnaie à rendre est multiple de 10    
        if cash % 10 == 0:
            return {
            'two': 0,
            'five': 0,
            'ten': cash//10
            }
        
        # si la monnaie à rendre est multiple de 5
        elif cash % 5 == 0:
            return {
            'two': 0,
            'five': (cash % 10) // 5,
            'ten': cash // 10
            }
        
        # cas de nbre pair comme 4, 6, 8, 12, 16
        elif cash % 2 == 0 :
            return {
            'two': (cash%10) // 2,
            'five': 0,
            'ten': cash // 10
            }
        
        # cas de nbre impair et/ou premier comme 1, 3, 13, 11, 23, 31
        elif cash % 2 != 0 and (cash%10 == 1 or cash%10 == 3 ):
            return 'None'
        
        # cas de nombre comme 7, 17, 27, 29
        else :
            return {
            'two': (cash % 5) //2,
            'five': (cash % 10) // 5,
            'ten': cash // 10
            }


  
        
def main():
    cash = input("Entrez la monnaie à rendre : ")
    try :
        cash = int(cash)
        result = change(cash)
        if result is None :
            print('Impossible de rendre la monnaie exacte avec les paramètres ' 
                   + 'disponibles')
        
        else :
            print(result)
    except ValueError :
        print('Veuillez entrez un montant valide')
        

if __name__ == '__main__':
    main()        
   
