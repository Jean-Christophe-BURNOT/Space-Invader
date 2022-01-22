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
        self.master = master
        self.master.attributes("-fullscreen",True)  
        self.fullScreenState = False
        self.master.bind("<F2>",self.toggleFullScreen)
        self.master.bind("<Escape>",self.quitFullScreen)
        self.master.title('Space Invaders')
        self.master.config(cursor="dotbox")
        
    # mode plein écran
    def toggleFullScreen(self,event):
        self.fullScreenState = not self.fullScreenState
        self.master.attributes("-fullscreen",self.fullScreenState)

    # sortir du plein écran
    def quitFullScreen(self,event):
        self.fullScreenState = False
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

        self.master = master
        
        # héritage de la classe ComportementFenetre
        ComportementFenetre.__init__(self,master)
        

        self.background = PhotoImage(file="./Images/menu-bg.png",master = self.master)
        

        self.canvas=Canvas(self.master,
                            width = 100,
                            height = 100,
                            borderwidth = -10)
        
        self.canvas.create_image(0, -200, 
                                  image = self.background, 
                                  anchor = "nw")
              
        self.canvas.create_text(800,200,text = "Space Invaders",font = ("Matura MT Script Capitals",80),fill = "blue")
        
        
        self.BoutonJouer = Button(self.master,text = "Jouer",
                                  font = ("Matura MT Script Capitals",20),
                                  bg = "black",fg="white",
                                  width = 10,relief=RAISED,
                                  borderwidth = 10,
                                  command = self.ouvrir)
        
        self.BoutonQuitter = Button(self.master,text = 'Quitter',
                                    font = ("Matura MT Script Capitals", 20),
                                    bg = "black",fg = "white",
                                    width = 10,relief = RAISED,
                                    borderwidth = 10,
                                    command = self.quitter)
        
        
        # positionnements
        self.canvas.pack(fill = "both", expand = True)
        self.BoutonJouer.place(x = 700,y = 400)
        self.BoutonQuitter.place(x = 700,y = 500)

     

    # aller à la page de jeu
    def ouvrir(self):
        self.master.destroy() 
        self.master = Tk() 
        self.app = Personnalisation(self.master)

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
                                     master = self.master).zoom(2)
 
        self.canvas = Canvas(self.master, 
                             width = 100, 
                             height = 100,bg = "black",
                             borderwidth = -10)
        
        
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
        
        
        self.ship1.place(x = 510,y = 400)
        self.ship2.place(x = self.master.winfo_screenwidth()/2,y = 400)
        self.ship3.place(x = 1000,y = 400)
        self.BoutonSuivant.place(x = 1250,y = 730)
        self.BoutonRetour.place(x = 50,y = 730)
        
        
    # aller à la page de jeu
    def suivant(self):
        
        #sécurité de sélection de vaisseau
        l=[]
        if self.myShip1.get() == True:
            l.append(1)
        if self.myShip2.get() == True:
            l.append(1)
        if self.myShip3.get() == True:
            l.append(1)
            
        if len(l) == 0:
            messagebox.showinfo("INFORMATION", 
                                "Veuillez sélectionner un vaisseau")
        elif len(l) > 1:
            messagebox.showinfo("INFORMATION", 
                                "Veuillez sélectionner un seul vaisseau")
            
        #on récupère le vaisseau choisi
        if self.myShip1.get() == 1 and len(l) == 1:
            type_vaisseau = 1
            pagejeu = PageJeu(self.master, type_vaisseau)
        if self.myShip2.get() == 1 and len(l) == 1:
            type_vaisseau = 2
            pagejeu = PageJeu(self.master, type_vaisseau)
        if self.myShip3.get() == 1 and len(l) == 1:
            type_vaisseau = 3
            pagejeu = PageJeu(self.master, type_vaisseau)
        

        if len(l) == 1:
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
    
    def __init__(self, master, monCanvas, monPion): 
        
        self.master = master
        self.canvas = monCanvas
        self.pion = monPion
        
        global listeEnnemi
        listeEnnemi = []
        
        self.listeTirsEnnemis = []
        #cree une pile et une file
        self.pile = self.generateurListe(1)
        self.file = self.generateurListe(2)
        
        self.ennemis()
        
        self.vie = 1000
        self.myVie = Label(self.master, 
                           text = "Vie restante : "+str(self.vie),
                           font = ("Matura MT Script Capitals", 25),
                           bg = "black", 
                           fg = "white")
        
        self.myVie.place(x = 0,y = 0)
        #appelle la methode qui génère une liste pour randomiser la fréquence d'apparition de l'ennemi bonus
        
        

    def ennemis(self):
        self.enBonus = PhotoImage(file = "Images/alien1.png", master = self.master).subsample(4)
        self.ennemiBonus = self.canvas.create_image(0,100,image = self.enBonus)
        listeEnnemi.append(self.ennemiBonus)
        
        #appelle la fonction qui permet le déplacement de l'ennemi
        self.mvtBonus(self.ennemiBonus)
        
       
        
        self.ennemi2 = PhotoImage(file = "Images/alien2.png", master = self.master).subsample(3)
        
        
        for i in range(1,6):
            self.en = self.canvas.create_image(0+i*130,165,image = self.ennemi2)
            listeEnnemi.append(self.en)
            
        #fais les appels adéquats pour les methodes     
        self.mouvement(10, 0)
        self.shootEnnemis()

    """
    fonction qui génère aléatoirement des liste
    avec des valeurs adéquates pour que les fonction qui suivent
    puissent les utiliser comme des piles ou des files
    """
    def generateurListe(self,selecteur):
        if selecteur==1:
            liste1=[]
            for i in range(3):
                i=random.randint(3000,20000)
                liste1.append(i)
            return liste1
        elif selecteur==2:
            liste2=[]
            for i in range(3):
                i=random.randint(10,60)
                liste2.append(i)
            return liste2
    
    
    
    
    
    def mvtBonus(self, bonus):
        
        if self.file==[]:
            self.file=self.generateurListe(2)
        self.canvas.move(self.ennemiBonus,self.file[0],0)
        
        if self.pile==[]:
            self.pile=self.generateurListe(1)
            
            
        if self.canvas.coords(bonus)[0] >= self.pile[-1]:
            
            self.canvas.coords(bonus,0,100)
            self.pile = self.pile[:-1]
            self.file= self.file[1:]
        self.master.after(15,self.mvtBonus,self.ennemiBonus)
      
    
    #Méthode qui permet de déplacer la vague d'ennemis
    def mouvement(self,x,y):
        # valeurs limite de l'écran
        limiteD = self.master.winfo_screenwidth()
        limiteG = 0
        for ennemi in listeEnnemi[1:]:
            self.canvas.move(ennemi, x, y)
            self.collision()
            posVagueD = self.canvas.coords(listeEnnemi[1:][-1])[0]
            posVagueG = self.canvas.coords(listeEnnemi[1:][0])[0]
            if posVagueD >= limiteD:
                #print("<<<<<limite droite atteinte>>>>>")
                for ennemi in listeEnnemi[1:]:
                    self.canvas.move(ennemi,-10,10)
                    self.collision()
                x = -x
            if posVagueG <= limiteG:
                #print("<<<<<limite gauche atteinte>>>>>")
                for ennemi in listeEnnemi[1:]:
                    self.canvas.move(ennemi,10,10)
                    self.collision()
                x = -x
        self.master.after(30, self.mouvement, x, y)
        
    """          
    
    bonnes pratiques
    dossier final
    """
    
    def shootEnnemis(self): 
        for ennemi in listeEnnemi[1:]:
            a=random.randint(1,10)
            if a == 1:
                self.balleEn = self.canvas.create_rectangle(self.canvas.coords(ennemi)[0],self.canvas.coords(ennemi)[1]+20,
                                                        self.canvas.coords(ennemi)[0],self.canvas.coords(ennemi)[1]-5,
                                                        outline = "yellow", fill = "yellow")
                self.listeTirsEnnemis.append(self.balleEn)
    
                self.mvtBalleEnnemis(self.balleEn) 
        self.canvas.after(300,self.shootEnnemis)
            
            
            
    def mvtBalleEnnemis(self,balleEn):
         
            self.canvas.move(balleEn, 0, 30)
            
            #si la balle sort de l'écran
            if self.canvas.coords(balleEn)[1] > self.master.winfo_screenheight(): 
                    self.canvas.delete(balleEn) 
                    self.listeTirsEnnemis.remove(balleEn)
                    
            else:
                x0,y0,x1,y1 = self.canvas.coords(balleEn)
                
                #liste des éléments touchés par la balle ennemi
                elemTouchéBalleEnnemi = self.canvas.find_overlapping(x0,y0,x1,y1)
                
                #si un ilot est dans la liste des elem touchés, on le supprime
                for elem in elemTouchéBalleEnnemi:
                    for ilot in listeIlots: 
                        if elem == ilot :
                            self.canvas.delete(ilot)
                            self.canvas.delete(balleEn)
                            self.listeTirsEnnemis.remove(balleEn)
                            
                    if elem == self.pion:
                        self.vie -= 1
                        self.myVie.config(text="Vie restante : "+str(self.vie))
                        if self.vie == 0:
                            self.canvas.delete(self.pion)
                            messagebox.showinfo("INFORMATION", 
                                "Vous avez perdu")
                        self.canvas.delete(balleEn)
                        self.listeTirsEnnemis.remove(balleEn)
           
                self.canvas.after(100,self.mvtBalleEnnemis,balleEn)
                

                
                
                
    def collision(self):
        for ennemi in listeEnnemi[1:]:
            x,y = self.canvas.coords(ennemi)
            limit=50
            if abs(self.canvas.coords(ennemi)[0] - self.canvas.coords(self.pion)[0]) < limit and abs(self.canvas.coords(ennemi)[1] - self.canvas.coords(self.pion)[1]) < limit:
                self.canvas.delete(self.pion)
                self.canvas.delete(ennemi)
                listeEnnemi[1:].remove(ennemi)
                messagebox.showinfo("INFORMATION", 
                                    "Vous avez perdu")

                
                
        
        
                    
            
        
                
                
     
            
