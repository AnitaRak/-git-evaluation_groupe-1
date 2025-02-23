#!/bin/bash



# Ce script cree un fichier nommé operation.txt contenant 1000 expression générées par le script generator.py   
# Nombre d'expressions à générer
N=1000

# Nom du fichier de sortie
OUTPUT_FILE="operations.txt"

# Exécuter le générateur et rediriger la sortie vers le fichier
python3 generator.py $N > $OUTPUT_FILE

# Vérifier si le fichier a été créé
if [ -f $OUTPUT_FILE ]; then
    echo "Fichier $OUTPUT_FILE créé avec succès."
else
    echo "Erreur : le fichier $OUTPUT_FILE n'a pas été créé."
    exit 1
fi
