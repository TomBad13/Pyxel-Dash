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
    def __init__(self, x, y, r = False):
        self.x = x
        self.y = y
        self.w = 8
        if r == True:
            self.h = -8
        else:
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
        self.current_game_state = 2
        self.PointGiven = False
        self.jumping = 0
        self.carre = Carre(32, 40)
        self.carrelost = CarreLost(32, 40)
        self.fond = Fond()
        self.pique,self.bloc,self.monte,self.corde = [], [], [], []
        for i in range(24, 152, 8):
            self.bloc.append(Bloc(i, 24))
        self.monte.append(Monte(144, 32, True))
        self.bloc.append(Bloc(152, 32))
        self.bloc.append(Bloc(160, 32))
        for i in range(176, 232, 8):
            self.bloc.append(Bloc(i, 32))
        for i in range(232, 272, 8):
            self.bloc.append(Bloc(i, 24))
        self.victoire = Victoire(264,32)
        self.pique.append(Pique(56, 32, True))
        self.pique.append(Pique(56, 48, False))
        for i in range(56, 256, 8):
            self.corde.append(Corde(56,i))
        self.pique.append(Pique(128, 40, False))
        for i in range(48, 256, 8):
            self.corde.append(Corde(128,i))
        pyxel.run(self.update, self.draw)
                
    def update(self):
        global actualtime,last_actualtime
        actualtime += 1
        if actualtime - 2 == last_actualtime:
            last_actualtime = actualtime
            if self.current_game_state > 0:
                for p in self.pique:
                    if p.x == self.carre.x and p.y == self.carre.y:
                        self.current_game_state = 0
                        pyxel.play(0, 0)
                    else:
                        for i in range(1,7+1):
                            if (p.x == self.carre.x + i or p.x + i == self.carre.x) and p.y == self.carre.y:
                                self.current_game_state = 0
                                pyxel.play(0, 0)
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
                    b.x -= 1
                for m in self.monte:
                    if self.current_game_state > 0:
                        m.x -= 1
                for c in self.corde:
                    for i in range(1,2+1):
                        if (c.x == self.carre.x + i or c.x + i == self.carre.x) and c.y == self.carre.y:
                            self.current_game_state = 0
                            pyxel.play(0, 0)
                    c.x -= 1
                if self.current_game_state > 0:
                    self.victoire.x -= 1
        for m in self.monte:
            if m.x == self.carre.x and m.y == self.carre.y and self.current_game_state == 1:
                self.carre.y -= 8
                self.carrelost.y -= 8
            elif m.x == self.carre.x and m.y == self.carre.y and self.current_game_state == 2:
                self.carre.y += 8
                self.carrelost.y += 8
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)) and self.jumping == 0 and self.current_game_state == 1:
            self.jumping = 1
            self.carre.y -= 8
            self.carrelost.y -= 8
        elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP)) and self.jumping == 0 and self.current_game_state == 2:
            self.jumping = 1
            self.carre.y += 8
            self.carrelost.y += 8
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
        elif (self.jumping == 0 or self.jumping == 55) and self.current_game_state == 2:
            self.jumping = 0
            for b in self.bloc:
                if b.y + 8 == self.carre.y and b.x == self.carre.x:
                    platforme = True
                    break
                else:
                    for i in range(1,7+1):
                        if (b.x == self.carre.x + i or b.x == self.carre.x - i) and b.y + 8 == self.carre.y:
                            platforme = True
                            break
            for m in self.monte:
                if m.y + 8 == self.carre.y and m.x == self.carre.x:
                    platforme = True
                    break
            if platforme == False:
                self.carre.y -= 8
                self.carrelost.y -= 8
                platforme = True
        if (self.carre.y > 120 or self.carre.y < 0 ) and self.current_game_state > 0:
            self.current_game_state = 0
            pyxel.play(0, 0)
        if self.victoire.x == self.carre.x and self.current_game_state > 0 and self.PointGiven == False:
            self.PointGiven = True
            with open(r"..\PointsLog.txt","r") as f:
                readed = int(f.read())
                with open(r"..\PointsLog.txt","w") as f:
                    f.write(str(readed+1))
            self.current_game_state = 0
            pyxel.play(0, 1)

            
    def draw(self):
        self.fond.draw()
        if self.current_game_state > 0:
            self.carre.draw()
        elif self.current_game_state == 0  and self.carre.x != self.victoire.x:
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
        pyxel.text(10, 110, "PLAYING" if self.current_game_state > 0 else "GAME OVER", 1)
        if self.current_game_state == 0:
            pyxel.text(10, 10, "Game made by Titouan, Sebastien, Jean-Baptiste and Thomas!", 3)
App()