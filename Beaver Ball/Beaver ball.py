import pygame
pygame.init()
print("Welcome to Beaver Ball")
win = pygame.display.set_mode((500, 480))#, pygame.FULLSCREEN)

pygame.display.set_caption("Beaver Ball")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player (object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isjump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
    def draw(self,win):
            if self.walkcount + 1 >= 27:
                self.walkcount = 0
            if self.left:
                win.blit(walkLeft[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walkRight[self.walkcount//3],(self.x,self.y))
                self.walkcount += 1
            else:
                win.blit(char, (self.x,self.y))


def redrawgamewindow():
    global walkcount
    win.blit(bg,(0,0))
    beaverbill.draw(win)
    pygame.display.update()



#mainloop
beaverbill = player (300,410,64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and beaverbill.x > beaverbill.vel:
        beaverbill.x -= beaverbill.vel
        beaverbill.left = True
        beaverbill.right = False
        
    elif keys[pygame.K_RIGHT] and beaverbill.x < 500 - beaverbill.width - beaverbill.vel:
        beaverbill.x += beaverbill.vel
        beaverbill.right = True
        beaverbill.left = False

    else:
        beaverbill.right = False
        beaverbill.left = False
        beaverbill.walkcount = 0


    if not (beaverbill.isjump):

        if keys[pygame.K_UP]:
            beaverbill.isjump = True
            beaverbill.right = False
            beaverbill.left = False
            beaverbill.walkcount = 0
    else:
        if beaverbill.jumpcount >= -10:
            neg = 1
            if beaverbill.jumpcount < 0:
                neg = -1
            beaverbill.y -= (beaverbill.jumpcount** 2) * 0.5 * neg
            beaverbill.jumpcount -= 1

        else:
            beaverbill.isjump = False
            beaverbill.jumpcount = 10
    redrawgamewindow()



pygame.quit()

