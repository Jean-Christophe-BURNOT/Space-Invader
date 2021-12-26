# -*- coding: utf-8 -*-
"""
Jean-Christophe BURNOT
12/12/2021
classe principale pour les ennemis
"""



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
   
        
   
    
   
class ennemis:
    def __ini__(self,niveau):
        self.__niveau = niveau
        




