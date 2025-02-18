# generator.py
import sys
import random


minVal = 1.0
maxVal = 1000.0

def generate_float(min,max):
    return random.uniform(min, max)

def generate_operator():
    operateurs = ["+","-","*","/"]
    integer = random.randint(0, 3)
    return operateurs[integer]

def generate_expression():
    result = ""
    result += str(generate_float(minVal,maxVal))
    result += generate_operator()
    result += str(generate_float(minVal,maxVal))
    return result

def generate_n_expressions(n):
    for _ in range(n):
        sys.stdout.write(generate_expression() + "\n")



# fonction main qui va se lancer au lancement du programme, prendre l'argument pour sortir le nombre d'expressions voulues
# python   generator.py nb
# commande arg0         arg1
# A voir si ça va causer des erreurs avec le pipe | après ?
if __name__ == "__main__":
    try:
        # n expressions, 1 par défaut
        if len(sys.argv) < 2:
            n=1
        else :
            n = int(sys.argv[1])
        
    except ValueError:
        print("Erreur : le paramètre doit être un entier valide.")
        sys.exit(1)

    generate_n_expressions(n)