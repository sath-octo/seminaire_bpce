# Séminaire BPCE
---

Au cours de ce TP, nous allons vous demander de travailler en binôme.

## Partie 1

***Un peu d'histoire:***

**Pêcheur 1** pêche le Sandre dans le Maine et Loire, et **Pêcheur 2** pêche le Brochet dans l’Indre-et-Loire, mais ils sont aussi développeurs !
Ils veulent créer un script bash pour récupérer le nombre de poissons pêchés dans leur département entre 2018 et 2022.
Ils récupèrent un script bash incomplet.

***Partie technique:***

*Pour la réalisation de cette partie du TP, vous devez:*

- Cloner un répertoire git sur votre environnement de travail.
- Vous rendre sur la branche bash
- À partir de la branche bash créer une nouvelle branche nommée bash_<VOTRE_NOM>
- Compléter le script bash existant (#FIXME) pour que le programme retourne:

```shell
$ bash main.sh
Nombre de Sandre pêchés dans le Maine-et-Loire entre 2018 et 2022:  28 
```
ou
```shell
$ bash main.sh
Nombre de Brochets pêchés dans l'Indre-et-Loire entre 2018 et 2022:  73 
```

- Pousser votre travail sur le dépôt git distant


## Partie 2

***Un peu d'histoire:***

Pêcheur 1 et Pêcheur 2 décident de mutualiser leur travail en mettant en commun leurs codes.
Ils décident de créer une seule version du programme bash comportant les deux fonctionnalités implémentées dans l'étape précédente.

***Partie technique:***

(Cette partie du TP se réalise en binôme).

*Pour la réalisation de cette partie du TP, vous devez:*

- Vous rendre sur la branche bash
- Créer une nouvelle branche depuis la branche bash que vous appelez bash_<NOM_PECHEUR_1>_<NOM_PECHEUR_2>
- Merger les branches bash_<NOM_PECHEUR_1> & bash_<NOM_PECHEUR_2> sur la branche bash_<NOM_PECHEUR_1>_<NOM_PECHEUR_2>
- Corriger les conflits si il y en a, et modifier le code pour qu'il affiche:
```shell
$ bash main.sh
Nombre de Sandre pêchés dans le Maine et Loire entre 2018 et 2022:  28
Nombre de Brochets pêchés dans l'Indre et Loire entre 2018 et 2022:  73 
```
- Pousser votre travail sur le dépôt distant

## Partie 3

***Un peu d'histoire:***

**Pêcheur 1** et **Pêcheur 2**, dans un souci de portabilité, de maintenance et de lisibilité aimeraient transcrire leur script bash en **python**. Heureusement dans les sources récupérées un bout de code python existe déjà, finissez de développer ce programme.

***Partie technique:***

(Cette partie du TP se réalise en binôme).

*Pour la réalisation de cette partie du TP, vous devez:*

- Vous rendre sur la branche **python**
- Créer une nouvelle branche appelée **python_<NOM_PECHEUR_1>_<NOM_PECHEUR_2>**
- Finir d'implémenter le programme python pour qu'il affiche:
```shell
$ python3 main.py
Nombre de Sandre pêchés dans le Maine et Loire entre 2018 et 2022:  28
Nombre de Brochets pêchés dans l'Indre et Loire entre 2018 et 2022:  73 
```
- Pousser votre travail sur le dépôt distant

## BONUS

Si vous avez de l'avance, compléter le programme python pour qu'il affiche des informations supplémentaires:
- La commune sur laquelle il y a eu le plus de prises
- La taille moyenne des prises


```shell
Sandre:
Nombre de Sandre pêchés dans le Maine et Loire entre 2018 et 2022: 28
Meilleur commune: LE LION-D'ANGERS avec 14 prise(s)
Taille moyenne: 231.21428571428572 mm

Brochet:
Nombre de Brochets pêchés dans l'Indre et Loire entre 2018 et 2022: 73
Meilleur commune: CANDES-SAINT-MARTIN avec 29 prise(s)
Taille moyenne: 335.2191780821918 mm
```