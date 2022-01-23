#Space-Invaders
#Dépôt du projet de CS-DEV "Space-Invaders"

__________

Cette version du Space-Invaders à été réalisée par:
	-Raphaël GUZELIAN
	-Jean-Christophe BURNOT
__________
	
Pour ce projet nous avons utilisé GIT via la plateforme GitHub.
Liens du dépôt: https://github.com/Jean-Christophe-BURNOT/Space-Invaders.git
__________

Ce programme contient plusieurs méthodes récursives. Dans le sens d'apparition dans le code on retrouve:
	-mvtBonus
	-mouvement
	-shootEnnemis
	-mvtBalleEnnemis
	-mvtBalle

__________

Ce programme possède une implémentation de file:
Elle se trouve dans mvtBonus et gère la vitesse aléatoire de notre vaisseau bonus. On a avant d'appeller cette fonction une liste est crée par l'appel de la fonction generateurListe. Elle a 3 termes générées entre 10 et 60. Cette valeur entre 10 et 60 représente la vitesse de notre vaisseaux bonus. Le vaisseau va prendre la première des valeurs, il va aller à la vitesse qu'elle contient puis rappeller la fonction avec la même liste sans le premier terme. Quand file arrive à 0 on rappelle la fonction generateurListe avec le selacteur à 2.


__________

Ce programme possède une implémentation de file:
Elle se trouve dans mvtBonus et gère la distance limite de notre vaisseau bonus. On a avant d'appeller cette fonction une liste est crée par l'appel de la fonction generateurListe. Elle a 3 termes générées entre 3000 et 20000. Cette valeur entre 3000 et 20000 représente la limite qui quand elle sera franchie ramenera notre vaisseau bonus à l'extrémité gauche de l'écran. Par ce subterfuge l'apparition du vaisseau se fait aléatoirement en fonction du temps qu'il met à atteindre la limite. Le vaisseau va prendre la dernière des valeurs, aller jusqu'à la valeur qu'elle contient puis retourner la à sa position initiale à gauche et rappeller la fonction avec la même liste sans le dernier terme. Quand file arrive à 0 on rappelle la fonction generateurListe avec le selacteur à 1.

__________

notes:

Nous avons dans notre code ajouté un mode fênetré et un mode plein écran, on peut passer de l'un à l'autre en appuyant sur "échap", attention le jeu a été calibré pour une taille d'écran particulière

Un point qui nous différencie de la version originale est le fait que le joueur doit faire attention avant de tirer puisqu'il ne peut tirer qu'une seule balle à la fois
