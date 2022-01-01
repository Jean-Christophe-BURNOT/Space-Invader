# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
12/12/2021
classe principale pour les ennemis
"""
from tkinter import*




#class qui gère le joueur; affichage + actions
class joueur:
    
    def __init__(self,):
        
        self.master = master
        ComportementFenetre.__init__(self, master)
        self.background = PhotoImage(file = "./Images/space-bg.png", master=self.master)
        self.canvas = Canvas(self.master, width = 100, height = 100,bg="black", borderwidth=-10)
        self.canvas.create_image(0, 0, image = self.background, anchor = "nw")
        self.canvas.pack(fill = "both", expand = True)
        
        #Permet de faire apparaître le vaisseau principal.
        with open('vaisseau.txt',"r") as fichier: #on prend l'image du vaisseau choisi
            filecontent= fichier.readlines()
            fichier.close()
        if "1" in filecontent:
            self.ship = PhotoImage(file = "./Images/spaceShip1.png", master=self.master).subsample(3)
        if "2" in filecontent:
            self.ship = PhotoImage(file = "./Images/spaceShip2.png", master=self.master).subsample(8)
        if "3" in filecontent:
            self.ship = PhotoImage(file = "./Images/spaceShip3.png", master=self.master).subsample(4)
        self.pion = self.canvas.create_image(self.master.winfo_screenwidth()/2,770,image=self.ship)
        self.btnPause = Button(self.master, text="II", font=(None,20), bg="black",fg="white", width=4, relief=RAISED, borderwidth=3, command=self.pause)
        self.btnPause.place(x = 1400, y = 40)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<space>", self.shoot)
        self.listeIlots = []
        self.ilots()
        

    def destruction(self):
        print("hello")




"""
#class qui gère les ennemis; affichage + actions
class ennemis:
    def __init__(self,):
        
    def déplacement(self):
        
    def tir(self):
        
    def destruction(self):




#classe qui gère les ilots (hardcode sauf si on fait des niveaux)
class ilots:
    def __init__(self):
        
    def destruction(self):
"""

