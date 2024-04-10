import pyxel,random
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
        self.lengh = random.randrange(560,720,8)
        self.spawnpoint = [32,random.randrange(40,80,8)]
        self.carre = Carre(self.spawnpoint[0],self.spawnpoint[1])
        self.carrelost = CarreLost(self.spawnpoint[0],self.spawnpoint[1])
        self.bloc.append(Bloc(32,self.spawnpoint[1]+8))
        self.bloc.append(Bloc(40,self.spawnpoint[1]+8))        
        self.bloc.append(Bloc(48,self.spawnpoint[1]+8))        
        self.bloc.append(Bloc(56,self.spawnpoint[1]+8))
        self.spawnpoint[1] += 8
        PassTurn = False
        PastItemLog = ["B","B","B","B"]
        for i in range(64, self.lengh, 8):
            if PassTurn == True:
                PassTurn = False
            else:
                RandomAppear = random.randint(1,9)
                if RandomAppear <= 4: #PIQUE
                    self.bloc.append(Bloc(i,self.spawnpoint[1]))
                    if PastItemLog[-2] != "P" and PastItemLog[-3] != "P" and PastItemLog[-2] != "V" and PastItemLog[-3] != "V" and PastItemLog[-1] != "D" and PastItemLog[-1] != "PR":
                        self.pique.append(Pique(i,self.spawnpoint[1]-8))
                        if random.randint(1,5) == 1 and PastItemLog[-3] != "V" and PastItemLog[-3] != "P":
                            self.pique.append(Pique(i,self.spawnpoint[1]-24,True))
                            for j in range(0, self.spawnpoint[1]-24, 8):
                                self.corde.append(Corde(i,j))
                        PastItemLog.append("P")
                    else:
                        PastItemLog.append("B")
                elif RandomAppear <= 7: #MONTE
                    self.bloc.append(Bloc(i,self.spawnpoint[1]))  
                    if self.spawnpoint[1] - 16 != 0 and PastItemLog[-1] != "P" and PastItemLog[-1] != "V" and self.spawnpoint[1] != 240:
                        self.spawnpoint[1] -= 8
                        self.monte.append(Monte(i,self.spawnpoint[1]))
                        self.bloc.append(Bloc(i+8,self.spawnpoint[1]))
                        PassTurn = True
                        PastItemLog.append("M")
                    else:
                        self.bloc.append(Bloc(i,self.spawnpoint[1]))
                        PastItemLog.append("B")
                elif RandomAppear <= 8: #VIDE
                    if PastItemLog[-3] != "V" and PastItemLog[-2] != "V" and PastItemLog[-2] != "P" and PastItemLog[-1] != "PR":
                        PastItemLog.append("V")
                    else:
                        self.bloc.append(Bloc(i,self.spawnpoint[1]))
                        PastItemLog.append("B")
                elif RandomAppear <= 9: #DESCENTE
                    if self.spawnpoint[1] + 32 != 248 and self.spawnpoint[1] + 24 != 248 and self.spawnpoint[1] + 16 != 248 and self.spawnpoint[1] + 8 != 248 and PastItemLog[-1] != "P" and PastItemLog[-2] != "P" and PastItemLog[-1] != "V" and PastItemLog[-2] != "V":
                        self.spawnpoint[1] += random.randint(1,2)*8
                        self.bloc.append(Bloc(i,self.spawnpoint[1]))
                        PastItemLog.append("D")
                    else:
                        self.bloc.append(Bloc(i,self.spawnpoint[1]))
                        PastItemLog.append("B")
        self.bloc.append(Bloc(self.lengh,self.spawnpoint[1]))
        self.bloc.append(Bloc(self.lengh+8,self.spawnpoint[1]))
        self.bloc.append(Bloc(self.lengh+16,self.spawnpoint[1]))
        self.victoire = Victoire(self.lengh+16,self.spawnpoint[1]-16)
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