import pyxel
from sys import argv

global actualtime,last_actualtime,resourcefile
actualtime,last_actualtime = 0, 0

try:
    resourcefile = r"..\Textures\{}".format(argv[1])
except IndexError:
    resourcefile = r"..\Textures\TextureThomas.pyxres"

class Carre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
    
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 1)
    
class CarreLost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 24, self.w, self.h, 1)
        
class Fond:
    def __init__(self):
        pass
    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 250, 120, 1)


class Bloc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, self.w, self.h, 1)

class Corde:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, self.w, self.h, 1)


class Pique:
    def __init__(self, x, y, r = False):
        self.x = x
        self.y = y
        self.w = 8
        if r == True:
            self.h = -8
        else:
            self.h = 8
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 8, self.w, self.h, 1)

class Monte:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 16, self.w, self.h, 1)

class Victoire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 16
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 24, self.w, self.h, 1) 

class App:
    def __init__(self):
        global resourcefile
        pyxel.init(248, 120, title="Pyxel Dash", quit_key=pyxel.KEY_ESCAPE, fps=60)
        pyxel.load(resourcefile)
        self.current_game_state = 1
        self.PointGiven = False
        self.jumping = 0
        self.fond = Fond()
        self.pique,self.bloc,self.monte,self.corde = [], [], [], []



        #CHANGER CI-DESSOUS POUR CREER LE NIVEAU
        self.carre = Carre() #POSITION DU CARRE | COORDONNES x et y entre les Parenthèses sous le format x,y
        self.victoire = Victoire() #POSITION DE LA VICTOIRE | COORDONNES x et y entre les Parenthèses sous le format x,y

        self.corde.append(Corde()) #POSITION DES CORDES | COORDONNES x et y entre les Parenthèses sous le format x,y [COPIER CETTE LIGNE POUR CHAQUE CORDE]

        self.monte.append(Monte()) #POSITION DES RAMPES | COORDONNES x et y entre les Parenthèses sous le format x,y [COPIER CETTE LIGNE POUR CHAQUE RAMPE]

        self.pique.append(Pique())  #POSITION DES PIQUES | COORDONNES x et y (et eventuellement le pique à l'envers) entre les Parenthèses sous le format x,y,reverse (True/False) [COPIER CETTE LIGNE POUR CHAQUE PIQUE]

        self.bloc.append(Bloc()) #POSITION DES BLOCS | COORDONNES x et y entre les Parenthèses sous le format x,y [COPIER CETTE LIGNE POUR CHAQUE BLOC]

        #CHANGER CI-DESSUS POUR CREER LE NIVEAU


        self.carrelost = CarreLost(self.carre.x, self.carre.y)
        pyxel.run(self.update, self.draw)

    def update(self):
        global actualtime,last_actualtime
        actualtime += 1
        if actualtime - 2 == last_actualtime:
            last_actualtime = actualtime
            if self.current_game_state == 1:
                for p in self.pique:
                    if p.x == self.carre.x and p.y == self.carre.y:
                        self.current_game_state = 0
                        pyxel.play(0, 0)
                    else:
                        for i in range(1,7+1):
                            if (p.x == self.carre.x + i or p.x + i == self.carre.x) and p.y == self.carre.y:
                                self.current_game_state = 0
                                pyxel.play(0, 0)
                    if self.current_game_state == 1:
                        p.x -= 1
                for b in self.bloc:
                    if b.x == self.carre.x and b.y == self.carre.y:
                        self.current_game_state = 0
                        pyxel.play(0, 0)
                    else:
                        for i in range(1,7+1):
                            if (b.x == self.carre.x + i or b.x + i == self.carre.x) and b.y == self.carre.y:
                                self.current_game_state = 0
                                pyxel.play(0, 0)
                    if self.current_game_state == 1:
                        b.x -= 1
                for m in self.monte:
                    if self.current_game_state == 1:
                        m.x -= 1
                for c in self.corde:
                    for i in range(1,2+1):
                        if (c.x == self.carre.x + i or c.x + i == self.carre.x) and c.y == self.carre.y:
                            self.current_game_state = 0
                            pyxel.play(0, 0)
                    c.x -= 1
                if self.current_game_state == 1:
                    self.victoire.x -= 1
        for m in self.monte:
            if m.x == self.carre.x and m.y == self.carre.y:
                self.carre.y -= 8
                self.carrelost.y -= 8
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)) and self.jumping == 0 and self.current_game_state == 1:
            self.jumping = 1
            self.carre.y -= 8
            self.carrelost.y -= 8
        platforme = False
        if self.jumping > 0:
            self.jumping += 1
        if (self.jumping == 0 or self.jumping == 55) and self.current_game_state == 1:
            self.jumping = 0
            for b in self.bloc:
                if b.y - 8 == self.carre.y and b.x == self.carre.x:
                    platforme = True
                    break
                else:
                    for i in range(1,7+1):
                        if (b.x == self.carre.x + i or b.x == self.carre.x - i) and b.y-8 == self.carre.y:
                            platforme = True
                            break
            for m in self.monte:
                if m.y - 8 == self.carre.y and m.x == self.carre.x:
                    platforme = True
                    break
            if platforme == False:
                self.carre.y += 8
                self.carrelost.y += 8
                platforme = True
        if self.carre.y > 120 and self.current_game_state == 1:
            self.current_game_state = 0
            pyxel.play(0, 0)
        if self.victoire.x == self.carre.x and self.current_game_state == 1 and self.PointGiven == False:
            self.PointGiven = True
            with open(r"..\PointsLog.txt","r") as f:
                readed = int(f.read())
                with open(r"..\PointsLog.txt","w") as f:
                    f.write(str(readed+1))
            self.current_game_state = 0
            pyxel.play(0, 1)

            
    def draw(self):
        self.fond.draw()
        if self.current_game_state == 1:
            self.carre.draw()
        elif self.current_game_state == 0 and self.carre.x != self.victoire.x:
            self.carrelost.draw()
        else:
            self.carre.draw()    
        self.victoire.draw()
        for p in self.pique:
            p.draw()
        for b in self.bloc:
            b.draw()
        for m in self.monte:
            m.draw()
        for c in self.corde:
            c.draw()
        pyxel.text(10, 110, "PLAYING" if self.current_game_state == 1 else "GAME OVER", 1)
        if self.current_game_state == 0:
            pyxel.text(10, 10, "Game made by Titouan, Sebastien, Jean-Baptiste and Thomas!", 3)
App()