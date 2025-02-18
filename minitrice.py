def calculer(expression):
    try:
        # Supprimer les espaces éventuels autour des opérateurs
        expression = expression.replace(" ", "")

        # Trouver l'opérateur dans l'expression
        for op in ['+', '-', '*', '/']:
            if op in expression:
                # Diviser l'expression en deux nombres
                num1, num2 = expression.split(op)
                # Convertir les nombres en flottants
                num1, num2 = float(num1), float(num2)

                # Effectuer le calcul en fonction de l'opérateur
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
                        return "Erreur : Division par zéro."

                return f"Le résultat de {expression} est {resultat}"

        return "Erreur : Opérateur non valide."

    except ValueError:
        return "Erreur : Entrée invalide. Assurez-vous d'entrer deux nombres séparés par un opérateur."

# Exemple d'utilisation
expression = input("Entrez une expression (ex: 3+4) : ")
print(calculer(expression))
