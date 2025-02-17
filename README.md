# git-evaluation_groupe-1

## Repartition des tâches : 
**Section à supprimer** 

Anita : 
- mini calculatrice minitrice.py + - * / :
- gestion des erreurs : après, suite de minitrice.py

Nathan  : 
- générateur d'opérations generator.py :
- autres options, fermer avec ctrl+D, accepter une entrée STDIN, gestion du pipe :

Joe : 
- gource :
- automatiser les tests ? créer un miniscript qui crée un fichier avec 1000 opérations à l'aide du générator

Saroumaia: 
- rédiger le fichier README.md
- test & results : créer un fichier result qui affiche les resultats des tests des fichiers tests

## Le barème pour rappel
**Section à supprimer** 
 - La rédaction du `README.md` conforme à la consigne : 1 points,
 - Respect des noms de programmes et fichiers pour les travaux réalisés : 2 points,
 - Exécution correcte de votre programme sur les fichiers du répertoire `test` :  1 points,
 - Présence du répertoire `results` contenant les différents fichiers de résultat avec le contenu attendu : 1 points,
 - Exécution correcte de votre programme sur les scénarios dans ce document : 1 points;
 - La création du programme `generator` et son exécution correcte : 1 point,
 - Gestion et explication des erreurs gérées par `generator` : 1 point **(bonus)**,
 - Exécution correcte de votre programme sur un grand fichier (environ 10000 lignes) qui n'est pas fournis : 1 point,
 - Chaque message commit doit avoir un sujet court (< 70 caractères) et doit décrire correctement le travail réaliser par le commit. Si votre décription est plus longue, utilisez le corps du message de commit : 2 points,
 - Votre historique de commit doit être similaire à l'historique produit par le [workshop 3](https://github.com/frozar/git-workshop-3/blob/main/img/historique-final.png) : 3 points,
 - Pour chaque progression sur votre projet, l'utilisation des *Pull Request* sur Github avec des descriptions explicites du contenu de la *Pull Request* : 3 points,
 - Création d'un Github Actions pour automatiser les tests de minitrice sur les fichiers de tests. Les tests doivent vérifier que le programme s'exécute correctement et que les résultats de calcul sont corrects : 2 point,
 - Publication de la vidéo générée par l'utilitaire [gource](https://gource.io/) correspondante à votre activité sur ce dépôt : 2 points.

## Composition du groupe : 
- Anita Rakotoarisoa Tantelimaminirina
- Saroumaia Asmahani
- Joe Rakotomahefa
- Nathan Riviere

## Installation :
Ce qu'il faut faire pour pouvoir lancer votre programme. Si des logiciels tiers (compilateur par exemple) doivent être installer, les procédures d'installation doivent être décrite ici. Il en est de même pour les bibliothèques,

## Exécution :
Un exemple d'utilisation de votre programme, avec la sortie attendue, comme ce qui fait dans ce document,
Générator : Description de la gestion de ou des erreurs que vous avez mis en place sur le programme generator. La ou les procédures pour reproduire le ou les erreurs doivent être renseignées,

## Publication :
Le lien Youtube de votre vidéo gource associée à l'activité sur votre dépôt (plus de renseignements dans la section suivante),

## Liens utiles :
Une liste de ressoruces en ligne qui vous a été utile pour réussir ce projet. Cette liste doit être sous la même forme que la section Liens utiles de ce document.
 - [Organisation du développement collaboratif](https://slides.com/frozar/git) : le support de cours pour git/github,
 - [How to capture Control+D signal?](https://stackoverflow.com/questions/1516122/how-to-capture-controld-signal) : discussion sur l'interception du signal `End Of File`,
 - [Find out if there is input from a pipe or not in Python?](https://stackoverflow.com/questions/33871836/find-out-if-there-is-input-from-a-pipe-or-not-in-python) : discussion sur la détection de l'utilisation d'un pipe en Python,
 - [My Gource video production pipeline](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0) : décrit un exemple d'utilisation de gource,
 - [Philosophie d'Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix) : description de la philosophie Unix,
 - [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix)) : description du pipe,
 - [Pipe: How the System Call That Ties Unix Together Came About](https://thenewstack.io/pipe-how-the-system-call-that-ties-unix-together-came-about/) : décrit l'histoire de la création du pipe.