import pygame as pg, json, random

pg.init()
pg.mixer.init()

score = 0
misses = 0

GameVersion = 1.1

def changeScore(pos="None"):
    global score
    if pos is True:
        score += 50 
        return score
    elif pos is False:
        score -= 50
        return score
    elif pos == "None":
        return score

def Miss(add=None):
    global misses
    if add == "Yes": misses += 1
    return misses

def loadConfig():
    try:
        with open("assets/data/config.json") as file:
            if json.load(file)["Information"]["Version"] == GameVersion:
                return json.load(file)
            else:
                config = {
            "Information": {
                "Version": GameVersion,
                "Author": "GuestTox",
                "YACINE EST PD": True
            },
            "Cheats": {
                "Speed": 1,
                "No Misses": False,
                "God Mode": False
            },
            "User Settings": {
                "Keybinds": ["D", "F", "K", "L"],
                "Note Colors": [(0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255)],
                "Dev Mode": False
            }
        }
                with open("assets/data/config.json", "w") as file:
                    json.dump(config, file, indent=5)
                    return config
    except:
        config = {
            "Information": {
                "Version": GameVersion,
                "Author": "GuestTox",
                "YACINE EST PD": True
            },
            "Cheats": {
                "Speed": 1,
                "No Misses": False,
                "God Mode": False
            },
            "User Settings": {
                "Keybinds": ["D", "F", "K", "L"],
                "Note Colors": [(0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255)],
                "Dev Mode": False
            }
        }
        with open("assets/data/config.json", "w") as file:
            json.dump(config, file, indent=5)
        return config

config = loadConfig()

class Note():
    def __init__(self, arrowParent, yDelay) -> None:
        self.arrowParent = arrowParent
        self.image = self.arrowParent.image
        self.speed = config["Cheats"]["Speed"]
        self.yDelay = yDelay
        self.y = 600 + self.yDelay
        self.x = self.arrowParent.x
        self.isHit = False
        self.isVisible = True

    def draw(self, x, y):
        self.x = x
        self.y = y
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.y <= -50 or not self.isVisible:
            self.y = 500 + self.yDelay
            self.isVisible = True
        else:
            self.y -= self.speed
        if self.y <= -50:
            changeScore(False)
            Miss("Yes")
        if self.isHit or not self.isVisible:
            self.y = 500 + self.yDelay
            self.isHit = False
            self.isVisible = True
        self.draw(self.x, self.y)
    
    def checkHit(self):
        if self.arrowParent.y - 50 < self.y < self.arrowParent.y + 50:
            self.isHit = True
            changeScore(True)
        elif self.arrowParent.y + 50 < self.y < self.arrowParent.y + 300:
            self.isVisible = False
            changeScore(False)
            Miss("Yes")

class Arrow():
    def __init__(self, rotation) -> None:
        self.image = pg.transform.rotate(pg.transform.scale(pg.image.load("assets/images/arrow.png"), (50, 50)), rotation)
        self.lightImage = pg.transform.rotate(pg.transform.scale(pg.image.load("assets/images/arrowLight.png"), (50, 50)), rotation)
        self.light = False
        self.x = 0
        self.y = 0

    def draw(self, x, y):
        self.x = x
        self.y = y
        if self.light:
            screen.blit(self.lightImage, (self.x, self.y))
        elif not self.light:
            screen.blit(self.image, (self.x, self.y))

class Game():
    def __init__(self) -> None:
        self.WINDOW = (1100, 500)
        self.TITLE = "Friday Night Funkin: Pythonic Edition"

        global screen
        screen = pg.display.set_mode(self.WINDOW)
        self.score = 0
        pg.display.set_caption(self.TITLE)

        self.leftArrow = Arrow(90.0)
        self.upArrow = Arrow(0.0)
        self.downArrow = Arrow(180.0)
        self.rightArrow = Arrow(-90.0)
        self.leftNote = Note(self.leftArrow, random.randint(500, 900))
        self.upNote = Note(self.upArrow, random.randint(500, 900))
        self.downNote = Note(self.downArrow, random.randint(500, 900))
        self.rightNote = Note(self.rightArrow, random.randint(500, 900))

        self.font = pg.font.SysFont("arialblack", 40)

        self.arrows = [self.leftArrow, self.upArrow, self.downArrow, self.rightArrow]
        self.notes = [self.leftNote, self.upNote, self.downNote, self.rightNote]

        self.mainloop()

    def drawText(self, text, font, textColor, x, y):
        img = font.render(text, True, textColor)
        screen.blit(img, (x, y))

    def changeScore(self, pos):
        if pos: self.score += 50
        elif not pos: self.score -= 50

    def mainloop(self):
        self.running = True
        self.start = False

        pg.mixer.music.load("assets/music/freakyMenu.ogg")
        pg.mixer.music.set_volume(1.0)
        pg.mixer.music.play()

        self.music = "menu"

        while self.running:
            screen.fill((255, 255, 255))

            self.color = None

            while not self.start:
                self.color = random.randint(0, 50)
                self.color = (self.color, self.color, self.color)
                self.drawText("Press ENTER to start.", self.font, self.color, 250, 200)
                pg.display.flip()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.start = True
                        self.running = False
                    elif event.type == pg.KEYDOWN:
                        if event.key == pg.K_RETURN:
                            self.start = True

            if self.music == "menu":
                self.music = "bopeebo"
                pg.mixer.music.stop()
                self.inst = pg.mixer.Sound("assets/songs/bopeebo/Inst.ogg")
                pg.mixer.music.set_volume(1.0)
                pg.mixer.Channel(0).play(self.inst)
                self.voices = pg.mixer.Sound("assets/songs/bopeebo/Voices.ogg")
                pg.mixer.music.set_volume(1.0)
                pg.mixer.Channel(1).play(self.voices)

            posX = 430
            for arrow in self.arrows:
                arrow.draw(posX, 50)
                posX += 60
            for note in self.notes:
                note.x = note.arrowParent.x
                note.yDelay = random.randint(500, 750)
                note.move()
            self.drawText(f"Score: {changeScore()}", self.font, (0, 0, 0), 50, 50)
            self.drawText(f"Misses: {Miss(None)}", self.font, (0, 0, 0), 50, 100)
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.start =  False
                    if event.key == pg.K_d or event.key == pg.K_LEFT:
                        # if self.leftArrow.light == 0:
                            self.leftArrow.light = True
                            self.leftNote.checkHit()
                    elif event.key == pg.K_f or event.key == pg.K_UP:
                        # if self.upArrow.light == 0:
                            self.upArrow.light = True
                            self.upNote.checkHit()
                    elif event.key == pg.K_k or event.key == pg.K_DOWN:
                        # if self.downArrow.light == 0:
                            self.downArrow.light = True
                            self.downNote.checkHit()
                    elif event.key == pg.K_l or event.key == pg.K_RIGHT:
                        # if self.rightArrow.light == 0:
                            self.rightArrow.light = True
                            self.rightNote.checkHit()
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_d or event.key == pg.K_LEFT:
                        # if self.leftArrow.light == 0:
                            self.leftArrow.light = False
                    elif event.key == pg.K_f or event.key == pg.K_UP:
                        # if self.upArrow.light == 0:
                            self.upArrow.light = False
                    elif event.key == pg.K_k or event.key == pg.K_DOWN:
                        # if self.downArrow.light == 0:
                            self.downArrow.light = False
                    elif event.key == pg.K_l or event.key == pg.K_RIGHT:
                        # if self.rightArrow.light == 0:
                            self.rightArrow.light = False

if __name__ == "__main__":
    global FNFGame
    FNFGame = Game()