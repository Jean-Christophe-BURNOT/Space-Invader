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

fonctionnalités supplémentaires:
Nous avons ajouté un menu qui permet de choisir entre 3 vaisseaux différents. Il est soumis à une saisie protégée.

__________

Ce programme contient plusieurs méthodes récursives. Dans le sens d'apparition dans le code on retrouve:
	-mvtBonus
	-mouvement
	-shootEnnemis
	-mvtBalleEnnemis
	-mvtBalle

__________

Ce programme possède des implémentations de listes "classique":
On peut citer comme exemple "listeEnnemi". Elle contient tous objets du canvas qui sont les ennemis. Son premier terme correspond à l'ennemi Bonus et le reste aux autres ennemis (5 ennemis "classiques").

__________

Ce programme possède une implémentation de file:
Elle se trouve dans la méthode mvtBonus et gère la vitesse aléatoire de notre vaisseau bonus. Avant d'appeller cette méthode, on génère aléatoirement une liste de 3 valeurs par l'appel de la fonction generateurListe avec la variable selecteur à 2, ces 3 termes sont entre 10 et 60. Cette valeur entre 10 et 60 représente la vitesse de notre vaisseaux bonus. Le vaisseau va prendre la première des valeurs (l'indice 0), il va aller à la vitesse qu'elle contient puis rappeller la fonction avec la même liste mais sans le premier terme. Quand la file arrive à 0 (liste vide) on rappelle la fonction generateurListe avec le selacteur à 2 pour regénérer 3 nouvelles valeurs.


__________

Ce programme possède une implémentation de pile:
Elle se trouve dans la méthode mvtBonus et gère la limite que notre vaisseau peut peut atteindre à droite. Avant d'appeller cette méthode, on génère aléatoirement une liste de 3 valeurs par l'appel de la fonction generateurListe avec la variable selecteur à 1, ces 3 termes sont entre 3000 et 20000. Cette valeur entre 3000 et 20000 représente la limite de droite de notre vaisseaux bonus. Par ce subterfuge l'apparition du vaisseau se fait aléatoirement en fonction du temps qu'il met à atteindre la limite de droite comprise en 3000 et 20000. Le vaisseau va prendre la dernière des valeurs (l'indice -1), il va aller jusqu'a la limite fixée par cette valeur puis, il va revenir à sa position initiale à droite et rappeller la fonction avec la même liste mais sans le dernier terme. Quand la pile arrive à 0 (liste vide) on rappelle la fonction generateurListe avec le selacteur à 1 pour regénérer 3 nouvelles valeurs.

__________

notes générales:

Nous avons dans notre code ajouté un mode fênetré et un mode plein écran, on peut passer de l'un à l'autre en appuyant sur "échap", attention le jeu a été calibré pour une taille d'écran particulière.

Un point qui nous différencie de la version originale est le fait que le joueur doit faire attention avant de tirer puisqu'il ne peut tirer qu'une seule balle à la fois.


