#!/bin/bash

mkdir -p results

for file in ./test/*.txt; do
    output_file="results/$(basename "$file" .txt)-result.txt"
    #echo "Exécution de : python3 minitrice.py < $file > $output_file"  # Ajouté pour debug
    python3 minitrice.py < "$file" > "$output_file"
    echo "Résultat enregistré dans $output_file"
done
