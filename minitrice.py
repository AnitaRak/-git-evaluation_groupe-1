import sys

def calculer(expression):
    try:
        expression = expression.replace(' ', '')
        for op in ['+', '-', '*', '/']:
            if op in expression:
                num1, num2 = expression.split(op)
                num1, num2 = float(num1), float(num2)
                if op == '+':
                    resultat = num1 + num2
                elif op == '-':
                    resultat = num1 - num2
                elif op == '*':
                    resultat = num1 * num2
                elif op == '/':
                    if num2 != 0:
                        resultat = num1 / num2
                    else:
                        return 'Erreur : Division par zero.'

                # Convertir en entier si le résultat est un nombre entier
                if resultat.is_integer():
                    return int(resultat)
                else:
                    return resultat

        return 'Erreur : Opérateur non valide.'
    except ValueError:
        return 'Erreur : Entrée invalide. Assurez-vous d\'entrer deux nombres séparés par un opérateur.'

if __name__ == "__main__":
    # Si on a une entrée
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        print(calculer(expression))
    #Sinon on lance un mode interractif avec des input
    else:
        #On implémente le EOF avec ctrl+D
        try:
            while True:
                expression = input("> ")
                print(calculer(expression))
        except EOFError:
            print("\nFin des calculs :)")