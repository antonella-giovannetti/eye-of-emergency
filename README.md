# eye-of-emergency

## Présentation du projet :

Ce projet a pour but de nous initié aux **Natural Language Processing (NLP)** et de nous faire découvrir les différentes méthodes de traitement de texte.   
Pour cela, nous avons utilisé deux jeux de tweets en anglais : un jeu de tweets d'entrainement et un jeu de tweets de test.   
Les jeux de données se présentent sous forme de fichiers csv avec :
- une colonne `id` : l'identifiant unique du tweet,
- une colonne `text` : le contenu du tweet,
- une colonne `location` : la localisation de l'utilisateur ayant posté le tweet,
- une colonne `keyword` : le mot-clé associé au tweet.

Le jeu d'entraiement contient également :
- une colonne `target` : la cible du tweet (0 pour un tweet normal et 1 pour un tweet signalant une catastrophe).