# ----------------------------------------------------------------------------                    
# Page de jeu
class PageJeu(ComportementFenetre):
    
    def __init__(self, master, type_vaisseau):
        

        self.master = master
        
        #fait l'héritage des classes
        
        ComportementFenetre.__init__(self, master)

        self.background = PhotoImage(file = "./Images/space-bg.png", 
                                     master=self.master)
                
        self.canvas = Canvas(self.master, 
                             width = 100, 
                             height = 100,bg = "black",
                             borderwidth = -10)
        
        self.canvas.create_image(0, 0, 
                                 image = self.background, 
                                 anchor = "nw")
        
        self.canvas.pack(fill = "both", expand = True)
        
        
    
        
        self.typeVaisseau = type_vaisseau
        if self.typeVaisseau == 1:
            self.ship = PhotoImage(file = "./Images/spaceShip1.png", master = self.master).subsample(4)
        if self.typeVaisseau == 2:
            self.ship = PhotoImage(file = "./Images/spaceShip2.png", master = self.master).subsample(9)
        if self.typeVaisseau == 3:
            self.ship = PhotoImage(file = "./Images/spaceShip3.png", master = self.master).subsample(5)

            
            
        self.pion = self.canvas.create_image(self.master.winfo_screenwidth()/2,770,image = self.ship)
        
        global listeIlots
        listeIlots = []
        self.ilots()
        
        monPion = self.pion      
        monCanvas = self.canvas
        myCanvas = Ennemi(master, monCanvas, monPion)
        

        
        self.btnMenu = Button(self.master,text = "Menu",
                               font = ("Matura MT Script Capitals", 20),
                               bg = "black",fg = "white",
                               width = 4,relief = RAISED,
                               borderwidth = 3,
                               command = self.menu)
        
        self.btnQuitter = Button(self.master,text = "Quitter",
                               font = ("Matura MT Script Capitals", 20),
                               bg = "black",fg = "white",
                               width = 4,relief = RAISED,
                               borderwidth = 3,
                               command = self.quitter)
        
        self.btnMenu.place(x = 1300,y = 0)
        self.btnQuitter.place(x = 1442,y = 0)

        
        self.score = 0
        self.myScore = Label(self.master, 
                         text = "Score : "+str(self.score),
                         font = ("Matura MT Script Capitals", 25),
                         bg = "black", 
                         fg = "white")
        self.myScore.place(x = 0,y = 50)
        
        self.master.bind("<Right>", self.moveRight)
        self.master.bind("<Left>", self.moveLeft)
        self.master.bind("<space>", self.shoot)
        
        
         
    def moveRight(self, event):
        self.canvas.move(self.pion, 10, 0)
        if self.canvas.coords(self.pion)[0] > self.master.winfo_screenwidth():
            self.canvas.move(self.pion, -20, 0)
        
       
    def moveLeft(self, event):
        self.canvas.move(self.pion, -10, 0)
        if self.canvas.coords(self.pion)[0] < -20:
            self.canvas.move(self.pion, 20, 0)
            
    
    def shoot(self,event):   
        self.balle=self.canvas.create_rectangle(self.canvas.coords(self.pion)[0],self.canvas.coords(self.pion)[1]-30,
                                                self.canvas.coords(self.pion)[0],self.canvas.coords(self.pion)[1]-50,
                                                outline = "yellow",
                                                fill = "yellow")
        #pour ne pas tirer plusieurs balles à la suite
        self.master.unbind("<space>")
        
        self.loadedGun=True
        self.mvtBalle()


    def mvtBalle(self):
        if self.loadedGun == True:
            #si la balle sort de l'écran
            if self.canvas.coords(self.balle)[1] < 0: 
                self.canvas.delete(self.balle)
                self.master.bind("<space>", self.shoot) 
                self.loadedGun = False
            else:                               
                self.canvas.move(self.balle, 0, -30)                
                x0,y0,x1,y1 = self.canvas.coords(self.balle)
                #liste des éléments touchés par la balle
                elemTouchéBalleJoueur = self.canvas.find_overlapping(x0,y0,x1,y1)
                
                for elem in elemTouchéBalleJoueur:
                    
                    #si un ilot est dans la liste des elem touchés, on le supprime
                    for ilot in listeIlots: 
                        if elem == ilot :
                            self.canvas.delete(ilot)
                            self.canvas.delete(self.balle)
                            self.loadedGun=False
                            self.master.bind("<space>",self.shoot)
                    
                    #si un ennemi est dans la liste des elem touchés, on le supprime
                    for ennemi in listeEnnemi[1:]:
                        if elem == ennemi:
                            self.canvas.delete(ennemi)
                            listeEnnemi.remove(ennemi)
                            self.canvas.delete(self.balle)
                            self.score += 20
                            self.myScore.config(text="Score : "+str(self.score))
                            self.master.bind("<space>",self.shoot)  
                        
                    if elem == listeEnnemi[0]:
                        self.canvas.delete(elem)
                        self.canvas.delete(self.balle)
                        self.score += 100
                        self.myScore.config(text="Score : "+str(self.score))
                        self.master.bind( "<space>",self.shoot)  
                            
                self.master.after(100,self.mvtBalle)

        


    def ilots(self):
        #bloc 1
        for i in range(1,8):
            self.b1 = self.canvas.create_rectangle(170+i*30,640, #ligne 1
                                         200+i*30,670,
                                         outline = "black",
                                         fill = "brown",
                                         tags = "mur")
            listeIlots.append(self.b1)
            self.b1 = self.canvas.create_rectangle(170+i*30,610, #ligne 2
                                         200+i*30,640,
                                         outline = "black",
                                         fill = "brown",
                                         tags = "mur")
            listeIlots.append(self.b1)
            self.b1 = self.canvas.create_rectangle(170+i*30,580, #ligne 3
                                         200+i*30,610,
                                         outline = "black",
                                         fill = "brown",
                                         tags = "mur")
            listeIlots.append(self.b1)

        
        # bloc 2
        for i in range(1,8):
            self.b2 = self.canvas.create_rectangle(630+i*30,640, #ligne 1
                                          660+i*30,670,
                                          outline = "black",
                                          fill = "brown",
                                          tags = "mur")
            listeIlots.append(self.b2)
            self.b2 = self.canvas.create_rectangle(630+i*30,610, #ligne 2
                                          660+i*30,640,
                                          outline = "black",
                                          fill = "brown",
                                          tags = "mur")
            listeIlots.append(self.b2)
            self.b2 = self.canvas.create_rectangle(630+i*30,580, #ligne 3
                                          660+i*30,610,
                                          outline = "black",
                                          fill = "brown",
                                          tags = "mur")
            listeIlots.append(self.b2)
        
        # bloc 3
        for i in range(1,8):
            self.b3 = self.canvas.create_rectangle(1090+i*30,640, #ligne 1
                                         1120+i*30,670,
                                         outline = "black",
                                         fill = "brown",
                                         tags = "mur")
            listeIlots.append(self.b3)
            self.b3 = self.canvas.create_rectangle(1090+i*30,610, #ligne 2
                                         1120+i*30,640,
                                         outline = "black",
                                         fill = "brown",
                                         tags = "mur")
            listeIlots.append(self.b3)
            self.b3 = self.canvas.create_rectangle(1090+i*30,580, #ligne 3
                                         1120+i*30,610,
                                         outline = "black",
                                         fill = "brown",
                                         tags = "mur")
            listeIlots.append(self.b3)
            
          

    











    def menu(self):
        self.master.destroy() 
        self.master = Tk() 
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
