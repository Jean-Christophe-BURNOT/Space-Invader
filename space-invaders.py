#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 07:41:27 2021

@author: raphael.guzelian
"""

from tkinter import *


# ----------------------------------------------------------------------------        
# comportements fenêtre

class ComportementFenetre():
    
    # attributs
    def __init__(self,master):
        self.master=master
        self.master.attributes("-fullscreen",True)  
        self.fullScreenState = False
        self.master.bind("<F2>",self.toggleFullScreen)
        self.master.bind("<Escape>",self.quitFullScreen)
        self.master.title('Space Invaders')
        
    # mode plein écran
    def toggleFullScreen(self,event):
        self.fullScreenState=not self.fullScreenState
        self.master.attributes("-fullscreen",self.fullScreenState)

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
        position_x=screen_x//2-window_x//2
        position_y=screen_y//2-window_y//2
        geo="{}x{}+{}+{}".format(window_x,window_y,position_x,position_y)
        self.master.geometry(geo)
   
        
# ----------------------------------------------------------------------------        
# Page d'accueil

class accueil(ComportementFenetre):
    
    # attributs GUI
    def __init__(self,master):

        self.master=master
        
        # héritage de la classe ComportementFenetre
        ComportementFenetre.__init__(self,master)
        
        self.background=PhotoImage(file="./Images/menu-bg.png",master=self.master)
        
        self.canvas=Canvas(self.master,
                           width=100,
                           height=100)
        
        self.canvas.create_image(0, 0, 
                                 image = self.background, 
                                 anchor = "nw")
              
        self.canvas.create_text(950,200,text="Space Invaders",font=("Matura MT Script Capitals",80),fill="blue")
        
        
        self.BoutonJouer = Button(self.master,text="Jouer",font=("Matura MT Script Capitals",20),bg="black", fg="white",width=10,relief=RAISED,borderwidth=10,command=self.ouvrir)
        self.BoutonQuitter = Button(self.master,text='Quitter',font=("Matura MT Script Capitals", 20),bg="black",fg="white",width=10,relief=RAISED,borderwidth = 10,command=self.quitter)
        
        
        # positionnements
        self.canvas.pack(fill = "both", expand = True)
        self.BoutonJouer.place(x=800,y=400)
        self.BoutonQuitter.place(x=800,y=500)

     

    # aller à la page de jeu
    def ouvrir(self):
        self.master.destroy() 
        self.master=Tk() 
        self.app=PageJeu(self.master)
        self.master.mainloop()

    # quitter le jeu 
    def quitter(self):
        self.master.destroy()
    

# ----------------------------------------------------------------------------                    
# Page de jeu
class PageJeu(ComportementFenetre):
    # attributs GUI 
    def __init__(self,master):
        self.master = master

        # héritage de la classe ComportementFenetre
        ComportementFenetre.__init__(self, master)
        
        self.background = PhotoImage(file = "./Images/space-bg.png", 
                                     master=self.master)
        
        self.canvas = Canvas(self.master, 
                             width = 100, 
                             height = 100)
        
        self.canvas.create_image(0, 0, 
                                 image = self.background, 
                                 anchor = "nw")
        
        self.canvas.pack(fill = "both", expand = True)
        
        
        
        
        
        self.PosX=self.master.winfo_screenwidth()/2
        self.PosY=950
        
        self.pion = self.canvas.create_oval(self.PosX-10,
                                            self.PosY-10,
                                            self.PosX+10,
                                            self.PosY+10,
                                            width=10,
                                            outline="red",
                                            fill="red")
        self.canvas.focus_set()
        self.canvas.bind('<Key>',self.Clavier)
        
    def Clavier(self,event):
        
        self.touche = event.keysym
        
        limitX=self.master.winfo_screenwidth()
        limitY=800
        
        
        if self.touche == 'z':
            self.PosY -=20
            if self.PosY < limitY:
                self.PosY = limitY+20
        if self.touche == 's':
            self.PosY +=20
            if self.PosY > self.master.winfo_screenheight() :
                self.PosY = self.master.winfo_screenheight()-20
        if self.touche == 'd':
            self.PosX +=20
            if self.PosX > limitX:
                self.PosX = limitX-20
        if self.touche == 'q':
            self.PosX -=20
            if self.PosX < 0:
                self.PosX = 20
            
            
        self.canvas.coords(self.pion, 
                           self.PosX-10,
                           self.PosY-10,
                           self.PosX+10,
                           self.PosY+10,)
        
        

        
# ----------------------------------------------------------------------------              
# fonction principale 
def main(): 
    
    root = Tk()
    app = accueil(root)
    root.mainloop()
    
    
# lancement du programme 

if __name__ == '__main__':
    main()
