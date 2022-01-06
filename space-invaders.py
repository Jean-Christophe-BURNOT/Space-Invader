#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 07:41:27 2021
 
@author: raphael.guzelian
"""

from tkinter import *
import random



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
        self.master.config(cursor="dotbox")
        
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
                            height=100,
                            borderwidth=-10)
        
        self.canvas.create_image(0, -200, 
                                  image = self.background, 
                                  anchor = "nw")
              
        self.canvas.create_text(800,200,text="Space Invaders",font=("Matura MT Script Capitals",80),fill="blue")
        
        
        self.BoutonJouer = Button(self.master,text="Jouer",
                                  font=("Matura MT Script Capitals",20),
                                  bg="black",fg="white",
                                  width=10,relief=RAISED,
                                  borderwidth=10,
                                  command=self.ouvrir)
        
        self.BoutonQuitter = Button(self.master,text='Quitter',
                                    font=("Matura MT Script Capitals", 20),
                                    bg="black",fg="white",
                                    width=10,relief=RAISED,
                                    borderwidth = 10,
                                    command=self.quitter)
        
        
        # positionnements
        self.canvas.pack(fill = "both", expand = True)
        self.BoutonJouer.place(x=700,y=400)
        self.BoutonQuitter.place(x=700,y=500)

     

    # aller à la page de jeu
    def ouvrir(self):
        self.master.destroy() 
        self.master=Tk() 
        self.app=Personnalisation(self.master)

    # quitter le jeu 
    def quitter(self):
        self.master.destroy()
        
        
        
        
        
# ----------------------------------------------------------------------------                    
# Page de personnalisation
class Personnalisation(ComportementFenetre):
    
    def __init__(self, master):


        self.master = master
        ComportementFenetre.__init__(self, master)
        
        self.background = PhotoImage(file = "./Images/perso-bg.png", 
                                     master=self.master).zoom(2)
 
        self.canvas = Canvas(self.master, 
                             width = 100, 
                             height = 100,bg="black",
                             borderwidth=-10)
        
        
        
        
        self.canvas.create_image(0, -200, 
                                 image = self.background,
                                 anchor="nw")
        
        self.image1 = PhotoImage(file = "./Images/spaceShip1.png", 
                                 master=self.master).subsample(3)
        
        self.canvas.create_image(560, 550, 
                                 image = self.image1)
        self.image2 = PhotoImage(file = "./Images/spaceShip2.png", 
                                 master=self.master).subsample(7)
        
        self.canvas.create_image(820, 550, 
                                 image = self.image2)
        self.image3 = PhotoImage(file = "./Images/spaceShip3.png", 
                                 master=self.master).subsample(3)
        
        self.canvas.create_image(1060, 550, 
                                 image = self.image3)
        
        
        
        self.canvas.pack(fill = "both", expand = True)
        
        self.canvas.create_text(self.master.winfo_screenwidth()/2,200, 
                                text = "Choisissez votre vaisseau",
                                font = ("Matura MT Script Capitals", 50),
                                fill = "white")
        self.myShip1 = IntVar()
        self.ship1 = Checkbutton(self.master,
                                 text = "Select",
                                 font = ("Matura MT Script Capitals", 20),
                                 selectcolor = "black",
                                 bg = 'black',
                                 fg = 'white',
                                 variable = self.myShip1)
        self.myShip2 = IntVar()
        self.ship2 = Checkbutton(self.master,
                                 text = "Select",
                                 font = ("Matura MT Script Capitals", 20),
                                 selectcolor = "black",
                                 bg = 'black',
                                 fg = 'white',
                                 variable = self.myShip2)
        self.myShip3 = IntVar()
        self.ship3 = Checkbutton(self.master,
                                 text = "Select",
                                 font = ("Matura MT Script Capitals", 20),
                                 selectcolor = "black",
                                 bg = 'black',
                                 fg = 'white',
                                 variable = self.myShip3)
           
 

        self.BoutonSuivant = Button(self.master,
                                    text = "Suivant",
                                    font = ("Matura MT Script Capitals", 20),
                                    bg = "black", 
                                    fg = "white",
                                    width = 10,relief = RAISED,borderwidth = 10,
                                    command = self.suivant)
        
        self.BoutonRetour = Button(self.master,
                            text = "Retour",
                            font = ("Matura MT Script Capitals", 20),
                            bg = "black", 
                            fg = "white",
                            width = 10,relief = RAISED,borderwidth = 10,
                            command = self.retour)
        
        
        self.ship1.place(x=510,y=400)
        self.ship2.place(x=self.master.winfo_screenwidth()/2,y=400)
        self.ship3.place(x=1000,y=400)
        self.BoutonSuivant.place(x=1250,y=730)
        self.BoutonRetour.place(x=50,y=730)
        
        
    # aller à la page de jeu
    def suivant(self):
        if self.myShip1.get()==1:#on récupère le vaisseau choisi
            type_vaisseau=1
            pagejeu = PageJeu(self.master, type_vaisseau)
        if self.myShip2.get()==1:
            type_vaisseau=2
            pagejeu = PageJeu(self.master, type_vaisseau)
        if self.myShip3.get()==1:
            type_vaisseau=3
            pagejeu = PageJeu(self.master, type_vaisseau)
            
        
        #sécurité de sélection de vaisseau
        l=[]
        if self.myShip1.get() == True:
            l.append(1)
        if self.myShip2.get() == True:
            l.append(1)
        if self.myShip3.get() == True:
            l.append(1)
            
        if len(l)==0:
            messagebox.showinfo("INFORMATION", 
                                "Veuillez sélectionner un vaisseau")
        elif len(l)>1:
            messagebox.showinfo("INFORMATION", 
                                "Veuillez sélectionner un seul vaisseau")
            
        else:
            self.master.destroy()
            self.master = Tk()
            self.app = PageJeu(self.master, type_vaisseau)
            self.master.mainloop()


    # retour accueil    
    def retour(self):   
        self.master.destroy()
        self.master = Tk()
        self.app = accueil(self.master)
        
        
        
        
        
# ----------------------------------------------------------------------------
#  Création des ennemis      
class Ennemi():
    
    def __init__(self, master, monCanvas): 
        
        self.master=master
        self.canvas=monCanvas
        
        global listeEnnemi
        
        listeEnnemi=[]
        
        self.listeTirsEnnemis = []
   
        self.x = 5
        self.y = 0
        self.ennemis()
        

    def ennemis(self):
        self.ennemi1= PhotoImage(file = "Images/alien1.png", master=self.master).subsample(2)
        self.ennemi2= PhotoImage(file = "Images/alien2.png", master=self.master).subsample(3)
        self.en1 = self.canvas.create_image(self.master.winfo_screenwidth()/2,156,image=self.ennemi2)
        listeEnnemi.append(self.en1)
        
        self.mouvement()
        self.shootEnnemis()
        
        
    def mouvement(self):
        self.canvas.move(self.en1, self.x, self.y)
        self.y=0
        x, y = self.canvas.coords(self.en1)
        if x > self.master.winfo_screenwidth():
            self.x=-5
            self.y=50
        if x < 0:
            self.x=5
            self.y=50
        self.canvas.after(10,self.mouvement)
    
    def shootEnnemis(self):
        a=random.randint(1,5)
        if a==1:
            self.balleEn=self.canvas.create_rectangle(self.canvas.coords(self.en1)[0],self.canvas.coords(self.en1)[1]+20,
                                                    self.canvas.coords(self.en1)[0],self.canvas.coords(self.en1)[1]-5,
                                                    outline="yellow", fill="yellow")
            self.listeTirsEnnemis.append(self.balleEn)
            # self.loadedGun=True
            self.mvtBalleEnnemis()
            self.canvas.after(100,self.shootEnnemis)
        else:
            self.canvas.after(100,self.shootEnnemis)
            
    def mvtBalleEnnemis(self):
        for val in self.listeTirsEnnemis:
            self.canvas.move(val, 0, 30)
            # if self.loadedGun==True:
            #     if self.canvas.coords(val)[1] > self.master.winfo_screenheight(): #si la balle sort de l'écran
            #         self.canvas.delete(val)
            #         self.listeTirsEnnemis.remove(val)
            #         self.loadedGun=False
            if self.canvas.coords(val)[1] > self.master.winfo_screenheight(): #si la balle sort de l'écran
                    self.canvas.delete(val)
                    self.listeTirsEnnemis.remove(val)
                    
            else:
                x0,y0,x1,y1 = self.canvas.coords(val)
                elemTouché = self.canvas.find_overlapping(x0,y0,x1,y1) #liste des éléments touchés par la balle ennemi
                for elem in elemTouché:
                    for ilot in listeIlots: #si un ilot est dans la liste des elem touchés, on le supprime
                        if elem==ilot :
                            self.canvas.delete(ilot)
                            self.canvas.delete(val)
                            self.listeTirsEnnemis.remove(val)

                
                self.canvas.after(100,self.mvtBalleEnnemis)
     
            
# ----------------------------------------------------------------------------                    
# Page de jeu
class PageJeu(ComportementFenetre):
    
    def __init__(self, master, type_vaisseau):
        

        self.master = master
        ComportementFenetre.__init__(self, master)

        self.background = PhotoImage(file = "./Images/space-bg.png", 
                                     master=self.master)
                
        self.canvas = Canvas(self.master, 
                             width = 100, 
                             height = 100,bg="black",
                             borderwidth=-10)
        
        self.canvas.create_image(0, 0, 
                                 image = self.background, 
                                 anchor = "nw")
        
        self.canvas.pack(fill = "both", expand = True)
        
        
        monCanvas=self.canvas
        myCanvas = Ennemi(master,monCanvas)
        
        
        
        self.typeVaisseau = type_vaisseau
        if self.typeVaisseau==1:
            self.ship = PhotoImage(file = "./Images/spaceShip1.png", master=self.master).subsample(4)
        if self.typeVaisseau==2:
            self.ship = PhotoImage(file = "./Images/spaceShip2.png", master=self.master).subsample(9)
        if self.typeVaisseau==3:
            self.ship = PhotoImage(file = "./Images/spaceShip3.png", master=self.master).subsample(5)

            
            
        self.pion = self.canvas.create_image(self.master.winfo_screenwidth()/2,770,image=self.ship)

        
        self.btnMenu = Button(self.master,text="Menu",
                               font=("Matura MT Script Capitals", 20),
                               bg="black",fg="white",
                               width=4,relief=RAISED,
                               borderwidth=3,
                               command=self.menu)
        
        self.btnQuitter = Button(self.master,text="Quitter",
                               font=("Matura MT Script Capitals", 20),
                               bg="black",fg="white",
                               width=4,relief=RAISED,
                               borderwidth=3,
                               command=self.quitter)
        
        self.btnMenu.place(x=1250,y=30)
        self.btnQuitter.place(x=1400,y=30)

        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<space>", self.shoot)
        
        self.myScore = Label(self.master, 
                         text = "Score :         ",
                         font = ("Matura MT Script Capitals", 25),
                         bg = "black", 
                         fg = "white")
        
        self.myVie = Label(self.master, 
                         text = "Vie restante :",
                         font = ("Matura MT Script Capitals", 25),
                         bg = "black", 
                         fg = "white")
        
        self.myScore.place(x=50,y=30)
        self.myVie.place(x=50,y=80)
        self.vie=3 


        global listeIlots
        listeIlots=[]
        self.ilots()
        
        
         
    def move_right(self, event):
        self.canvas.move(self.pion, 10, 0)
        if self.canvas.coords(self.pion)[0] > self.master.winfo_screenwidth():
            self.canvas.move(self.pion, -20, 0)
        
       
    def move_left(self, event):
        self.canvas.move(self.pion, -10, 0)
        if self.canvas.coords(self.pion)[0] < -20:
            self.canvas.move(self.pion, 20, 0)
            
    
    def shoot(self,event):   
        self.balle=self.canvas.create_rectangle(self.canvas.coords(self.pion)[0],self.canvas.coords(self.pion)[1]-30,
                                                self.canvas.coords(self.pion)[0],self.canvas.coords(self.pion)[1]-50,
                                                outline="yellow",
                                                fill="yellow")
        self.master.unbind("<space>") #pour ne pas tirer plusieurs balles à la suite
        self.loadedGun=True
        self.mvtBalle()


    def mvtBalle(self):
        if self.loadedGun==True: 
            if self.canvas.coords(self.balle)[1] < 0: #si la balle sort de l'écran
                self.canvas.delete(self.balle)
                self.master.bind("<space>", self.shoot) #on peut retirer
                self.loadedGun=False
            else:                               
                self.canvas.move(self.balle, 0, -30)                
                x0,y0,x1,y1 = self.canvas.coords(self.balle)
                elemTouché = self.canvas.find_overlapping(x0,y0,x1,y1) #liste des éléments touchés par la balle
                
                for elem in elemTouché:
                    for ilot in listeIlots: #si un ilot est dans la liste des elem touchés, on le supprime
                        if elem==ilot :
                            self.canvas.delete(ilot)
                            self.canvas.delete(self.balle)
                            self.loadedGun=False
                            self.master.bind("<space>",self.shoot)
                    for ennemi in listeEnnemi: #si un ennemi est dans la liste des elem touchés, on le supprime
                        if elem==ennemi:
                            self.canvas.delete(ennemi)
                            self.canvas.delete(self.balle)
                            self.master.bind("<space>",self.shoot)
                self.master.after(100,self.mvtBalle)

        


    def ilots(self):
        #bloc 1
        for i in range(1,8):
            self.b1=self.canvas.create_rectangle(170+i*30,640, #ligne 1
                                         200+i*30,670,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b1)
            self.b1=self.canvas.create_rectangle(170+i*30,610, #ligne 2
                                         200+i*30,640,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b1)
            self.b1=self.canvas.create_rectangle(170+i*30,580, #ligne 3
                                         200+i*30,610,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b1)

        
        #bloc 2
        for i in range(1,8):
            self.b2=self.canvas.create_rectangle(630+i*30,640, #ligne 1
                                         660+i*30,670,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b2)
            self.b2=self.canvas.create_rectangle(630+i*30,610, #ligne 2
                                         660+i*30,640,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b2)
            self.b2=self.canvas.create_rectangle(630+i*30,580, #ligne 3
                                         660+i*30,610,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b2)
        
        #bloc 3
        for i in range(1,8):
            self.b3=self.canvas.create_rectangle(1090+i*30,640, #ligne 1
                                         1120+i*30,670,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b3)
            self.b3=self.canvas.create_rectangle(1090+i*30,610, #ligne 2
                                         1120+i*30,640,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b3)
            self.b3=self.canvas.create_rectangle(1090+i*30,580, #ligne 3
                                         1120+i*30,610,
                                         outline="black",
                                         fill="brown",
                                         tags="mur")
            listeIlots.append(self.b3)
            
          

    











    def menu(self):
        self.master.destroy() 
        self.master=Tk() 
        self.app=accueil(self.master)

        
    def quitter(self):
        self.master.destroy()
            

# ----------------------------------------------------------------------------              
# fonction principale 
def main(): 
    root = Tk()
    app = accueil(root)
    root.mainloop()
    
# lancement du programme 
if __name__ == '__main__':
    main()
