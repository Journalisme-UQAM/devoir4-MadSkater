# coding : utf-8 
# Travail fait par Jessica Potsou

# Je vais importer les modules nécessaires pour utiliser spacy

import csv, spacy
from collections import Counter

# Je vais placer le fichier csv avec lequel  je vais travailler

chronique = "martino.csv"

# Dans les prochaines lignes, je vais ouvrir le fichier dans lequel je veux travailler.
# J'utilise la fonction encoding pour permettre à mon script de lire les caractères qu'il n'arrive pas a lire
# J'utilise la fonction next afin que mon script ne lise pas la première ligne du fichier csv
f = open(chronique, encoding="utf-8") 
interventions = csv.reader(f)
next(interventions)

# Je charge le réseau de neurnes...
tal = spacy.load("fr_core_news_md")

# Je me fais de listes de vides que j'utiliserai plus tard.
tousmots = []
bigrams = []
bigramfinal = []

#Je fais une boucle pour traiter chaque ligne de mon fichier cvs
for inter in interventions:
    # Je créer une variable dans laquelle je met le modèle pour traiter l'information dont j'ai besoin
    # Dans le fichier csv, l'information que je désire traiter est l'élément 3 de ma liste inter.
    doc = tal(inter[3])
    # Avec l'option suivante, je lemmatise le texte
    lemmes = [token.lemma_ for token in doc]
    # print (lemmes)

    # Dans la variable mots de mets les mots lemmatisé auxquels j'enlèves les mots vides et la ponctuation
    mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]

    # Avec dans les prochaines lignes je fais mes paires de mots que j'ajoute à ma liste bigrams
    for x, y in enumerate(mots[:-1]):
        bigrams.append("{} {}".format(mots[x], mots[x+1]))
        # Les commentaires au lignes 52 et 53, permettent de vérifier si mes paires de mots sont bel et bien faites.
    
    #Ceci est la partie que je n'ai pas pas réussi à vérifier à cause de mes problèmes techniques
    # J'ai fait une boucle qui me permet d'appliquer ma condition pour chaque paire de mots. 
    # Si la condition est remplie, le bigram est ajouté à ma liste bigramfinal
    for bigram in bigrams:
        if "islam" or "musulm" in bigram:
            bigramfinal.append(bigram)

# freq1 = Counter(bigrams)
# print (freq1.most_common(50))
# Les deux lignes précédentes fonctionnent. Elles me donnent les 50 paires de mots les plus utilisé ainsi que leur férquence d'utilisation

# Si le code des lignes 48 à 50 fonctionne, les lignes suivantes sont la procédure à suivre.
# Les deux prochaines lignes me me donneront les 50 paires de mots les plus utilisés correspondant à ma condition ainsi que leur fréquence d'utilisation
freq = Counter(bigramfinal)
print (freq.most_common(50))
