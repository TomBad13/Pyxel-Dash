import tkinter as tk
import os,subprocess

#-----------------------------------------------
global TextureFile,GameFile
MainColor = "#7af09a"
SecondColor = "#1738cf"
ThirdColor = "#fcf451"
TextureFile = r""
GameFile = r""
#-----------------------------------------------

#-----------------------------------------------
def JeuLance():
    global Textures,TextureBtn,Games,GamesBtn,Txt3,Image
    Txt2.config(text="Welcome to PYXEL DASH! Please choose a Texture Pack.\n",bg=MainColor,fg=SecondColor,font=("Comic Sans MS", 20, "bold"))
    Txt3.destroy()
    Image.destroy()
    del Txt3,Image
    Textures = []
    TextureBtn = []
    Games = []
    GamesBtn = []
    for nom_fichier in os.listdir("Textures"):
        with open(f"Textures/{nom_fichier}", 'r'):
            Textures.append(nom_fichier)
    for Texture in Textures:
        TextureBtn.append(tk.Button(text=Texture[:str(Texture).index(".")],bg=ThirdColor,fg=SecondColor,font=("Comic Sans MS", 15, "bold"),command=lambda texture=Texture[:Texture.index(".")]: TextureDef(texture)))
        TextureBtn.append(tk.Label(bg=MainColor,text="",font=("Comic Sans MS", 5)))
    for TextureB in TextureBtn:
        TextureB.pack(fill="x")
    subprocess.run(["python", "Games\{}".format(GameFile), TextureFile])    
    with open(r"PointsLog.txt", "r") as f:
        readed = f.read()
    PtsTxt.config(bg=MainColor,text=f"You have {readed} wins!",font=("Comic Sans MS", 20, "bold"), fg=SecondColor)



def TextureDef(Texture):
    def GameDef(Game):
        global GameFile,TextureFile,Txt3,Image
        GameFile = Game + ".py"
        for GameB in GamesBtn:
            GameB.destroy()
        Txt2.config(text=f"You chose\nTextures: {TextureFile[:TextureFile.index('.')]}\nGame: {GameFile[:GameFile.index('.')]}")
        Txt3 = tk.Label(text="\n\nLOADING THE GAME...\n",bg=MainColor,fg=SecondColor,font=("Comic Sans MS", 20, "bold"))
        Txt3.pack()
        Image = tk.Label(image=GDImg,bg=MainColor,fg=SecondColor)
        Image.pack()
        fenetre.after(1000,JeuLance)
        # subprocess.run(["python", r"Games\{}".format(GameFile), TextureFile])

    global TextureFile
    TextureFile = Texture + ".pyxres"
    for TextureB in TextureBtn:
        TextureB.destroy()
    Txt2.config(text="Please choose a Game Mode\n")
    Games = []
    GamesBtn = []
    for nom_fichier in os.listdir("Games"):
        with open(f"Games/{nom_fichier}", 'r'):
            Games.append(nom_fichier)

    for Game in Games:
        GamesBtn.append(tk.Button(text=Game[:str(Game).index(".")],bg=ThirdColor,fg=SecondColor,font=("Comic Sans MS", 15, "bold"),command=lambda game=Game[:Game.index(".")]: GameDef(game)))
        GamesBtn.append(tk.Label(bg=MainColor,text="",font=("Comic Sans MS", 5)))
    for GamesB in GamesBtn:
        GamesB.pack(fill="x")


#-----------------------------------------------

fenetre = tk.Tk()
GDImg = tk.PhotoImage(file="Images/Logo.png")
fenetre.title("Pyxel Dash")
fenetre.iconbitmap("Images/Logo.ico")
fenetre.geometry("920x720+50+50")
fenetre.configure(bg=MainColor)
Txt1 = tk.Label(text="PYXEL DASH\n",bg=MainColor,fg=SecondColor,font=("Comic Sans MS", 40, "bold"))
Txt1.pack()
Txt2 = tk.Label(text="Welcome to PYXEL DASH! Please choose a Texture Pack.\n",bg=MainColor,fg=SecondColor,font=("Comic Sans MS", 20, "bold"))
Txt2.pack()
Textures = []
TextureBtn = []
for nom_fichier in os.listdir("Textures"):
    with open(f"Textures/{nom_fichier}", 'r'):
        Textures.append(nom_fichier)

for Texture in Textures:
    TextureBtn.append(tk.Button(text=Texture[:str(Texture).index(".")],bg=ThirdColor,fg=SecondColor,font=("Comic Sans MS", 15, "bold"),command=lambda texture=Texture[:Texture.index(".")]: TextureDef(texture)))
    TextureBtn.append(tk.Label(bg=MainColor,text="",font=("Comic Sans MS", 5)))
for TextureB in TextureBtn:
    TextureB.pack(fill="x")

with open(r"PointsLog.txt", "r") as f:
    readed = f.read()
PtsTxt = tk.Label(bg=MainColor,text=f"You have {readed} wins!",font=("Comic Sans MS", 20, "bold"), fg=SecondColor)
PtsTxt.pack(side="bottom")
fenetre.mainloop()
