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
    import sys
    if len(sys.argv) == 2:
        expression = sys.argv[1]
        resultat = calculer(expression)
        print(resultat)
    else:
        print("Usage: ./calculatrice.py 'expression'")
