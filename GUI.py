#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:51:08 2021

@author: terramotu
Ce programme est l'interface graphique du Space-Invaders
"""
from tkinter import *




#Classe qui définit le comportement graphique de toutes les fenêtres
class ComportementFenetre():
    
    def __init__(self, master):
        self.master=master
        self.master.attributes("-fullscreen", True)  
        self.fullScreenState = False
        self.master.bind("<F2>", self.toggleFullScreen)
        self.master.bind("<Escape>", self.quitFullScreen)
        self.master.title('Space-Invaders')
        self.master.config(cursor = "dotbox")
        
    # mode plein écran
    def toggleFullScreen(self, event):
        self.fullScreenState=not self.fullScreenState
        self.master.attributes("-fullscreen", self.fullScreenState)

    # sortir du plein écran
    def quitFullScreen(self,event):
        self.fullScreenState=False
        self.master.attributes("-fullscreen",self.fullScreenState)
        # récupération des dimensions de l'écran
        screen_x = self.master.winfo_screenwidth()
        screen_y = self.master.winfo_screenheight()
        window_x = 1080
        window_y = 720
        # centrage automatique
        position_x = screen_x//2-window_x//2
        position_y = screen_y//2-window_y//2
        geo = "{}x{}+{}+{}".format(window_x, window_y, position_x, position_y)
        self.master.geometry(geo)
        



#Classe qui s'occupe de la page d'accueil
class accueil(ComportementFenetre):
    
    # attributs GUI
    def __init__(self, master):
        self.master = master
        # héritage de la classe ComportementFenetre
        ComportementFenetre.__init__(self, master)
        self.background=PhotoImage(file="./Images/menu-bg.png", master=self.master)
        self.canvas=Canvas(self.master, width=100, height=100, borderwidth=-10)
        self.canvas.create_image(0, -200,image = self.background, anchor = "nw")
        self.canvas.create_text(800,200,text="Space Invaders",font=("Matura MT Script Capitals",80),fill="blue")
        self.BoutonJouer = Button(self.master,text="Jouer", font=("Matura MT Script Capitals",20), bg="black",fg="white", width=10,relief=RAISED, borderwidth=10, command=self.ouvrir) 
        self.BoutonQuitter = Button(self.master,text='Quitter', font=("Matura MT Script Capitals", 20), bg="black", fg="white", width=10, relief=RAISED, borderwidth = 10, command=self.quitter)
        # positionnements
        self.canvas.pack(fill = "both", expand = True)
        self.BoutonJouer.place(x=700,y=400)
        self.BoutonQuitter.place(x=700,y=500)

    # aller à la page de jeu
    def ouvrir(self):
        self.master.destroy() 
        self.master=Tk() 
        self.app=Personnalisation(self.master)
        self.master.mainloop()

    # quitter le jeu 
    def quitter(self):
        self.master.destroy()




#Classe qui s'occupe de la page de choix du vaisseaux
class Personnalisation(ComportementFenetre):
    
    def __init__(self,master):
        self.master = master
        ComportementFenetre.__init__(self, master)
        self.background = PhotoImage(file = "./Images/perso-bg.png", master=self.master).zoom(2)
        self.canvas = Canvas(self.master, width = 100, height = 100,bg="black", borderwidth=-10)
        self.canvas.create_image(0, -200, image = self.background, anchor="nw")
        self.image1 = PhotoImage(file = "./Images/spaceShip1.png", master=self.master).subsample(3)
        self.canvas.create_image(560, 550, image = self.image1)
        self.image2 = PhotoImage(file = "./Images/spaceShip2.png", master=self.master).subsample(7)
        self.canvas.create_image(820, 550, image = self.image2)
        self.image3 = PhotoImage(file = "./Images/spaceShip3.png", master=self.master).subsample(3)
        self.canvas.create_image(1060, 550, image = self.image3)
        self.canvas.pack(fill = "both", expand = True)
        self.canvas.create_text(self.master.winfo_screenwidth()/2,200, text = "Choisissez votre vaisseau", font = ("Matura MT Script Capitals", 50), fill = "white")
        self.myShip1 = IntVar()
        self.ship1 = Checkbutton(self.master, text = "Select", font = ("Matura MT Script Capitals", 20), selectcolor = "black", bg = 'black', fg = 'white', variable = self.myShip1)
        self.myShip2 = IntVar()
        self.ship2 = Checkbutton(self.master, text = "Select", font = ("Matura MT Script Capitals", 20), selectcolor = "black", bg = 'black', fg = 'white', variable = self.myShip2)
        self.myShip3 = IntVar()
        self.ship3 = Checkbutton(self.master, text = "Select", font = ("Matura MT Script Capitals", 20), selectcolor = "black", bg = 'black', fg = 'white', variable = self.myShip3)
        self.BoutonSuivant = Button(self.master, text = "Suivant", font = ("Matura MT Script Capitals", 20), bg = "black", fg = "white", width = 10,relief = RAISED,borderwidth = 10, command = self.suivant)
        self.BoutonRetour = Button(self.master, text = "Retour", font = ("Matura MT Script Capitals", 20), bg = "black", fg = "white", width = 10,relief = RAISED,borderwidth = 10, command = self.retour)
        #Attributs de position des vaisseaux
        self.ship1.place(x=510,y=400)
        self.ship2.place(x=self.master.winfo_screenwidth()/2,y=400)
        self.ship3.place(x=1000,y=400)
        self.BoutonSuivant.place(x=1250,y=730)
        self.BoutonRetour.place(x=50,y=730)
        
    #aller à la page de jeu
    def suivant(self):
        with open('vaisseau.txt',"w") as fichier: #on associe à chaque vaisseau un chiffre
            if self.myShip1.get()==1:
                fichier.write(str(1))
            if self.myShip2.get()==1:
                fichier.write(str(2))
            if self.myShip3.get()==1:
                fichier.write(str(3))
        fichier.close()
        #saisie protégée
        l=[]
        if self.myShip1.get() == True:
            l.append(1)
        if self.myShip2.get() == True:
            l.append(1)
        if self.myShip3.get() == True:
            l.append(1)  
        if len(l)==0:
            messagebox.showinfo("INFORMATION", "Veuillez sélectionner un vaisseau")
        if len(l) > 1:
            messagebox.showinfo("INFORMATION", "Veuillez sélectionner un seul vaisseau")
        else:
            self.master.destroy()
            self.master = Tk()
            #génère la page suivante et la stocke dans "self.app"
            
            self.app = PageJeu(self.master)
            self.master.mainloop()

    # retour accueil    
    def retour(self):   
        self.master.destroy()
        self.master = Tk()
        self.app = accueil(self.master)
        self.master.mainloop()




#Classe qui s'occupe de la page de jeu
class PageJeu(ComportementFenetre):
   
    #permet de lancer le mécanisme de jeu
    def __init__(self, master):
        self.master = master
        ComportementFenetre.__init__(self, master)
        self.background = PhotoImage(file = "./Images/space-bg.png", master=self.master)
        self.canvas = Canvas(self.master, width = 100, height = 100,bg="black", borderwidth=-10)
        self.canvas.create_image(0, 0, image = self.background, anchor = "nw")
        self.canvas.pack(fill = "both", expand = True)
        joueur(self.master)
        