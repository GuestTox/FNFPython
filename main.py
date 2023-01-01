import pygame as pg, json, random

pg.init()

def loadConfig():
    try:
        with open("assets/data/config.json") as file:
            return json.load(file)
    except:
        config = {
            "Cheats": {
                "Speed": 1,
                "No Misses": False,
                "God Mode": False
            },
            "User Settings": {
                "Keybinds": ["D", "F", "K", "L"],
                "Note Colors": [(0, 255, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255)],
                "Dev Mode": False
            },
            "User Data": {
                "Songs": [
                    {
                    "Name": "Sugar Daddy Adventure",
                    "Score": 0
                    },
                    {
                    "Name": "Hot Mama Titties",
                    "Score": 0
                    },
                ]
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

    def draw(self, x, y):
        self.x = x
        self.y = y
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.y <= -50:
            self.y = 500 + self.yDelay
        else:
            self.y -= self.speed
        if self.isHit:
            self.y = 500 + self.yDelay
            self.isHit = False
        self.draw(self.x, self.y)
    
    def checkHit(self):
        if self.arrowParent.y - 50 < self.y < self.arrowParent.y + 50:
            self.isHit = True
            print(f"Hit {self.x}")

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
        pg.display.set_caption(self.TITLE)

        self.leftArrow = Arrow(90.0)
        self.upArrow = Arrow(0.0)
        self.downArrow = Arrow(180.0)
        self.rightArrow = Arrow(-90.0)
        self.leftNote = Note(self.leftArrow, random.randint(500, 900))
        self.upNote = Note(self.upArrow, random.randint(500, 900))
        self.downNote = Note(self.downArrow, random.randint(500, 900))
        self.rightNote = Note(self.rightArrow, random.randint(500, 900))

        self.arrows = [self.leftArrow, self.upArrow, self.downArrow, self.rightArrow]
        self.notes = [self.leftNote, self.upNote, self.downNote, self.rightNote]

        self.mainloop()

    def mainloop(self):
        running = True

        while running:
            screen.fill((255, 255, 255))
            posX = 430
            for arrow in self.arrows:
                arrow.draw(posX, 50)
                posX += 60
            for note in self.notes:
                note.x = note.arrowParent.x
                note.yDelay = random.randint(500, 750)
                note.move()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
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
    FNFGame = Game()
