#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
12/12/2021
Programme principal pour démarrer le space invaders
"""
from tkinter import*
from spaceInvaders import ComportementFenetre, accueil, PageJeu

def main(): 
    
    root = Tk()
    app = accueil(root)
    root.mainloop()
    
    
# lancement du programme 

if __name__ == '__main__':
    main()
