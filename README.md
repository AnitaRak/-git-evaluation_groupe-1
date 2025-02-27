# Minitrice - Mini Calculatrice en Ligne de Commande

## 📌 Introduction
Minitrice est un programme permettant d'effectuer les 4 opérations arithmétiques de base (+, -, *, /) entre deux nombres positifs, en ligne de commande. Il supporte également l'utilisation de fichiers de tests pour automatiser les calculs.

## 📥 Installation
### Sous Linux :
```bash
# Cloner le projet
git clone git@github.com:AnitaRak/-git-evaluation_groupe-1.git
cd -git-evaluation_groupe-1

# Donner les permissions d'exécution aux scripts
chmod +x minitrice.py generator.py
```

### Sous Windows (WSL recommandé) :
1. Installer Python 3 et Git.
2. Cloner le projet et exécuter :
```bash
python3 minitrice.py
```

## 🚀 Utilisation

### 🔹 Mode interactif
Exécutez le programme et entrez les expressions mathématiques :
```bash
python3 minitrice.py
```
Exemple :
```
> 5+3
8
> 10/2
5.0
> (Ctrl+D pour quitter)
```

### 🔹 Mode avec STDIN
Vous pouvez utiliser un pipe pour fournir des entrées au programme :
```bash
echo "5+3" | python3 minitrice.py
```

### 🔹 Exécution avec un fichier de tests
Pour tester plusieurs expressions à la fois, utilisez un fichier de tests :
```bash
cat test/good-expression.txt | python3 minitrice.py
```

### 🔹 Exécution automatique des tests
Un script `test_runner.sh` est fourni pour exécuter les tests automatiquement et stocker les résultats :
```bash
./test_runner.sh
```
Les résultats seront stockés dans le répertoire `results/`.

Un script `runTest.sh` est fourni pour rajouter 1000 opérations à partir de generator.py dans le fichier operations.txt
```bash
./runTest.sh
```

## 📽️ Publication
Une vidéo générée par l'outil [gource](https://gource.io/) illustrant l'historique des contributions Git sera publiée sur YouTube.

La vidéo sera disponible via le lien : [git-evaluation](https://youtu.be/5NhsZ-WpwPI)


**Projet réalisé par :**

- Anita Rakotoarisoa Tantelimaminirina:
    - mini calculatrice minitrice.py + - * / :
    - gestion des erreurs : après, suite de minitrice.py

- ASMAHANI SAROUMAIA:
    - rédiger le fichier README.md
    - test & results : créer un fichier result qui affiche les resultats des tests des fichiers tests

- Joe Rakotomahefa:
    - gource :
    - automatiser les tests ? créer un miniscript qui crée un fichier avec 1000 opérations à l'aide du générator

- Nathan Riviere:
    - générateur d'opérations generator.py :
    - autres options, fermer avec ctrl+D, accepter une entrée STDIN, gestion du pipe

